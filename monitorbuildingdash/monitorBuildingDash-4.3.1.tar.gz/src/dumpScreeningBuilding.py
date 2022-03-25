#!/bin/python
import importlib
import pandas as pd
import os
import dorianUtils.comUtils as comUtils
import time,datetime as dt,sys
import monitorBuildingDash.screenBuilding as screenBuilding
importlib.reload(screenBuilding)
start=time.time()

dumper_screenBuilding = screenBuilding.ScreeningBuilding_dumper()
# dumper_screenBuilding.park_database()
dumper_screenBuilding.start_dumping()
