# implements a decentralized routines master 
# connects to worker pool
# broadcast heartbeat
# listen to commands


from distutils.log import Log
import os,time,json,boto3
from concurrent.futures import thread


from SharedData.Logger import Logger
logger = Logger(__file__)
from SharedData.SharedDataAWSKinesis import KinesisStreamConsumer,KinesisStreamProducer


stream_name='deepportfolio-workerpool'
profile_name='jcooloj'
username=os.environ['USERNAME']+'@'+os.environ['USERDOMAIN']

Logger.log.info('Starting master')
session = boto3.Session(profile_name=profile_name)
client = session.client('kinesis')

consumer = KinesisStreamConsumer(stream_name, profile_name)
producer = KinesisStreamProducer(stream_name, profile_name)

target='jcooloj@500010349783-NB'
target='jcooloj@TRADEBOT01-PC'
target='jcooloj@TRADEBOT02-PC'
target='jcooloj@TRADEBOT03-PC'
target='jcooloj@TRADEBOT04-PC'
target='jcooloj@TRADEBOT05-PC'
target='jcooloj@TRADEBOT06-PC'
target='jcooloj@TRADEBOT07-PC'
target='Administrator@IP-10-68-244-22'
target='ALL'


data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "ping",    
}
producer.produce(data,'command')

data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "pong",    
}
producer.produce(data,'command')

data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "status",    
}
producer.produce(data,'command')


GIT_TOKEN=os.environ['GIT_TOKEN']
GIT_ACRONYM=os.environ['GIT_ACRONYM']
data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "gitpwd",    
    "GIT_TOKEN" : GIT_TOKEN,
    "GIT_ACRONYM" : GIT_ACRONYM
}
producer.produce(data,'command')

data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "command",
    "command" : ['wmic','path','win32_VideoController',\
        'get','name,deviceID,Status'],
}
producer.produce(data,'command')


data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "command",
    "command" : ['wmic','memorychip','get','capacity,speed'],
}
producer.produce(data,'command')


data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "routine",
    "repo" : 'Backtest-RiskMetrics',
    "routine" : "calculate_moments_cpu.py"
}
producer.produce(data,'command')

data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "routine",
    "repo" : 'Backtest-RiskMetrics',
    "routine" : "realtimeprice.py"
}
producer.produce(data,'command')

data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "routine",
    "repo" : 'MarketData-Bloomberg',
    "routine" : "producer.py"
}
producer.produce(data,'command')

data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "routine",
    "repo" : 'MarketData-CSIData',
    "routine" : "csiez_download.py"
}
producer.produce(data,'command')

data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "routine",
    "repo" : 'MarketData-CSIData',
    "routine" : "sync_upload.py"
}
producer.produce(data,'command')

data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "routine",
    "repo" : 'MarketData-CSIData',
    "routine" : "download.py"
}
producer.produce(data,'command')

data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "routine",
    "repo" : 'MarketData-CSIData',
    "routine" : "load.py"
}
producer.produce(data,'command')

data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "routine",
    "repo" : 'MarketData-Bloomberg',
    "routine" : "producer.py"
}
producer.produce(data,'command')

data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "routine",
    "repo" : 'SharedData',
    "routine" : "tests\\test08_logconsumer.py"
}
producer.produce(data,'command')

data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "command",
    "command" : ["git","pull"]
}
producer.produce(data,'command')

data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "command",
    "command" : ['venv\\Scripts\\python.exe','-m',\
        'pip','install','-r','requirements.txt']
}
producer.produce(data,'command')


data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "command",
    "command" : ['venv\\Scripts\\python.exe','-m',\
        'pip','install','decentralizedroutines==0.0.4']
}
producer.produce(data,'command')


data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "command",
    "command" : ['shutdown','-f','-r']
}
producer.produce(data,'command')

data = {
    "sender" : "MASTER",
    "target" : target,
    "job" : "restart",
}
producer.produce(data,'command')

# response = client.delete_stream(
#     StreamName=stream_name
# )


