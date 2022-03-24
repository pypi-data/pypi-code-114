"""Command line program and Python library for particle tracking velocimetry."""

import warnings

try:
    from ._version import version as __version__
except ImportError:
    warnings.warn(
        "couldn't import _version.py, if this is a development setup run "
        "'pip install -e .[dev]' to create this file"
    )
    __version__ = "0.0.0"


class PtvPyError(Exception):
    """Base for errors specific to PtvPy.

    Parameters
    ----------
    message : str
        A message describing the cause of the error.
    hint : str, optional
        A helpful hint on what to do about the error.
    """

    def __init__(self, message: str, hint: str = None):
        self.message = message
        self.hint = hint
        super().__init__(message, hint)

    def __str__(self):
        return self.message
