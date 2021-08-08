# Djanogss
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.serializers.json import DjangoJSONEncoder
# libs
import pytz
import hashlib
import json
from  datetime import datetime, timedelta
# app
from api.wallet import sendTransaction


# Create your models here.
class SiteSettings(models.Model):
    timeToNextUpdate = models.DateTimeField(default = datetime.now().replace(tzinfo=pytz.utc))
    creditsForTimeSlotView = models.IntegerField(default=10)#number of credits to buy 1 time slot 
    timeSlotDuration = models.IntegerField(default=10) #duration of 1 timeslot
    secondsToAPIRequest = models.IntegerField(default = 300)

    def save(self, *args, **kwargs):
        if not self.pk and SiteSettings.objects.exists():
            raise Exception('impossible to create more settings!')
        return super(SiteSettings, self).save(*args, **kwargs)


class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    title = models.CharField(max_length = 50)
    isPublic = models.BooleanField()
    msgHash = models.CharField(max_length = 32, default = None ,null = True )
    txId = models.CharField(max_length = 32, default = None ,null = True )

    def WriteOnChain(self):

        msgPack = {
            "author": self.user.username,
            "timestamp": self.datetime,
            "title" : self.title,
            "content" : self.content,
            "isPublic" : self.isPublic
        }
        if not self.isPublic:
            msgPack["content"] = "nono! you won't see the private posts here my friend !" 
        msgPack = json.dumps(msgPack,sort_keys=False,indent=1,cls=DjangoJSONEncoder)
        self.msgHash = hashlib.sha256(msgPack.encode("utf-8")).hexdigest()
        self.txId = sendTransaction(msgPack)
        self.save()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credit = models.IntegerField( default=10)
    isBetting = models.BooleanField(default=False)
    hasView = models.BooleanField(default=False)
    expiringTime = models.DateTimeField(default=datetime.now())
    viewStart = models.DateTimeField(default=datetime.now())
    


    def startView(self):
        self.viewStart = datetime.now() 
        self.hasView = True
        self.save()

    def addTime(self,spentCredits):
        settings= SiteSettings.objects.get(id=1)
        if self.credit >= spentCredits and spentCredits >= int(settings.creditsForTimeSlotView):
            extension = int(settings.timeSlotDuration) * (spentCredits//10)
            if not self.hasView:
                self.startView()
                self.expiringTime = self.viewStart + timedelta(minutes=extension)
            else:
                self.expiringTime = self.expiringTime + timedelta(minutes=extension)
            self.credit -= spentCredits
            self.save()
        else: 
            print("NOT ENOUGHT CREDIT !")

    def checkHasView(self):
        if self.expiringTime.replace(tzinfo=pytz.utc) >= datetime.now().replace(tzinfo=pytz.utc):
            self.hasView = True
        else :
            self.hasView = False
        self.save()



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class BetsStats(models.Model):
    currency = models.CharField(max_length= 30)
    lastPrice = models.FloatField(default =0 )
    currentPrice = models.FloatField(default =0 )
    green = models.BooleanField(default = False)

    def __str__(self):
        return self.currency


class OpenBids(models.Model):
    OPEN = 0
    WIN = 1
    LOSS = -1
    Status = ((OPEN ,"OPEN"),(WIN,"WIN"),(LOSS,"LOSS"))

    UP = 1
    DOWN= -1
    Vote = ((UP,"UP"),(DOWN,"DOWN"))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    currency =  models.CharField(max_length = 30)
    bidAmount = models.IntegerField(default=0)
    status = models.IntegerField(choices=Status,default=OPEN)
    returns = models.IntegerField(default=0)
    vote = models.IntegerField(choices=Vote,default = UP)

