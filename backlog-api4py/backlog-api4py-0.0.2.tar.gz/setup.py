#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup

from backlog import __author__, __license__, __title__, __version__

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name=__title__,
    version=__version__,
    author=__author__,
    maintainer=__author__,
    url="https://github.com/ryo8000/backlog-api4py",
    description="Backlog API for Python",
    long_description=readme,
    license=__license__,
    packages=[
        "backlog",
    ],
    python_requires=">=3.7.0",
    install_requires=[
        "requests>=2.0"
    ],
    classifiers=[
        "Topic :: Software Development",
        "Development Status :: 7 - Inactive",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Intended Audience :: Developers",
    ]
)
