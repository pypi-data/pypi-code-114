"""A simple IPyParallel based wrapper around IPython Kernel"""


from .kernel import IPyParallelKernel

from . import _version

__version__ = _version.get_versions()["version"]
