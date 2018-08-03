from DollarTry import*
from EuroTry import*
from DbThings import*
import time

lastValD=0
lasttimeD=0
lastValE=0
LastTimeE=0
print("Tracking Started At : " + str(getTime()))
createdbDollar()
createdbEuro()
while True:
    time.sleep(61)
    try:
        dollarRate = getDollarTryRate()
        euroRate = getEuroTryRate()
    except Exception as e:
        print("No connection ..!")
        break


    if(lastValD != dollarRate):
        lastTimeD = getTime()
        lastValD = dollarRate
    if(lastValE != euroRate):
        lastTimeE = getTime()
        lastValE = euroRate

    print("USD/TRY: " + str(dollarRate) + " Last Updated At : " + str(lastTimeD))
    print("EUR/TRY: " + str(euroRate) + " Last Updated At : " + str(lastTimeE))
    print("\n")

    DollarDbInsert(lastTimeD,lastValD)
    euroDbInsert(lastTimeE,lastValE)
    time.sleep(61)

    while ((lastValD == getDollarTryRate()) and (lastValE == getEuroTryRate())):
        time.sleep(61)

input("Press any key to exit...")
