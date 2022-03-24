# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages

NAME = 'bulkrequests'
VERSION = '0.0.1rc1'

REQUIRES = [
    'requests >= 2.23.0',
    'dcacheclient',
    'urllib3',
    'alive-progress',
    'humanize'
]

setup(
    name=NAME,
    version=VERSION,
    description='a draft implementation of bulk requests in dCache',
    author='Dario Graña, Pau Tallada',
    author_email='dgrana@unc.edu.ar, tallada@pic.es',
    packages=find_packages(),
    install_requires=REQUIRES,
    include_package_data=True,
    entry_points={
        'console_scripts': ['bulkrequests=bulkrequests.cliclient:main']
        }
)
