# from _libCombineArrays import ffi, lib
# @ffi.def_extern()
# ffi.cdef("int combine_arrays_v1( int *pz, double *pr, double *py, int n, int m);")

from _libCombineArrays import lib
from cffi import FFI
ffi = FFI()

def combine_arrays_v1( z, r, y, n, m):
    # Use CFFI type conversion
    pz = ffi.cast("int *", z.ctypes.data)
    pr = ffi.cast("double *", r.ctypes.data)
    py = ffi.cast("double *", y.ctypes.data)
    
    # Call C++ function
    result = lib.combine_arrays_v1( pz, pr, py, n, m)

    return result


def combine_arrays_v2( z, r, y, n, m):
    # Use CFFI type conversion
    pz = ffi.cast("int *", z.ctypes.data)
    pr = ffi.cast("double *", r.ctypes.data)
    py = ffi.cast("double *", y.ctypes.data)
    
    # Call C++ function
    result = lib.combine_arrays_v1( pz, pr, py, n, m)
    
    return result


def combine_arrays_v3( z, r, y, n, m):
    # Use CFFI type conversion
    pz = ffi.cast("int *", z.ctypes.data)
    pr = ffi.cast("double *", r.ctypes.data)
    py = ffi.cast("double *", y.ctypes.data)
    
    # Call C++ function
    result = lib.combine_arrays_v1( pz, pr, py, n, m)

    return result

