"""An example magic"""
__version__ = '0.0.1'

from .df_magic_openSARlab import DfMagics

def load_ipython_extension(ipython):
    ipython.register_magics(DfMagics)
