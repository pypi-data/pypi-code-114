# Copyright (c) 2021, 2022 Narotechnology, nash@narotechnology.com
# SPDX-License-Identifier: LicenseRef-Narotechnology-Proprietary

"""
`ModuleName`
====================================================

module for the ...

* Author(s): NaSeokhwan (2021)
"""

import sys
import logging
import socket
import threading
import time
import json
import statistics
import requests
import naro

print('<-', __name__)

from flaskr import my_globals as gm
from flaskr import shared

from flaskr import __about__
from flaskr.hw import adc
from flaskr.hw import lcd
from flaskr.hw import cpu
from flaskr.hw import uart
from flaskr.hw import bme280
from flaskr.hw import ledcolor as led

print(__about__.__title__, __about__.__version__, __about__.__build_date__)
print(__about__.__summary__)


def print2(*s):
    print(__name__, 'debug:', *s)


# # 외부 파일 참조
# if sys.platform == 'win32':
#     sys.path.append('e://bb//python//serial-com')
# elif sys.platform == 'linux':
#     sys.path.append('/home/pi/mnt/python/serial-com')
# from wdn400s import ModemMqtt

from flaskr.hw.wdn400s import ModemMqtt

# 기본 로거 설정
mylog = logging.getLogger('mylog')

# 주변장치 존재 여부
gm.peri['adc'] = adc.ad1.attached
gm.peri['lcd1'] = lcd.disp1.attached
gm.peri['bme280'] = bme280.bme280.attached

# ThingsBoard server sample: 'http://nash.wo.tc:9090/api/v1/RASPBERRY_PI_DEMO_TOKEN/telemetry'

things_cred = socket.gethostname().lower()  # 'RPI-LASER01'
url_path = '/api/v1/' + things_cred + '/telemetry'
things1 = gm.iot['wifi']['server'] + ':' + str(gm.iot['wifi']['port']) + url_path
print2(things1)


things_headers = {
    'Content-type': 'application/json',
}


def list_diff(lst):
    diff = []
    p_x = 0
    for x in lst:
        us = int((x - p_x) * 1000 * 1000)  # micro second
        diff.append(us)
        p_x = x
    diff[0] = 0
    return diff


# if True:
def create_threads():
    """create ny threads"""

    print(__name__, 'fun:create_threads() start')
    print(__name__, socket.gethostname() + ', ' + time.asctime())

    if True:    # config structure changed, 개발시, 첫 배치에는 항상 이걸로 하라.
        shared.config_from_to_file(cmd='save', cnfg=gm.cnfg)
    else:       # 배치 후 테스트 완료 후 이 모드를 사용해야 한다.
        config_from_to_file(cmd='load')
        gm.cnfg['from_file'] = True

    def th_func2(arg1):
        """ADC read 데이터를 다른 함수에서 사용가능하게 한다"""
        lg = logging.getLogger('th_func2')
        lg.propagate = 0
        lg.setLevel(logging.DEBUG)
        lg.critical('---')
        lg.info(time.asctime())
        lg.info(gm.cnfg)

        t1 = naro.Timer()
        t1.clear()

        cnt = 0
        while True:
            cnt += 1
            lst_time = []
            lst_data = []
            size = gm.cnfg['sample']['size']
            period = float(gm.cnfg['sample']['period']) / 1000  # ms -> second
            MIN_PERIOD_ADS = 1 / 3300  # for ADS1015. 0.303ms
            MIN_PERIOD = 1 / 4000
            decimation = int(period / MIN_PERIOD)
            assert decimation >= 1
            gm.status['sample']['decimation'] = decimation

            if cnt < gm.cnfg['log']['max']:
                lg.info(f'cnt: {cnt}, decimation: {decimation}')
                if period < MIN_PERIOD_ADS:
                    lg.info('sampling period setting is too low. 0.33ms will be used instead.')

            if period < 1.0 / 1000:  # high speed, Decimation, 모두 이걸로 테스트
                gm.status['sample']['mode'] = 'Decimation'
                gm.status['sample']['delay'] = None
                for j in range(size * decimation):
                    distance = adc.ad1.read()
                    now = time.time()
                    if j % decimation == 0:
                        lst_data.append(distance)
                        lst_time.append(now)
                        # print('adc capture: ', j, lst_data)
            elif period < 10.0 / 1000:  # mid speed, Delay
                gm.status['sample']['mode'] = 'Delay'
                gm.status['sample']['decimation'] = None
                gm.status['sample']['delay'] = period - 0.20 / 1000  # for mid speed
                for j in range(size):
                    '''대책없이 기다린다. 현재로는 이게 가장 낫다.'''
                    t1.delay_sec(gm.status['sample']['delay'])
                    distance = adc.ad1.read()
                    now = time.time()
                    lst_data.append(distance)
                    lst_time.append(now)
                pass
            else:  # low speed, 이 경우는 현재 없다
                assert period < 10.0 / 1000

                for j in range(size):
                    time.sleep(period)
                    distance = adc.ad1.read()
                    now = time.time()
                    lst_data.append(distance)
                    lst_time.append(now)
                pass

            # 데이터 필터링

            gm.adc_data_mean = statistics.mean(lst_data)
            lst_time_diff = list_diff(lst_time)

            # 로그 파일에 기록

            if cnt < gm.cnfg['log']['max']:
                lg.info(lst_time)
                lg.info(lst_time_diff)
                lg.info(lst_data)
                tmp = gm.adc_data_mean
                lg.info(f'adc data_mean: {tmp}')

            elif cnt == gm.cnfg['log']['max']:
                lg.info('log count reached max_log(fun2)')
            else:
                pass

            # 웹서버를 위한 데이터 복사 일단 no deep copy
            gm.adc_time = lst_time
            gm.adc_data = lst_data
            gm.adc_time_diff = lst_time_diff
            gm.ipc['disp'] = gm.adc_data_mean
            gm.ipc['temp'] = gm.env['temp']

            # ThingsBoard
            if cnt % 5 == 0:
                gm.tele1_main['displacement'] = gm.adc_data_mean
                data = json.dumps(gm.tele1_main)

                try:
                    response = requests.post(things1, headers=things_headers, data=data)
                except:
                    lg.error('network error(fun2), Thingsboard server')
                    pass

            time.sleep(0.2)  # 200ms:

    th = threading.Thread(target=th_func2, daemon=True, args=(1,))
    th.start()
    # th.join() # 세련된 방법
    '''위 두가지 모두 무한루프 쓰레드를 종료시키지 못하는 듯 21.08
    해결:
        데몬 설정이 먹힌다 그런데 start() 전에 설정하니 성공
    '''

    def th_fun3_100ms(arg1):
        cnt = 0
        while True:
            cnt += 1
            if cnt < gm.cnfg['log']['max']:
                pass
            elif cnt == gm.cnfg['log']['max']:
                pass
            else:
                pass
            time.sleep(0.1)
            pass

    th3 = threading.Thread(target=th_fun3_100ms, daemon=True, args=(2,))
    th3.start()

    def th_fun4_cpu_temp(arg1):
        cnt = 0
        while True:
            cnt += 1
            gm.status['cpu_temp'] = cpu.cpu.get_cpu_temp()
            time.sleep(2)

    th4 = threading.Thread(target=th_fun4_cpu_temp, daemon=True, args=(2,))
    th4.start()

    def th_fun5_lcd(arg1):
        time_fmt = '%m%d,%H:%M:%S'
        s22 = time.strftime(time_fmt, time.localtime(time.time()))
        lcd.disp1.set_cursor(0, 0)
        lcd.disp1.print(s22)

        cnt = 0
        while True:
            cnt += 1
            lcd.disp1.set_cursor(0, 16 * 1)
            lcd.disp1.print(f'[{cnt}]')
            time.sleep(1.0)

    th5 = threading.Thread(target=th_fun5_lcd, daemon=True, args=(2,))
    th5.start()

    def th_fun6_serial(arg1):
        cnt = 0
        while True:
            cnt += 1
            time.sleep(0.5)
            pass

    th6 = threading.Thread(target=th_fun6_serial, daemon=True, args=(2,))
    th6.start()

    def th_fun7_bme280(arg1):
        """environment sensor

        온/습도, 기압, 고도
        """
        time.sleep(2)
        cnt = 0
        while True:
            gm.env['temp'] = bme280.bme280.measure_temp()  # Rpi OS 21.10 에서는 라이브러리 버그,
            gm.env['humi'] = bme280.bme280.measure_humi()
            gm.env['pres'] = bme280.bme280.measure_pres()
            gm.env['alti'] = bme280.bme280.measure_alti()

            gm.tele2_env['temperature'] = gm.env['temp']
            gm.tele2_env['humidity'] = gm.env['humi']
            gm.tele2_env['pressure'] = gm.env['pres']
            gm.tele2_env['cpu_temperature'] = gm.status['cpu_temp']

            cnt += 1
            time.sleep(1)
            pass

    th7 = threading.Thread(target=th_fun7_bme280, daemon=True, args=(2,))
    th7.start()

    def th_fun8_iot_server(arg1):
        """publish to MQTT Broker

        모뎀을 사용하지 않는 인터넷 연결만 사용
        측정 데이터 및 환경데이터도 전송한다

        """
        cnt = 0
        while True:
            data = json.dumps(gm.tele2_env)
            try:
                response = requests.post(things1, headers=things_headers, data=data)
            except:
                mylog.error('things1 request fail')

            cnt += 1
            time.sleep(2)

    th8 = threading.Thread(target=th_fun8_iot_server, daemon=True, args=(2,))
    th8.start()

    def th_fun9(arg1):
        """change neopixel led color

        이것 때문에 sudo 실행해야 한다
        """

        gm.status['thread']['led'] = True

        cnt = 0
        while True:
            if cnt % 3 == 0:
                led.ledcolor.color_green()
            elif cnt % 3 == 1:
                led.ledcolor.color_red()
            else:
                led.ledcolor.color_blue()

            cnt += 1
            time.sleep(1)

    th9 = threading.Thread(target=th_fun9, daemon=True, args=(2,))
    th9.start()

    def th_fun12(arg1):
        """lte-m1 modem mqtt

        mqtt server: mqtt.gleeze.com (my server)
        device name for mqtt server: 'forall'
        client name: hostname+wdn400s

        당분간 서버측에는 하나의 디바이스만 생성하고 공동으로 사용한다

        """

        def debug(*s):
            if True:
                print(__name__, 'lte', *s)

        gm.status['thread']['lte'] = True

        # dev1 = '/dev/ttyUSB0'
        # dev1 = 'COM16'
        if sys.platform == 'win32':
            dev1 = 'COM16'
        elif sys.platform == 'linux':
            dev1 = '/dev/ttyUSB1'
        elif sys.platform == 'cygwin':
            pass
        else:
            pass

        baud_rate = gm.cnfg['lte']['baud_rate']     # 115200  # 19200 # 9600
        time_out = gm.cnfg['lte']['time_out']

        time.sleep(2)
        debug('modem opening...')
        modem = ModemMqtt()  # dev1, baudrate=baud_rate, timeout=time_out)
        debug('config...')
        # server = 'mqtt.gleeze.com'
        # mqtt_user = 'forall'
        at_cmds_conf = [
            'AT*WMQTCFG=endpoint,' + gm.iot['lteM1']['server'],
            'AT*WMQTCFG=username,' + gm.iot['lteM1']['user']
        ]
        debug(at_cmds_conf)

        modem.at_config(at_cmds_conf, wait=0.5)  # 모뎀 부팅 후 한번만
        s1 = '''AT*WMQTPUB='''
        s2 = '''v1/devices/me/telemetry,'''

        cnt = 0
        while True:
            cnt += 1
            debug('connecting...')
            modem.at_connect()  # 전송 전

            dic1 = {'value': cnt, 'host': gm.hostname + '-wdn400s'}
            s3 = '\"' + str(dic1) + '\"'
            cmd = s1 + s2 + s3
            debug(cmd)

            debug('sending...')
            modem.at_mqtt_pub(cmd)

            debug('disconnecting...')
            modem.at_disconnect()  # 전송 후

            # modem.close()  # 프로그램 완전 종료 시에만 호출하라

            if cnt < 2:  # 처음에만 자주 전송한다.
                time.sleep(10)
            elif cnt == 2:
                debug('next time, lte send_interval will be change to:', gm.cnfg['lte']['send_interval'])
            else:
                time.sleep(gm.cnfg['lte']['send_interval'])

    th12 = threading.Thread(target=th_fun12, daemon=True, args=(2,))
    th12.start()

