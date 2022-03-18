"""
Simple Documentation framework that takes all of the python docstrings and unwraps them into proper docs while supporting
example and template files
"""

from .DocsBuilder import *
from .DocWalker import *
from .Writers import *

__all__ = []
from .DocsBuilder import *; from .DocsBuilder import __all__ as exposed
__all__ += exposed
from .DocWalker import *; from .DocWalker import __all__ as exposed
__all__ += exposed
from .Writers import *; from .Writers import __all__ as exposed
__all__ += exposed
from .ExamplesParser import *; from .ExamplesParser import __all__ as exposed
__all__ += exposed