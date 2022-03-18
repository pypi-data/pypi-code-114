"""
iMath Requests
====================================
Communication with the iMath data platform REST API
"""


try:
    from importlib import metadata
except ImportError:  # for Python<3.8
    import importlib_metadata as metadata
__version__ = metadata.version('imath_requests')
