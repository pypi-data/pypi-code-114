# coding=utf-8

from . import dsw_odps
from odps.ipython import load_ipython_extension as odps_load


def load_ipython_extension(ip):
    odps_load(ip)
    print('xx')
    for mod in (dsw_odps, ):
        if hasattr(mod, 'load_ipython_extension'):
            mod.load_ipython_extension(ip)
