'''
celery worker for periodicly update plot data
'''
from urllib.request import urlopen
from celery import Celery
from worker import load_hosts
from G_VAR import R_PATH
import os
import json
import time

# init celery instance for this worker
celery = Celery(__name__)

# init celery beat
@celery.on_after_configure.connect
def periodicUpdateData(sender, **kwargs):
    sender.add_periodic_task(60.0, updateHostsData, name = 'update-every-60-seconds')

# load and update plot data
@celery.task()
def updateHostsData():
    hosts = load_hosts()
    gpustats = []

    for name in hosts:
        gpustat = {}
        try:
            resp = urlopen(hosts[name] + '/gpustat', timeout = 10)
        except Exception as e:
            gpustats.append({
                'hostname': name,
                'connection': 'False',
            })
            continue

        rawstat = json.loads(resp.read())
        resp.close()

        if 'error' in rawstat:
            gpustats.append({
                'hostname': name,
                'connection': 'True',
                'error': rawstat['error']
            })
        else:
            gpustat['hostname'] = name
            gpustat['connection'] = 'True'
            
            sumTotMem = 0
            sumUsedMem = 0
            for gpu in rawstat['gpus']:
                sumTotMem += gpu['memory.total']
                sumUsedMem += gpu['memory.used']
            
            gpustat['totalMemUsage'] = sumUsedMem/sumTotMem
            gpustats.append(gpustat)
    
    gpuJSON = []
    with open(os.path.join(R_PATH,'static/js/HostData.json'), 'r') as f:
        gpuJSON = json.load(f)
    
    gpuJSON.append({int(round(time.time()*1000)):gpustats})

    # only keep the last week data 
    if len(gpuJSON) > 10080:
        gpuJSON = gpuJSON[-10080:]

    with open(os.path.join(R_PATH,'static/js/HostData.json'), 'w') as f:
        json.dump(gpuJSON,f,indent=4,separators=(',',':'))