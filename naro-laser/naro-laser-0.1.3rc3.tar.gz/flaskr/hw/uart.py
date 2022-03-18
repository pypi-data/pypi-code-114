# Copyright (c) 2021, 2022 Narotechnology, nash@narotechnology.com
# SPDX-License-Identifier: LicenseRef-Narotechnology-Proprietary

import logging
import os
import sys
from flaskr.hw.hw_base import HardwareBase


lg = logging.getLogger('hardware')
lg.propagate = 0
lg.info('=========================')
lg.info('importing uart')
lg.info('=========================')


class UART(HardwareBase):
    """My Class"""

    def __init__(self):
        super().__init__()
        lg.info('init UART start')
        self.attached = False  # nash add, 여기까지는 윈도즈에서도 가능
        if sys.platform == 'linux':
            self.attached = True
        else:
            lg.error('UART is *currently* only for linux')

        lg.info('init UART end')

    def hello(self):
        print('hello, from UART')
        if self.attached:
            print('UART attached')
        else:
            print('UART not attached')


uart = UART()
