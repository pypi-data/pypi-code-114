
import pkg_resources as pkgr

from pyfred.fred_client import FredClient


try:
    __version__ = pkgr.get_distribution(__name__).version
except pkgr.DistributionNotFound as e:
    __version__ = 'dev'
