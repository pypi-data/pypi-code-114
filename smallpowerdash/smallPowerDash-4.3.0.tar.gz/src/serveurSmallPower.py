#!/bin/python
import importlib
import comUtils
import time,datetime as dt,sys
importlib.reload(comUtils)
import smallPower
importlib.reload(smallPower)
# ==============================================================================
#                           MAIN SIMULATOR
simulatorBECKHOFF = smallPower.Simulator_SP()
simulatorBECKHOFF.start()
