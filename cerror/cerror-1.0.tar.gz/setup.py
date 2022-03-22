from setuptools import setup
from cerror import __version__ # type: ignore[attr-defined]

setup(
    name='cerror',
    py_modules=['cerror'],
    version=__version__,
)