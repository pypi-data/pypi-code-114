from importlib.metadata import version, PackageNotFoundError
try:
    __version__ = version("natorbs")
except PackageNotFoundError:
    # package is not installed
    pass

from natorbs.moldata import read_molecule
from natorbs.natural import NaturalOrbitals
from natorbs.diff import FragmentMullikenAnalysis, NOCV, DiffDensOrbitals
from natorbs.mulliken import mulliken_contribs
from natorbs.mutual_overlaps import mutual_overlaps
