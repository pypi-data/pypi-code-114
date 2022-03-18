#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='yiwheel',
    version="0.1.11",
    description=(
        'yi wheel'
    ),
    long_description=open('README.rst', encoding='utf-8').read(),
    author='zy.liang',
    author_email='37013823@qq.com',
    maintainer='zy.liang',
    maintainer_email='37013823@qq.com',
    license='BSD License',
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    platforms=["all"],
    url='https://github.com/AniPython/yiwheel',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries'
    ],
)