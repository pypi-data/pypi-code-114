# Copyright (c) 2021, 2022 Narotechnology, nash@narotechnology.com
# SPDX-License-Identifier: LicenseRef-Narotechnology-Proprietary

class HardwareBase:
    name = 'HardwareBase Class'
    msgNotSupportedOS = '**Not** Supported OS'
    msgDevNotAttached = 'Device **Not** Attached'
    msgDevConnected = 'Device Connected, OK'

    def __init__(self):
        self.name = 'HardwareBase instance'

    @classmethod
    def hello(cls):
        return cls.name

    @classmethod
    def hello_pr(cls):
        print(cls.name)

    @classmethod
    def hw(cls):
        print(cls.name)

