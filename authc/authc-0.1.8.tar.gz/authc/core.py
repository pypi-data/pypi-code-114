import json
import platform
import subprocess
import sys
import threading
import time
from typing import Dict

import codefast as cf
from codefast.patterns.singleton import SingletonMeta


class Bins(object):
    LINUX: str = 'linux'
    MACOS: str = 'mac'
    M1: str = 'm1'


class Authentication(metaclass=SingletonMeta):
    """ Authentication with binary.
    """

    def __init__(self) -> None:
        self._bin_path = "/tmp/authc"
        self._info = {}

    @property
    def bin_path(self):
        if not cf.io.exists(self._bin_path):
            _platform = platform.platform().lower()
            import os
            _path = os.path.join(cf.io.dirname(), 'data')
            if 'linux' in _platform:
                _path = os.path.join(_path, Bins.LINUX)
            elif 'macos' in _platform and 'x86_64' in _platform:
                _path = os.path.join(_path, Bins.MACOS)
            else:
                _path = os.path.join(_path, Bins.M1)

            cf.info('coping {} to {}'.format(_path, self._bin_path))
            cf.io.copy(_path, self._bin_path)
            subprocess.call(['chmod', '755', self._bin_path])
        return self._bin_path

    @property
    def info(self):
        if not self._info:
            self._info = self._query_accounts()
        return self._info

    def _query_accounts(self) -> Dict[str, str]:
        stdout: str = ''
        _accounts = {}
        try:
            cmd = self.bin_path + ' -a'
            stdout = cf.shell(cmd)
            _accounts = json.loads(stdout)
            _accounts = dict(sorted([(k, v) for k, v in _accounts.items()]))
        except json.decoder.JSONDecodeError as e:
            cf.error('failed to decode json {}, {}'.format(stdout, e))
        except Exception as e:
            cf.error('failed to query secrets: {}'.format(e))
        finally:
            return _accounts

    def register(self):
        cmd = self.bin_path + ' -r'
        try:
            print(cf.shell(cmd))
        except subprocess.CalledProcessError as e:
            pass

    def update(self):
        cmd = self.bin_path + ' -u'
        try:
            cf.shell(cmd)
        except subprocess.CalledProcessError as e:
            pass


def authc() -> Dict[str, str]:
    if len(sys.argv) > 1 and sys.argv[1] == '-r':
        cf.info('registering...')
        Authentication().register()
        cf.info('register complete')
    else:
        return Authentication().info


def gunload(key: str) -> str:
    return authc().get(key, '')
