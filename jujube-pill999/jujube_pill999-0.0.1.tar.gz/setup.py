#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='jujube_pill999',
    version='0.0.1',
    author='xlzd',
    author_email='wwwwu@gmail.com',
    url='https://zhuanlan.zhihu.com/p/26159930',
    description=u'吃枣药丸',
    packages=['pypi_test'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'jujube=jujube_pill:jujube',
            'pill=jujube_pill:pill'
        ]
    }
)