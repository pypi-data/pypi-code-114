#!/usr/bin/env python
# Licensed under a 3-clause BSD style license - see LICENSE.rst
# adapted from https://github.com/astropy/astropy
# Note: This file needs to be Python 2 / <3.6 compatible, so that the nice
# "This package only supports Python 3.x+" error prints without syntax errors etc.


'''
Note: if you get an error:

> error: [Errno 2] Could not find C/C++ file pycraf/pathprof/cyprop.(c/cpp)
> for Cython file pycraf/pathprof/cyprop.pyx when building extension
> pycraf.pathprof.cyprop. Cython must be installed to build from a git
> checkout.: 'pycraf/pathprof/cyprop.c'

Delete the file "pycraf/cython_version.py"

'''

import sys


TEST_HELP = """
Note: running tests is no longer done using 'python setup.py test'. Instead
you will need to run:
    tox -e test
If you don't already have tox installed, you can install it with:
    pip install tox
If you only want to run part of the test suite, you can also use pytest
directly with::
    pip install -e .[test]
    pytest --pyargs pycraf_gui --dogui
    # or individual tests:
    pytest --pyargs pycraf_gui --dogui -k <test_func_name/module_name/etc.>

For more information, see:
  https://docs.astropy.org/en/latest/development/testguide.html#running-tests
"""

if 'test' in sys.argv:
    print(TEST_HELP)
    sys.exit(1)


# Only import these if the above checks are okay
# to avoid masking the real problem with import error.
from setuptools import setup  # noqa


setup()
