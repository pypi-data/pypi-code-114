#!/bin/python
import importlib
import pandas as pd
import os
import dorianUtils.comUtils as comUtils
import time,datetime as dt,sys
import monitorBuildingDash.screenBuilding as screenBuilding
mb_utils=comUtils.Modebus_utils()
dumper_screenBuilding = screenBuilding.ScreeningBuilding_dumper()
# =================================================================
['meteo','smartlogger','vmuc','site_sls']
deviceClient = dumper_screenBuilding.devices['smartlogger']
# deviceClient.client.connect()
# d=deviceClient.get_slave_values(1)
# d=pd.DataFrame(d).T
start=time.time()
deviceClient.insert_intodb(dumper_screenBuilding.dbParameters)
d = deviceClient.collectData()
# deviceClient.checkConnection()
# res = pd.DataFrame(d).T
# print(res)
