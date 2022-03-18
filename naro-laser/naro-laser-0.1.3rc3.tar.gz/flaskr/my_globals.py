# Copyright (c) 2021, 2022 Narotechnology, nash@narotechnology.com
# SPDX-License-Identifier: LicenseRef-Narotechnology-Proprietary

print('<-', __name__)

import socket

adc_time = [0]
adc_data = [0]
adc_time_diff = [0]
adc_data_mean = 0

hostname = socket.gethostname()

# max_log = 10

'''Be careful
설정치 파일로드를 한번 실행하면 이후 이 구조의 변경은 무시된다.
'from_file' 키를 변경하는 일은 다른 모듈에서 한다.
'''
cnfg = {
    'sample': {
        'period': 0.25 * 4 * 1,  # IMPORTANT! unit is ms
        'size': 4  # buffer size
    },
    'log': {
        'max': 10
    },
    'proc': {
        'method': 'MEAN'
    },
    'lte': {
        'dev_name': 'not defined',
        'baud_rate': 115200,
        'time_out': 1,
        'send_interval': 60 * 60,  # 1 hour
    },
    'sse': {
        'period': 0.5
    },
    'from_file': False,
}

status = {
    'sample': {
        'mode': None,  # 'Decimation',  # or Delay
        'decimation': None,
        'delay': None
    },
    'cpu_temp': 0.0,
    'thread': {
        'lte': False,
        'led': False,

    },
    'text': '==='
}

env = {
    'temp': 0,
    'humi': 0,
    'pres': 0,
    'alti': 0,
}

debug = {
    'err_count_lcd': 0
}

peri = {
    'adc': -1,  # -1 means 'not checked'
    'modem': -1,
    'lcd': -1,
    'led': -1,
    'bme280': -1,
    'dio_ext': -1,
    'button': -1
}

tele1_main = {
    'displacement': 0
}

tele2_env = {
    'temperature': 0,
    'humidity': 0,
    'pressure': 0,
    'cpu_temperature': 0
}

ipc = {  # interprocess comm., or socket
    'disp': 0,
    'temp': 0,
}

iot = {
    'wifi': {
        'server': 'http://mqtt.gleeze.com',
        'port': 9090,
        'protocol': 'http',
        'credential': None
    },
    'lteM1': {
        'server': 'http://mqtt.gleeze.com',
        'port': 'default',
        'protocol': 'mqtt',
        'user': 'forall'
    }
}
