#!/usr/bin/env python
import os

from setuptools import setup

setup(
    install_requires=[open("requirements.txt").read().strip().split("\n")],
)
