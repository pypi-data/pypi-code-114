from pybrary.main import parse_argv

from pybrary import *

_, f, a, k = parse_argv()
globals()[f](*a, **k)
