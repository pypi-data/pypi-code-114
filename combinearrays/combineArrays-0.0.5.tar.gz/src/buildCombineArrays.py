from cffi import FFI
import os

ffibuilder = FFI()
PATH = os.path.dirname(__file__)

ffibuilder.cdef("""
    int combine_arrays_v1( int *pz, double *pr, double *py, size_t n, size_t m);
    int combine_arrays_v2( int *pz, double *pr, double *py, size_t n, size_t m);
    int combine_arrays_v3( int *pz, double *pr, double *py, size_t n, size_t m);
    """, override=True)

ffibuilder.set_source("_libCombineArrays", r"""
    #include "libCombineArrays.h"
""",
    sources=[os.path.join(PATH, "libCombineArrays.cpp")],
    include_dirs=[PATH]
    )


if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
