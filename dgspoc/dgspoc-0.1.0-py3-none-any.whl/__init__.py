"""Top-level module for describe-get-system proof of concept.

- allow end-user to describe his or her requirement to build test script.
"""

from dgspoc.core import Dgs
from dgspoc.config import version

__version__ = version

__all__ = [
    'Dgs',
    'version',
]