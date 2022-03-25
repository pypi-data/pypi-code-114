# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------

# This file can be modified by setup.py when building a manylinux2010 wheel
# When modified, it will preload some libraries needed for the python C extension
from ctypes import CDLL, RTLD_GLOBAL
try:
    _libcublas = CDLL("libcublas.so.10", mode=RTLD_GLOBAL)
    _libcudnn = CDLL("libcudnn.so.7", mode=RTLD_GLOBAL)
    _libcurand = CDLL("libcurand.so.10", mode=RTLD_GLOBAL)
    _libcufft = CDLL("libcufft.so.10", mode=RTLD_GLOBAL)
    _libcudart = CDLL("libcudart.so.10.2", mode=RTLD_GLOBAL)
except OSError:
    import os
    os.environ["ORT_CUDA_UNAVAILABLE"] = "1"
