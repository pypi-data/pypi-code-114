""" Abies """
from pathlib import Path
from . import framework
from . import library
from . import builder
from . import templates
from . import cmake
from .cmake import get_cmake_dir

__version__ = "0.0.4.1"


def get_include_dirs() -> list[str]:
    """C++ headers."""
    framework_include = Path(__file__).parent / "framework" / "include"
    return [framework_include]


def get_source_dirs() -> str:
    """C++ libraries src dir"""


def get_rtl_include_dirs() -> str:
    """HDL headers"""


def get_rtl_module_dirs() -> str:
    """Directory containing all Abies library HDL modules"""


__all__ = ["get_cmake_dir"]
