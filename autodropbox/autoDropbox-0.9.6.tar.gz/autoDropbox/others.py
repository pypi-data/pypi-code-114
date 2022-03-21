import time,datetime
from datetime import timezone


def getTime():
    t = time.time()
    t = int(1000 * t)
    return t



def toUnix(timeStr:str):
    dt = datetime.datetime.strptime(timeStr, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)
    return int(1000*dt.timestamp())


