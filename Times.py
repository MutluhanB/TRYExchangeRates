import datetime,time

def getTime():
    return datetime.datetime.now().replace(microsecond=0)
