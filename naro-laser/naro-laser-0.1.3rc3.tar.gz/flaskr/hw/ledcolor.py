# Copyright (c) 2021, 2022 Narotechnology, nash@narotechnology.com
# SPDX-License-Identifier: LicenseRef-Narotechnology-Proprietary

import logging
import os
import sys

from flaskr.hw.hw_base import HardwareBase


lg = logging.getLogger('hardware')
lg.propagate = 0
lg.info('=========================')
lg.info('importing ledcolor')
lg.info('=========================')


class LEDColor(HardwareBase):
    """My Class"""

    def __init__(self):
        super().__init__()
        lg.info('init LEDColor start')
        self.attached = False  # nash add, 여기까지는 윈도즈에서도 가능
        if sys.platform == 'linux':
            import board
            import neopixel

            self.pin_out = board.D21    # PWM
            self.pixels = neopixel.NeoPixel(self.pin_out, 1)
            self.pixels[0] = (5, 0, 0)
            self.pixels.show()

            self.attached = True
        else:
            lg.error('ledcolor is only for linux')

        lg.info('init LEDColor end')

    def hello(self):
        if self.attached:
            print('hello from ledcolor 1')
        else:
            print('hello from ledcolor 2')

    def color_red(self):
        print('RED  ', end='\r')  # use waitress, not flask!
        if self.attached:
            self.pixels[0] = (0, 5, 0)
            self.pixels.show()

    def color_green(self):
        print('GREEN ', end='\r')
        if self.attached:
            self.pixels[0] = (5, 0, 0)
            self.pixels.show()

    def color_blue(self):
        print('BLUE ', end='\r')
        if self.attached:
            self.pixels[0] = (0, 0, 5)
            self.pixels.show()


ledcolor = LEDColor()
