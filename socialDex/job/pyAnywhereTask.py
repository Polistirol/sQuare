#this task is used by pythonAnywhere instead of schedule (not available in PAW)
#runs timilar to origina one buy only once a day , at 12.00 CET

from fetch import fetchDataFromApi

def startTask():
    print("Task is now running!")
    fetchDataFromApi()