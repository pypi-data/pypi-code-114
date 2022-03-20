#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    reshapedata LLC
"""
import platform
from setuptools import setup
from setuptools import find_packages

setup(
    name = 'k3cloud_webapi_sdk',
    version = '3.0.3',
    install_requires=[
        'requests',
    ],
    packages=find_packages(),
    license = 'Apache License',
    author = 'hulilei',
    author_email = 'hulilei@takewiki.com.cn',
    url = 'http://www.reshapedata.com',
    description = 'erp web api in py language ',
    keywords = ['reshapedata', 'k3cloud_webapi_sdk'],
    python_requires='>=3.6',
)
