#!/bin/python
from configScreenBuilding import *

# ==============================================================================
#                           GENERATE RANDOM DATA
def generateRandomData():
    t1 = dt.datetime(2021,11,18,17,20).astimezone()
    t0 = t1-dt.timedelta(days=1,hours=t1.hour,minutes=t1.minute)
    streaming.generateRandomParkedData(t0,t1,vmucConfig.folderPkl,vmucConfig.allTags)
