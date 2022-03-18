# PROPRIETARY LIBS
import userconfig
logger = userconfig.getLogger(__file__)
from Routines.RoutineScheduler import RoutineScheduler
import time
from datetime import datetime

sched = RoutineScheduler(logger)
sched.getPendingRoutines()

while(True):
    print('',end='\r')
    print('Running Schedule %s' % (str(datetime.now())),end='')
    if sched.schedule['Run Times'][0].date()<datetime.now().date():
        print('')
        print('Reloading Schedule %s' % (str(datetime.now())))
        print('')
        sched.LoadSchedule()
        sched.getPendingRoutines()
        sched.RefreshLogs()

    sched.RunPendingRoutines()
    sched.RefreshLogs()
    time.sleep(5) 