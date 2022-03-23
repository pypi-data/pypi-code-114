import pandas as pd
pd.set_option('display.max_rows', None)
# PROPRIETARY LIBS
import userconfig
logger = userconfig.getLogger('Notebook/Routines_Report.py')
from Routines.RoutineScheduler import RoutineScheduler

sched = RoutineScheduler(logger)
sched.getPendingRoutines()