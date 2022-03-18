from ctypes import *
import os
psdr_cuda = cdll.LoadLibrary(os.path.dirname(__file__)+"/psdr_cuda.cp38-win_amd64.pyd")

