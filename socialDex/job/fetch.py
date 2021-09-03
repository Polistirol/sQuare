import requests
from api.models import BetsStats
from job.rebalance import rebalance

def fetchDataFromApi():
    urlCJ= "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum&vs_currencies=usd" #get from api eth and btc over USD
    dataFromAPI = requests.get(url = urlCJ).json()
    coins = list(dataFromAPI.keys())
    data = []
    for i in range(len(coins)):
        name = coins[i]
        curr = BetsStats.objects.get(currency = name)
        newPrice = dataFromAPI[coins[i]]["usd"]       
        if  newPrice > curr.currentPrice :
            curr.green = True
        else: curr.green = False
        lastPrice_toSet = curr.currentPrice
        curr.lastPrice = lastPrice_toSet
        curr.currentPrice = newPrice
        curr.save()
    print("Betting prices updated !" )
    rebalance()
    return 