# Copyright (c) 2021, 2022 Narotechnology, nash@narotechnology.com
# SPDX-License-Identifier: LicenseRef-Narotechnology-Proprietary

"""
`wdn400s`
====================================================

module for the LTE-M1 comm.

* Author(s): NaSeokhwan (2021)
"""

import time
import serial
import serial.tools.list_ports


def print2(*s):
    if True:
        print(*s)


def print3(*s):
    if True:
        print2(*s)


class WDN400S:
    """WD-N400S Modem"""
    def __init__(self):
        print(__name__, 'init modem instance...')

        url = self.find_modem_wdn400s()

        if url:
            self.ser = serial.serial_for_url(url=url, baudrate=115200, timeout=1)
            self.attached = True
        else:
            print('** modem not attached')
            self.attached = False

    def find_modem_wdn400s(self):
        """find WD-N400S LTE M1 modem"""
        ports = serial.tools.list_ports.comports(include_links=not True)
        for p in ports:
            print(p.device, p.description)

            if 'CP2105' in p.description:
                if '/dev/ttyUSB1' in p.device:  # raspberry
                    print('- target modem found:', p.device)
                    return p.device
                if 'Standard' in p.description:  # win 10
                    print('- target modem found:', p.device)
                    return p.device
        return False

    def close(self):
        if self.attached:
            self.ser.close()

    def readable(self):
        if self.attached:
            return self.ser.readable()

    def read_all(self):
        if self.attached:
            return self.ser.read_all()

    def write(self, cmd_bytes):
        if self.attached:
            self.ser.write(cmd_bytes)

    def write_str_cr(self, cmd_str):
        if self.attached:
            self.ser.write((cmd_str+'\r').encode('utf-8'))

    def write_read(self, cmd, wait, err_str='xxx', ok_str='xxx'):
        if not self.attached:
            return
        print2('W:', cmd)
        self.write_str_cr(cmd)
        time.sleep(wait)
        b1 = self.read_all()
        print2('R:', b1)
        if err_str.encode('utf-8') in b1:
            print3('  --not ok')
        else:
            if ok_str.encode('utf-8') in b1:
                print3('  --ok')
            else:
                print3('  --not ok')

    def at_config(self, at_cmds, wait):
        for cmd in at_cmds:
            self.write_read(cmd, wait, ok_str='OK')


class ModemMqtt(WDN400S):
    def at_connect(self):
        cmd = 'AT*WMQTCON'
        super().write_read(cmd, 2.0, ok_str='WMQTCON:2')

    def at_disconnect(self):
        cmd = 'AT*WMQTDIS'
        super().write_read(cmd, 2.0, ok_str='WMQTDIS:0')

    def at_mqtt_pub(self, cmd,):
        super().write_read(cmd, 0.2, err_str='WMQTPUB:NC', ok_str='WMQTPUB:')


class ModemTcp(WDN400S):
    def at_connect(self):
        cmd = 'AT+WSOCO=0'
        super().write_read(cmd, 0.5, ok_str='OPEN_CMPL')
        # 'WSOCO:0' 로는 감지 불가, 중복

    def at_disconnect(self):
        cmd = 'AT+WSOCL=0'
        super().write_read(cmd, 0.5, ok_str='CLOSE_CMPL')

    def at_tcp_send(self, cmd):
        super().write_read(cmd, 0.1, ok_str='WSOWR:1')


class ModemHttp(WDN400S):
    def at_connect(self):
        cmd = 'AT*WHTTP=3'  # 페이지 로드, 많은 데이터, 사용 주의
        super().write_read(cmd, 10, ok_str='WHTTPR:COMPLETED')

    # def at_disconnect(self):
    #     cmd = 'AT+?WSOCL=0'
    #     super().write_read(cmd, 0.1, ok_str='?CLOSE_CMPL')

    def at_http_send(self, cmd):
        super().write_read(cmd, 0.1)


def demo_wo_class():
    """demo without class"""
    ser = serial.serial_for_url('COM16', baudrate=115200, timeout=1)

    at_cmds = [b'ati\r',
               b'AT*WMQTCFG=endpoint,nash.mywire.org\r']

    for cmd in at_cmds:
        print('-----')
        ser.write(cmd)
        time.sleep(1)
        if ser.readable():
            b1 = ser.read_all()
            print('-- read bytes:')
            print(b1)
            print('-- convert to string:')
            s1 = b1.decode('utf-8')
            # s1 = b1.decode('ascii')
            print(s1)   # pycharm, run 창에서는 보이지 않는 버그 발견.
                        # 반드시 실행창에서 실행하라.

            # s2 = s1.replace('\r', '').split('\n')
            # for line in s23:
            #     print(line)

            print('---')
        else:
            print('not readable')

    ser.close()


def demo_class():
    print('modem opening...')
    # modem = ModemMqtt('COM16', baudrate=115200, timeout=1)
    modem = ModemMqtt()
    print('config...')
    at_cmds = [
        'AT*WMQTCFG=endpoint,mqtt.gleeze.com',
        'AT*WMQTCFG=username,forall'
    ]
    modem.at_config(at_cmds, wait=0.5)  # 모뎀 부팅 후 한번만


if __name__ == '__main__':
    demo_wo_class()
    demo_class()

