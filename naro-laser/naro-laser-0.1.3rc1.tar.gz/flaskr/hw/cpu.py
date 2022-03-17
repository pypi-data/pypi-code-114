# Copyright (c) 2021, 2022 Narotechnology, nash@narotechnology.com
# SPDX-License-Identifier: LicenseRef-Narotechnology-Proprietary

import logging
import os
import sys
from flaskr.hw.hw_base import HardwareBase


lg = logging.getLogger('hardware')
lg.propagate = 0
lg.info('=========================')
lg.info('importing cpu')
lg.info('=========================')


class CPU(HardwareBase):
    """My Class"""

    def __init__(self):
        super().__init__()
        lg.info('init CPU start')
        self.attached = False  # nash add, 여기까지는 윈도즈에서도 가능
        if sys.platform == 'linux':
            self.attached = True
        else:
            lg.error('cpu is only for linux')

        lg.info('init CPU end')

    def get_cpu_temp(self):
        if self.attached:
            temp = os.popen("vcgencmd measure_temp").readline()
            temp = temp.replace('temp=', '')
            temp = temp.replace("'C", "")
            # print('replaced:', temp)
            return float(temp)
        else:
            return -273.1   # fake


cpu = CPU()
