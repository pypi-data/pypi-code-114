"""
Infrastructure for automatically running sciagraph based on an environment
variable.
"""

import os
import sys
import logging


def _check():
    value = os.environ.pop("SCIAGRAPH_MODE", None)
    if value is None:
        return
    if value != "process":
        logging.error(
            "The SCIAGRAPH_MODE environment variable only supports the value"
            f" 'process', but you set it to {value!r}, exiting."
        )
        os._exit(1)

    import ctypes

    # TODO: Python 3.10 and later have sys.orig_argv.
    _argv = ctypes.POINTER(ctypes.c_wchar_p)()
    _argc = ctypes.c_int()
    ctypes.pythonapi.Py_GetArgcArgv(ctypes.byref(_argc), ctypes.byref(_argv))
    argv = _argv[: _argc.value]
    args = ["python", "-m", "sciagraph", "run"] + argv[1:]

    os.execv(sys.executable, args)


_check()
