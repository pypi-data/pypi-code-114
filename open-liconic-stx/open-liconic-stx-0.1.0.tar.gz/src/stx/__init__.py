import sys

if sys.version_info[:2] < (3, 8):
    import importlib_metadata as metadata
else:
    from importlib import metadata

from .stx import Stx

__version__ = metadata.version("open-liconic-stx")

__all__ = ["__version__", "Stx"]
