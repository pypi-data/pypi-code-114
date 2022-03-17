# Copyright (c) 2021, 2022 Narotechnology, nash@narotechnology.com
# SPDX-License-Identifier: LicenseRef-Narotechnology-Proprietary

import logging
import sys
import time

import qwiic_serlcd
import qwiic_micro_oled
import qwiic_oled_display

from flaskr.hw.hw_base import HardwareBase

lg = logging.getLogger('hardware')
lg.propagate = 0
lg.info('=========================')
lg.info('importing lcd')
lg.info('=========================')


class OLED1(HardwareBase):
    """128x48(?)"""
    def __init__(self):
        super().__init__()
        lg.info('init class OLED')
        self.attached = False  # nash add, 여기까지는 윈도즈에서도 가능
        if sys.platform == 'linux':
            if False:
                try:
                    lg.info('finding OLED...(try..except)')
                    print('=== trying...')
                    self._myDisp = qwiic_oled_display.QwiicOledDisplay()
                    # self._myDisp = qwiic_micro_oled.QwiicMicroOled()
                    print('===', self._myDisp.connected)
                except:
                    lg.info(HardwareBase.msgDevNotAttached)
                    print('Not found display')

            self._myDisp = qwiic_oled_display.QwiicOledDisplay()
            # print('self._myDisp connected=', self._myDisp.connected)

            if self._myDisp.connected:
                self._myDisp.begin()
                self._myDisp.clear(self._myDisp.ALL)
                self._myDisp.clear(self._myDisp.PAGE)
                self._myDisp.set_font_type(1)

                self.attached = True
                lg.info(HardwareBase.msgDevConnected)
            else:
                self.attached = False
                lg.info(HardwareBase.msgDevNotAttached)
        else:
            lg.info(HardwareBase.msgNotSupportedOS)

    def print(self, s):
        if self.attached:
            self._myDisp.print(s)
            self._myDisp.display()

    def set_cursor(self, col, row):
        if self.attached:
            self._myDisp.set_cursor(col, row)

    def clear(self):
        if self.attached:
            self._myDisp.clear(self._myDisp.ALL)
            # self._myDisp.clear(self._myDisp.PAGE)


disp1 = OLED1()

disp1.print('Disp1')
time.sleep(1)
disp1.clear()
