#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages

setup(
    name='test0017',
    version='2.0',
    author='Tector Pro',
    description='Testing something',
    packages=find_packages(),
    classifiers = [
  	'Development Status :: 5 - Production/Stable',
  	'Intended Audience :: Education',
  	'Operating System :: Microsoft :: Windows :: Windows 10',
  	'License :: OSI Approved :: MIT License',
  	'Programming Language :: Python :: 3'],
    install_requires=[
        'Abhi-pdf==7.3',
    ]
)
