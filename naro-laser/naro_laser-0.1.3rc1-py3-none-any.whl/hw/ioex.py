# Copyright (c) 2021, 2022 Narotechnology, nash@narotechnology.com
# SPDX-License-Identifier: LicenseRef-Narotechnology-Proprietary

import logging
import sys


if sys.platform == 'linux':
    from flaskr.hw import i2c
    import adafruit_ads1x15.ads1015 as ADS
    from adafruit_ads1x15.analog_in import AnalogIn


class SensorADC:
    """My Class"""
    def __init__(self, addr=0x48):
        """https://github.com/adafruit/Adafruit_CircuitPython_ADS1x15
        https://circuitpython.readthedocs.io/projects/ads1x15/en/latest/api.html
        https://github.com/adafruit/Adafruit_CircuitPython_MCP230xx
        """
        self.attached = False
        self.data_adc = []
        self.data_time = []
        logging.warning('init SensorADC start')
        if sys.platform == 'linux':
            if addr in i2c.scan():
                self.ads = ADS.ADS1015(i2c, data_rate=3300, mode=ADS.Mode.CONTINUOUS, address=0x48)
                self.channel = AnalogIn(self.ads, ADS.P3)
                # self.channel = AnalogIn(self.ads, ADS.P0, ADS.P1)
                self.attached = True
                logging.warning('Found i2c device' + hex(addr))
            else:
                logging.warning('Not found i2c device' + hex(addr))
        else:
            logging.warning('Only for linux')

        logging.warning('init SensorADC end')
