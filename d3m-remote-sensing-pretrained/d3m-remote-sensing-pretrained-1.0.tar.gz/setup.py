#!/usr/bin/env/python

from setuptools import setup, find_packages

VERSION = '1.0'

setup(
    name='d3m-remote-sensing-pretrained',
    author='Ben Johnson',
    author_email='ben@canfield.io',
    classifiers=[],
    description='Pretrained remote sensing models',
    keywords=['remote sensing', 'pretrained', 'rs'],
    url='https://gitlab.com/datadrivendiscovery/contrib/remote_sensing_pretrained',
    license='MIT',
    packages=find_packages(),
    version=VERSION
)
