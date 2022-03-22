#!/usr/bin/env python
# -*- coding: utf-8; buffer-read-only: t -*-

"""
Setup for CEMI Data Science Tollbox
"""

import os
import sys

from setuptools import find_packages, setup

def read(rel_path):
    """ Docstring """
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    """ Docstring """
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")

try:
    with open("README.md", "r") as fh:
        LONG_DESCRIPTION = fh.read()
except Exception:
    LONG_DESCRIPTION = ''

# Platform specific code
if sys.platform.startswith('win'):
    PYTHON_REQUIRES = '<3.7'
elif sys.platform.startswith('linux'):
    PYTHON_REQUIRES = '<=3.10'

setup(
    name="cemids",
    version=get_version("cemids/__init__.py"),
    description="This package provides a Python Toolbox with a set of functions to assist in the management of the CEMI Data Science project",
    long_description = LONG_DESCRIPTION,
    long_description_content_type="text/markdown",

    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/goyoambrosio/cemids",
    keywords=('data science '
              'public administration '
              ),

    author="G. Ambrosio-Cestero",
    author_email="gambrosio@malaga.eu",
    platforms=['Windows', 'Linux'],

    packages=find_packages(),

    install_requires=[
        "loguru",
        "pandas"
    ],
    extras_require={
        'full':['matplotlib>=3', 'jupyter'],
        'interactive': ['matplotlib>=3', 'jupyter']
    },
    python_requires=PYTHON_REQUIRES,

    tests_require=['unittest'],
    # These files will be located at ~/<anaconda-dir>/envs/<env-name>/[cemids/<dir>|...]
    data_files=[
    ],
    # sql files from cemids package will be included in the installation package
    # located at ~/<anaconda-dir>/envs/<env-name>/lib/<python>/site-packages/cemids
    package_data={'cemids': ['*.sql']},

)
