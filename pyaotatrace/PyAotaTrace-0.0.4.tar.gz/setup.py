#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

print('==> ', find_packages(where='./'))

setup(
    name='PyAotaTrace',
    version='0.0.4',
    description=(
        '使用Python读取Aota的Trace'
    ),
    long_description=open('README.md').read(),
    # long_description=open('./README.md').read(),
    author='Lizhenghao',
    author_email='zhenghao2021@iscas.ac.cn',
    maintainer='Lizhenghao',
    maintainer_email='zhenghao2021@iscas.ac.cn',
    license='MIT',
    packages=find_packages(where='./'),
    platforms=["Linux"],
    url='https://www.baidu.com',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
