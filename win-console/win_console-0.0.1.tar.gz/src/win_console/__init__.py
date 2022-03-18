from .exception import PlatfromNotSupportError
from sys import platform
if not platform.startswith('win'):
    raise PlatfromNotSupportError('This package JUST Support Running on Windows!')
from .core import stdout, stdin, backspace
from .utils import getpass
__all__ = [
    'stdout',
    'stdin',
    'backspace',
    'getpass'
]