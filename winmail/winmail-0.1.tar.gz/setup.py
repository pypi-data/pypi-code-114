# -*- coding:utf-8 -*-

from setuptools import setup, find_packages
# from distutils.core import setup

setup(
    name='winmail',
    version='0.1',
    description='Winmail API',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Sway',
    author_email = 'sway_wang@foxmail.com',
    url='http://winmail.cn',
    py_modules=['winmail'],
    packages=find_packages()
)


