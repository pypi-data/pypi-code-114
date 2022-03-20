#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 22:32:38 2022

@author: wilfried
"""

from setuptools import setup

setup(
    include_package_data=True,
    package_data={
        'SOMptimised': ['examples/iris_dataset/*', 'README.md'],
    },
)