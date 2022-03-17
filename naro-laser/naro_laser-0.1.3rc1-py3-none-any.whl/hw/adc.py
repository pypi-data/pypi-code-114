# Copyright (c) 2021, 2022 Narotechnology, nash@narotechnology.com
# SPDX-License-Identifier: LicenseRef-Narotechnology-Proprietary

import logging
import sys
import random
import time

from flaskr.hw.hw_base import HardwareBase

lg = logging.getLogger('hardware')
lg.propagate = 0
lg.info('=========================')
lg.info('importing adc')
lg.info('=========================')


# class SensorADC:
class SensorADC(HardwareBase):
    """My Class"""

    def __init__(self, add=0x48):
        super().__init__()
        """https://github.com/adafruit/Adafruit_CircuitPython_ADS1x15
        https://circuitpython.readthedocs.io/projects/ads1x15/en/latest/api.html
        """

        # time.sleep(2)
        self.attached = False
        self.data_adc = []
        self.data_time = []
        msg = 'init SensorADC start: ' + hex(add)
        lg.info(msg)
        # print(msg + '====================')

        if sys.platform == 'linux':
            from flaskr.hw import i2c
            import adafruit_ads1x15.ads1015 as ADS
            from adafruit_ads1x15.analog_in import AnalogIn

            if add in i2c.scan():
                self.ads = ADS.ADS1015(i2c, data_rate=3300, mode=ADS.Mode.CONTINUOUS, address=0x48)
                self.channel = AnalogIn(self.ads, ADS.P3)
                # self.channel = AnalogIn(self.ads, ADS.P0, ADS.P1)
                self.attached = True
                msg = '  found i2c device' + hex(add)
                lg.info(msg)
                # print(msg)
            else:
                msg = '  not found i2c device'
                lg.info(msg)
                # print(msg)
        else:
            msg = HardwareBase.msgNotSupportedOS
            lg.info(msg)
            # print(msg)

        # msg = 'init SensorADC end: ' + hex(add)
        # lg.info(msg)
        # print(msg)

    def read(self):
        if self.attached:
            return self.channel.value
        else:
            fake_data = random.randint(-200, -100)
            return fake_data

    # @staticmethod
    def hello(self):
        print('hello, from SensorADC')
        if self.attached:
            print('ADC attached')
        else:
            print('ADC not attached')


time.sleep(2)   # wait for... flask server
ad1 = SensorADC(add=0x48)
ad2 = SensorADC(add=0x49)

# lg.info('adc imported')
# lg.info(ad1.name)
