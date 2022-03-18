import importlib.metadata

from pint import UnitRegistry

from .data import IVESPA, Aubry, Mastin, Sparks
from .gp import GP_example
from .stats import QHstats

ureg = UnitRegistry()

__version__ = importlib.metadata.version("qhbayes")
