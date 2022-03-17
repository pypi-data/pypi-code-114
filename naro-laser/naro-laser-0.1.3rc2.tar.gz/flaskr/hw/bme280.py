# Copyright (c) 2021, 2022 Narotechnology, nash@narotechnology.com
# SPDX-License-Identifier: LicenseRef-Narotechnology-Proprietary

import logging
import sys
import time
from flaskr.hw.hw_base import HardwareBase

lg = logging.getLogger('hardware')
lg.propagate = 0
lg.info('=========================')
lg.info('importing bme280')
lg.info('=========================')


class BME280(HardwareBase):
    """My Class"""
    def __init__(self):
        super().__init__()
        lg.info('init BME280 start')
        self.attached = False  # nash add, 여기까지는 윈도즈에서도 가능
        if sys.platform == 'linux':
            import qwiic_bme280
            from flaskr.hw import i2c
            if 0x77 in i2c.scan():
                self.mySensor = qwiic_bme280.QwiicBme280()

                if self.mySensor.connected:
                    lg.info(HardwareBase.msgDevConnected)
                    msg = 'addr: ' + hex(self.mySensor.address)
                    lg.info(msg)
                    # print(msg)

                    self.mySensor.begin()
                    self.attached = True
                    time.sleep(1)  # give a sec for system messages to complete
                else:
                    print('bme280 not found')

            else:
                lg.info(HardwareBase.msgDevNotAttached)
                self.attached = False
        else:
            lg.info(HardwareBase.msgNotSupportedOS)
            # lg.error('bme280 is only for linux')

        lg.info('init BME280 end')

    def sensor_test(self):
        if self.attached:
            print("Humidity:\t%.3f" % self.mySensor.humidity)
        else:
            msg = 'Not found BME280'
            print(msg)
            lg.error(msg)

    def measure_temp(self):
        if self.attached:
            ret = self.mySensor.temperature_celsius     # 21.1203, 라이브러리에 문제가 있다.
        else:
            ret = -36.5
        return ret

    def measure_humi(self):
        if self.attached:
            ret = self.mySensor.humidity
        else:
            ret = -55.5
        return ret

    def measure_pres(self):
        if self.attached:
            ret = self.mySensor.pressure
        else:
            ret = -1013
        return ret

    def measure_alti(self):
        if self.attached:
            ret = self.mySensor.altitude_meters
        else:
            ret = -2744
        return ret


bme280 = BME280()
# bme280.sensor_test()

