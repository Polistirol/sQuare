from django.contrib.auth.models import User
from api.models import BetsStats,OpenBids,SiteSettings
from datetime import datetime,timedelta
import pytz

def rebalance():
    coins = BetsStats.objects.all()
    settings = SiteSettings.objects.get(id=1)

    #manage timer system
    settings.timeToNextUpdate=datetime.now().replace(tzinfo=pytz.utc)+timedelta(seconds=settings.secondsToAPIRequest)
    settings.save()
    
    #manage bet system
    for coin in coins:
        openBids = OpenBids.objects.all().filter(currency = coin.currency,status = 0)

        for openBid in openBids:
            print(openBid.id)
            user = openBid.user
            if coin.green and openBid.vote == 1:
                #Victory
                openBid.status = 1
                user.profile.credit += openBid.bidAmount
            else:
                openBid.status = -1
                user.profile.credit -= openBid.bidAmount
            user.profile.isBetting = False
            user.save()
            openBid.save()
    return
