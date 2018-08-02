import json
from urllib.request import urlopen
from Times import getTime

def checkD():
    with urlopen("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=TRY&apikey=5Y57NAHCNN1GRX1O") as dollarRequest:
        dollarSource = dollarRequest.read()
        dollarData = json.loads(dollarSource)
        return dollarData
def checkDollarData():
    return dollarData

def getDollarName():
    dollarName = dollarData["Realtime Currency Exchange Rate"]["2. From_Currency Name"]
    return dollarName

def getDollarTryRate():

    dollarRate = checkD()["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    return dollarRate
