#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='glitter_sdk',
    version='0.0.1',
    author='ted',
    author_email='ted@glitterprotocol.io',
    url='https://docs.glitterprotocol.io/',
    description=u'Glitter Protocol is a blockchain based database and index engine for developing and hosting web3 applications in decentralized storage networks.',
    packages=['glitter_sdk'],
    install_requires=['requests'],
    entry_points={}
)