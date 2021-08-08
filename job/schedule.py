from .fetch import fetchDataFromApi
from  apscheduler.schedulers.background import BackgroundScheduler


def startSchedule():
    try: 
        from api.models import SiteSettings
        setups = SiteSettings.objects.get(id=1)
        secondsForSchedule= setups.secondsToAPIRequest
    except:
        secondsForSchedule = 5

    scheduler = BackgroundScheduler()
    scheduler.add_job(fetchDataFromApi,'interval',seconds=secondsForSchedule)
    scheduler.start()
    