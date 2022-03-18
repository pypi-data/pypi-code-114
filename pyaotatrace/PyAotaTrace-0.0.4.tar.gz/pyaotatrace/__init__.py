import sys
import platform
from .types import *
from .cfunc import *
from .wrapper import *

def EnvCheck():
    assert platform.system() == "Linux"
    assert platform.architecture()[0] == '64bit'
    assert platform.architecture()[1] == 'ELF'
    assert sys.version > '3.6'

try:
    EnvCheck()
except Exception as e:
    raise EnvironmentError("该包需要在 Python 3.6 版本以上的 Linux 系统中运行")
