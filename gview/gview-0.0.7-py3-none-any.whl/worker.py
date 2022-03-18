from .app_celery_init import make_celery
from .app import app
from gpustat import GPUStatCollection
from urllib.request import urlopen
from .G_VAR import R_PATH
import os
import json

# initialize celery
celery = make_celery(app)

# util functions to load host info & self-gpu-data
def load_self_gpustat():
    my_gpustat = GPUStatCollection.new_query().jsonify()
    return my_gpustat

def load_hosts():
    hosts = {}
    with open( os.path.join(R_PATH, 'Hosts.txt') ) as file:
        for line in file:
            name, url = line.strip().split('   ')
            hosts[name] = url
        file.close()
    return hosts

# celery tasks
@celery.task()
def load_gpustat_by_host(hostname):
    hosts = load_hosts()
    hosturl = hosts[hostname]
    
    try:
        resp = urlopen(hosturl + '/gpustat', timeout=10)
    except Exception as e:
        print(hosturl + ' timeout')

    hoststat = {}

    rawresp = json.loads(resp.read())
    hoststat['url'] = hosturl.replace('http://','').replace(':9999','')
    hoststat['hostname'] = hostname

    if 'error' in rawresp:
        hoststat['error'] = rawresp['error']
    else:
        hoststat['error'] = 'null'
        hoststat['gpus'] = rawresp['gpus']
        for gpu in hoststat['gpus']:
            gpu['memoryUsage'] = gpu['memory.used']/gpu['memory.total'] * 100

    return {'result': hoststat}

@celery.task(bind=True)
def load_gpustats(self):
    count = 0

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
                'url': hosts[name].replace('http://','').replace(':9999','')
            })
            continue

        rawresp = json.loads(resp.read())
        resp.close()

        gpustat['hostname'] = name
        gpustat['connection'] = 'True'
        gpustat['url'] = hosts[name].replace('http://','').replace(':9999','')

        if 'error' in rawresp:
            gpustat['error'] = rawresp['error']
        else: 
            gpustat['error'] = 'null'
            gpustat['gpus'] = rawresp['gpus']
            for gpu in gpustat['gpus']:
                gpu['memoryUsage'] = gpu['memory.used']/gpu['memory.total'] * 100

        gpustats.append(gpustat)

        count += 1
        self.update_state(state = "LOADING", meta={'progress':count,'total':len(hosts),'status':'Loading ...','result':gpustats})
        
    return {'progress':8,'total':len(hosts),'status':'Complete','result':gpustats}