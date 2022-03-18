# Copyright (c) 2021, 2022 Narotechnology, nash@narotechnology.com
# SPDX-License-Identifier: LicenseRef-Narotechnology-Proprietary

"""임포트 시 실행되어버리는 것을 방지하는게 나을 듯
그러나 당분간 이대로 두자 21.09
"""

import logging
import sys

lg = logging.getLogger('hardware')
lg.propagate = 0
lg.info('=========================')
lg.info('importing hw')
lg.info('=========================')

if sys.platform == 'linux':
    '''i2c bus instance creation'''
    import board
    import busio

    # Create the I2C bus
    # ADC 외에도 lcd 등에서도 사용되므로 반드시 여기에 있어야 한다
    i2c = busio.I2C(board.SCL, board.SDA, 400000) # ???

    lg.info('Linux system')
else:
    lg.error('** NOT ** Linux system')


