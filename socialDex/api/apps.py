from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        from job import schedule,fetch
        try:
            schedule.startSchedule()
            print("The scheduler has started")
            fetch.fetchDataFromApi()
        except Exception as e:
            print("The scheduler is not running, check console for details ")
            print("NOTE: If using pythonanywhare this is expected, \nschedule is Tasked and it will run dayily at 12.00 CET ")
            print(e , e.args )        
        return
    