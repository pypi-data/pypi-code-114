from __future__ import print_function

import os
import sys
from warnings import warn

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
    name='fv3grid',
    version='1.0.1',
    url='https://github.com/noaa-oar-arl/fv3grid',
    license='MIT',
    include_package_data=True,
    package_data={'': ['fv3grid/*.nc']},
    author='Barry D. Baker',
    author_email='barry.baker@noaa.gov',
    maintainer='Barry D. Baker',
    maintainer_email='barry.baker@noaa.gov',
    packages=find_packages(),
    keywords=['fv3gfs'],
    description='FV3 Grid Data'
)
