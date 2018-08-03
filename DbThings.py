import sqlite3

def createdbDollar():
    dconnection = sqlite3.connect("../dollarTry.db")
    dc=dconnection.cursor()
    try:
        dc.execute("""CREATE TABLE ratesAndTimes
        (time text,rate real)""")
        dc.commit()
    except Exception as e:
        pass

def DollarDbInsert(date,value):
    dconnection = sqlite3.connect("../dollarTry.db")
    dc=dconnection.cursor()
    dc.execute(""" INSERT INTO ratesAndTimes VALUES (?,?)""",(date,value))
    dconnection.commit()

def createdbEuro():
    econnection = sqlite3.connect("../euroTry.db")
    ec=econnection.cursor()
    try:
        ec.execute("""CREATE TABLE ratesAndTimes
        (time text,rate real)""")
        dconnection.commit()
    except Exception as e:
        pass

def euroDbInsert(date,value):
    econnection = sqlite3.connect("../euroTry.db")
    ec=econnection.cursor()
    ec.execute(""" INSERT INTO ratesAndTimes VALUES (?,?)""",(date,value))
    econnection.commit()
