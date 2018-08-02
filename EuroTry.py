import json
from urllib.request import urlopen

def checkE():
    with urlopen("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=EUR&to_currency=TRY&apikey=5Y57NAHCNN1GRX1O") as euroRequest:
        euroSource = euroRequest.read()
        euroData = json.loads(euroSource)
        return euroData

def getEuroName():
    euroName = euroData["Realtime Currency Exchange Rate"]["2. From_Currency Name"]
    return euroName

def getEuroTryRate():
    euroRate = checkE()["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    return euroRate

def checkEuroData():
    return euroData
