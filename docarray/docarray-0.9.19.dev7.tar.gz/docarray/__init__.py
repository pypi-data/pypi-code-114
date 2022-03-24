__version__ = '0.9.19.dev7'

import os

from .document import Document
from .array import DocumentArray

if 'DA_NO_RICH_HANDLER' not in os.environ:
    from rich.traceback import install

    install()
