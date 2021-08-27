from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . forms import SignUpForm
from ipware import get_client_ip
import requests


# Create your views here.
def signup(response):
    if response.method == "POST":
        reg_form = SignUpForm(response.POST)
        if reg_form.is_valid():
            reg_form.save()
            new_user = authenticate(username=reg_form.cleaned_data['username'],
                                    password=reg_form.cleaned_data['password1'],
                                    )
            user = User.objects.get(username = reg_form.cleaned_data['username'] )                        
            saveIPinfo(response,user)                        
            login(response, new_user)        
            return redirect("/")
    else:
        reg_form= SignUpForm()
    return render(response,"signup/sign-up.html",{"reg_form": reg_form})

def saveIPinfo(response,user):
    ip,is_routable =   get_client_ip(response) 
    ipdata = ""
    if  ip:
        user.profile.lastIP = ip
    if is_routable:
        url_ip_api = "http://ip-api.com/json/"+str(ip)
        ipdata = requests.get(url_ip_api).json()
        if ipdata:
            user.profile.lastCountry = ipdata["country"]
            user.profile.lastCity = ipdata["city"]
    user.save()
