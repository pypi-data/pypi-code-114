import os

__version__ = "1.0.10"
from .pururin import get_pur
from .nhentai import get_nh
from .hentaifox import get_hfox
from .hentai2read import get_h2r
from .simplyh import get_sim
from .cli import *
from .utils.misc import choose