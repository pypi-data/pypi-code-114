from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from .tables import *
from .async_utils import check_files_exist
