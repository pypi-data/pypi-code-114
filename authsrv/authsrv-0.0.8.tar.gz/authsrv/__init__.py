'''
Wrapper around authsrv utilities from https://github.com/unixtools/authsrv
'''

import subprocess
from subprocess import PIPE

import getpass

__author__ = 'Nathan Neulinger'
__url__ = 'https://github.com/unixtools/authsrv-python'
__version__ = '0.0.8'


def fetch(owner: str = None, user='', instance='') -> str:
    '''Retrieve a stash from authsrv'''

    if owner is None:
        owner = getpass.getuser()

    if user == '' or instance == '':
        return None

    try:
        password = subprocess.check_output(["authsrv-decrypt", owner, user, instance], stderr=PIPE)
        password = password.decode('utf-8')
        password = password.rstrip('\n\r')
    except subprocess.CalledProcessError:
        password = None

    return password
