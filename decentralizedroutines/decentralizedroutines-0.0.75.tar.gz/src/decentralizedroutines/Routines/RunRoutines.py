# PROPRIETARY LIBS
import sys,time
from Routines.RoutineScheduler import RoutineScheduler
from datetime import datetime

from SharedData.Logger import Logger
logger = Logger(__file__)
from SharedData.SharedDataAWSKinesis import KinesisLogStreamConsumer

consumer = KinesisLogStreamConsumer()
sched = RoutineScheduler(consumer)
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