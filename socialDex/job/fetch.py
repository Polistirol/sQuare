import requests
from api.models import BetsStats
from job.rebalance import rebalance

def fetchDataFromApi():
    urlCJ= "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum&vs_currencies=usd" #get from api eth and btc over USD
    #urlCJ = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=1&interval=minutely"
    dataFromAPI = requests.get(url = urlCJ).json()
    coins = list(dataFromAPI.keys())
    
    for i in range(len(coins)):
        name = coins[i]
        curr = BetsStats.objects.get(currency = name)
        newPrice = dataFromAPI[coins[i]]["usd"]       
        if  newPrice >= curr.currentPrice :
            curr.green = True
        else: curr.green = False

        lastPrice_toSet = curr.currentPrice
        curr.lastPrice = lastPrice_toSet
        curr.save()
        curr.currentPrice = newPrice
        curr.save()        
        #print( "new", curr.currentPrice, newPrice)
        #print( "last", curr.lastPrice , lastPrice_toSet)

    print("Betting prices updated !" )
    rebalance()
    return 

