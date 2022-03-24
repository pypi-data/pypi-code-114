"""An example magic"""
__version__ = '0.0.1'

from .df_jupyter_magic import DfMagics

def load_ipython_extension(ipython):
    ipython.register_magics(DfMagics)
