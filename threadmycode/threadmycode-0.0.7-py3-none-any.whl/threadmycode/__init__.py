from threading import Thread, active_count
import time
import os
import logging
from sys import exit as sysexit
from os import _exit as osexit
import traceback

config = {'STOP':False,'KILLALL':False}

def stop(self, cls):
    logging.info('Stop Signal Recieved')
    global config
    config['STOP'] = True
    return

def killall(self, cls):
    logging.info('kill All Signal Recieved')
    try:
        sysexit(0)
    except SystemExit:
        osexit(0)
          
def threadCount(count):
    config['threadCount'] = count
    return 

def threadit(func):
    try:
        global config
        def wrapper(*args,**kwargs):
            if args and (type(args[0]) in [list,tuple,map]):
                def proc():
                    return "Processed"
                threads = []
                maxThread = config.get('threadCount')
                if maxThread is None:
                    maxThread = os.cpu_count() + 1
                if maxThread<=3:
                    maxThread = 3
                if maxThread>(os.cpu_count() * 10):
                    maxThread = os.cpu_count() * 10
                logging.info('Maxthread:' + str(maxThread))
                for elem in args[0]:
                    if config['STOP']:
                        break
                    while True:
                        activecount = active_count()
                        if (activecount>=maxThread):
                            time.sleep(1)
                        else:
                            break
                    logging.info('Active Count:' + str(activecount))
                    newArgs = (elem,) + args[1:]
                    if (activecount<maxThread):
                        t1 = Thread(target = func, args =newArgs,kwargs=kwargs)
                        t1.start()
                        logging.info('Thread Started with args:' + str(newArgs) + ' and kwargs ' + str(kwargs))
                        threads.append(t1)
                for thread in threads:
                    thread.join()
                return proc
            else:
                x=func(*args,**kwargs)
                return x
    except:
        logging.error(traceback.format_exc())
        
    return wrapper

