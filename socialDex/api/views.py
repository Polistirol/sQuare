from django.shortcuts import render
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User

from .models import Post,BetsStats,OpenBids,SiteSettings
from .forms import WritePost
from datetime import datetime,timedelta
from django.utils import timezone
from django.contrib import messages
import requests
import pytz
from ipware import get_client_ip


# Create your views here.

def home(request):
    return render(request,"api/home.html")

def userId(response,id):
    if response.user.is_authenticated:
        try:
            user = User.objects.get(id=id) 
            bets = OpenBids.objects.all().filter(user = user)
            postsNumber = Post.objects.all().filter(user = user).count()
            profit =0 
            for bet in bets:
                profit += bet.status * bet.bidAmount
            userInfo = {"bets": len(bets),"profit":profit}
            return render(response,"api/personal.html", {"user":user,"userInfo":userInfo,"postsNumber":postsNumber})
        except :
            return HttpResponseRedirect("/users/")
    else:
        return HttpResponseRedirect("/square/")

def postId(response,id):
        if response.user.is_authenticated and response.user.is_staff:
            try :
                post = Post.objects.get(id = id)
                response ={
                        "ID" : post.id,
                        "datetime" : post.datetime,
                        "author" : { "Username" : post.user.username ,
                                    "Name" : post.user.first_name ,
                                    "Surname" : post.user.last_name },
                                    
                        "Title" : post.title,
                        "content" : post.content,
                        "Public Post " : post.isPublic
                    }
                return JsonResponse(response,safe = False)
            except:
                response = {"Error - No Post with ID:" : id}
                return JsonResponse(response,safe = False)
        elif not response.user.is_staff:
            response = "You don't have Admin permissions to see this page"
            return JsonResponse(response,safe = False)
        else: 
            return HttpResponseRedirect("/square/")


def posts(request, key = None ):
    if request.user.is_authenticated :
        response = []
        posts=None
        if key == None :
            now = timezone.now().replace( second=0, microsecond=0)
            one_hour_ago = now - timedelta(hours=1)
            posts = Post.objects.filter(datetime__range=( one_hour_ago,now))

        elif key == "all"and request.user.is_staff:
            posts = Post.objects.filter().order_by("-datetime")
        
        elif key == "all" and not request.user.is_staff:         
            response.append("You don't have Admin permissions to see this page")
            return JsonResponse(response,safe = False)

        if posts :
            response.append({
                            "Number of posts" : len(posts),
                            "First post date" : posts[0].datetime,
                            "Last post date" : posts[len(posts)-1].datetime
                            })
            for post in posts:
                response.append(
                    {
                        "ID" : post.id,
                        "datetime" : post.datetime,
                        "author" : { "Username" : post.user.username ,
                                    "Name" : post.user.first_name ,
                                    "Surname" : post.user.last_name },
                        "Title" : post.title,
                        "content" : post.content if post.isPublic else "*****",
                        "Public Post " : post.isPublic,
                        "Message Hash": post.msgHash,
                        "Transaction ID" : post.txId
                    }) 
        else:
                response.append("No Posts found Here !" )
        return JsonResponse(response,safe = False)
    else: 
        return HttpResponseRedirect("/square/")

def users(request, key = None):
    if request.user.is_authenticated:
        users = User.objects.all()
        response=[]
        if not key:
            return render(request,"api/users.html",{"users":users})
        elif key == "all":
            if request.user.is_staff:
                for user in users:
                    postsInfo=[]
                    userPosts= Post.objects.all().filter(user = user).order_by("-id")
                    for post in userPosts:
                        postsInfo.append({
                            "Post ID":post.id,
                            "Title":post.title,
                            "Public": post.isPublic
                        })                
                    response.append({
                                    "User ID" : user.id,
                                    "Username" : user.username,
                                    "Is Active" : user.is_active,
                                    "Is Admin" : user.is_staff,
                                    "Is Betting" : user.profile.isBetting,
                                    "Has Vision" : user.profile.hasView,
                                    "Posts Count" : len(userPosts),
                                    "Posts Info" : postsInfo
                                    })
                return JsonResponse(response,safe = False)
            else:
                response.append("You don't have Admin permissions to see this page")
                return JsonResponse(response,safe = False)
    else: 
        return HttpResponseRedirect("/square/")

def profile(request):
    if request.user.is_authenticated:
        username = request.user.get_username()
        user = request.user
        posts = Post.objects.filter(user = user).order_by("-id")
        bets = OpenBids.objects.all().filter(user = user).order_by("-id")
        profit =0 
        for bet in bets:
            profit += bet.status * bet.bidAmount
        betStats= {"wins" : OpenBids.objects.all().filter(user = user,status=1).count(), 
                    "losses": OpenBids.objects.all().filter(user = user,status =-1).count(),
                    "profit": profit}
        return render(request,"api/my-profile.html",{"posts":posts, "user": user,"bets":bets, "betStats":betStats })
    else:
        return render(request,"api/my-profile.html",{ })

def bet(request):
    user = request.user
    coinsData = BetsStats.objects.all()
    remainingTime= getRemainingTime(SiteSettings.objects.get(id=1).timeToNextUpdate)
    if request.method == "POST":
        bid(request)
        return render(request,"api/bet.html",{ "user":user, "coinsData" : coinsData,"time":remainingTime})        
    else:
        return render(request,"api/bet.html",{ "user":user, "coinsData" : coinsData,"time":remainingTime})

def bid(request):
    user = request.user
    aviableCredits = user.profile.credit
    bid = int(request.POST.get("quantity", None))
    canBid = True if bid >0 and bid <=aviableCredits and not user.profile.isBetting else False
    if canBid:
        currency = request.POST.get("currencies",None)
        if request.POST.get("betUp", None):
            vote = 1
        elif request.POST.get("betDown", None):
            vote = -1
        user.profile.isBetting = True
        user.save()
        #create a bid object
        OpenBids.objects.create(user = user, currency = currency , bidAmount = bid , vote = vote)
        return
    else:
        print("cant bid")
        #bid impossible
        return

def checkIP(response):
    user = response.user
    ip,is_routable =   get_client_ip(response) 
    ipdata = ""
    if not ip:
        msg = "It was impossible to get your IP !"
        return render( response ,"api/my-ip.html",{"ip":ip,"msg":msg})

    else:
        url_ip_api = "http://ip-api.com/json/"+str(ip)
        ipdata = requests.get(url_ip_api).json()
        if ipdata["status"] == "success":
            ip_country = ipdata["country"]
            ip_city = ipdata["city"]
            if not isIPChanged(user,ip,ip_city,ip_country):
                return HttpResponseRedirect("/my-profile/")
            else:
                msg = "Your ip has changed ! IP : %s - Country : %s - City : %s" %(ip,ip_country,ip_city)
                messages.info(response, " ")
                return render( response ,"api/my-ip.html",{"ip":ip,"msg":msg})
        return HttpResponseRedirect("/my-profile/")




def square(response):
    user = response.user
    if not user.is_authenticated:
        return render(response, "api/square.html",{})

    posts = filterForView(user)
    time = getRemainingTime( user.profile.expiringTime.replace(tzinfo=pytz.utc))
    #print(response.META.get('HTTP_X_FORWARDED_FOR', response.META.get('REMOTE_ADDR', '')).split(',')[0].strip())
    if response.method == "POST":
        # manage seach bar
        if response.POST.get("src", None) and response.POST.get("srcInput",None):
            postsFound=[]
            srcInput = response.POST.get("srcInput",None).strip().lower()
            for post in posts:
                if srcInput in post.title.lower() or srcInput in post.content.lower() :
                    bolded  = "<b><u>"+srcInput+"</u></b>"
                    post.title = post.title.lower().replace(srcInput,bolded)
                    post.content = post.content.lower().replace(srcInput,bolded)
                    postsFound.append(post)
            return render(response, "api/srcResults.html",{"posts":postsFound , "srcInput":srcInput.capitalize()})
                    #return JsonResponse(postsFound,safe = False)
        #manage view power
        if response.POST.get("view", None):
            spentCredits = int(response.POST.get("quantity", None))
            manageView(user,spentCredits)
            return HttpResponseRedirect("/square/")
        #manage post form
        form = WritePost(response.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            if hasForbiddenWord(title) or  hasForbiddenWord(content):
                messages.info(response,"error")
                form = WritePost()
                return render(response, "api/square.html",{"posts":posts,"form":form,"time":time})
            isPublic = not form.cleaned_data['isPublic']
            newPost = response.user.post_set.create(title = title , content = content, isPublic = isPublic)
            newPost.WriteOnChain()
            return HttpResponseRedirect("/square/")
    else:
        form = WritePost()
    return render(response, "api/square.html",{"posts":posts,"form":form,"time":time})

"""UTILITY METHODS"""

def getRemainingTime(expiringTime):
    now = datetime.now().replace(tzinfo=pytz.utc)
    remainingTime = expiringTime-now
    remainingTime = int(remainingTime.total_seconds())
    return remainingTime
    
def hasForbiddenWord(text):
    word = "HACK"
    if word in text.upper():
        return True
    else: return False
        
def search(response):
    posts = Post.objects.all()
    n_times = 0
    print(posts)

def filterForView(user):
        #manage what is displayed
    user.profile.checkHasView()
    #has view:
    if user.profile.hasView:
        posts = Post.objects.all().filter().order_by("-datetime")
    #has not view:
    if not user.profile.hasView:
        posts = Post.objects.all().filter(isPublic = True).order_by("-datetime")
    return posts

def manageView(user,spentCredits):
    user.profile.addTime(spentCredits)
    return

def isIPChanged(user,ip,city,country):
    if user.profile.lastIP != ip :
        print("different ip")
    if user.profile.lastCity != city :
        print("different city")
    if user.profile.lastCountry != country:
        print("different country")
        return True
    else : return False

