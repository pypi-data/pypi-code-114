#!/usr/bin/env python
from setuptools import setup, find_packages
from distutils.core import setup

setup(name='dswmagic',
      classifiers=[
          'Programming Language :: Python :: 3.5',
      ],
      install_requires=['odps>=0.11.0'],
      version='1.0',
      description='dsw ipython magic command',
      author='xibai',
      packages=find_packages()
      )
