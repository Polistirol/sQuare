from .fetch import fetchDataFromApi
from  apscheduler.schedulers.background import BackgroundScheduler


def startSchedule():
    try: 
        from api.models import SiteSettings
        setups = SiteSettings.objects.get(id=1)
        secondsForSchedule= setups.secondsToAPIRequest -2  #the -2 are 2 seconds use to update the prices and the database before refreshing the page
    except:
        secondsForSchedule = 5

    scheduler = BackgroundScheduler()
    scheduler.add_job(fetchDataFromApi,'interval',seconds=secondsForSchedule)
    scheduler.start()
    