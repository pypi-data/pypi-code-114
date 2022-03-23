#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: Jake Cui
# Mail: hbucqp1991@sina.cn
# Created Time:  2022-02-10 19:17:34
#############################################

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


requirements = [
    'numpy', 'pandas', 'setuptools'
]


setup(
    name="restidy",
    version="0.2.3",
    keywords=["pip", "wgs", "resfinder"],
    description="resfinder result tidy",
    long_description="Organize resfinder result to tabluar format",
    license="MIT Licence",
    url="https://github.com/hbucqp/restidy",
    author="Jake Cui",
    author_email="hbucqp1991@sina.cn",
    packages=find_packages(),
    # include_package_data=True,
    package_data={'': ['*.tsv']},
    platforms="any",
    install_requires=requirements,
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={
        'console_scripts': [
            'restidy=restidy.restidy:main',
        ],
    },
)
