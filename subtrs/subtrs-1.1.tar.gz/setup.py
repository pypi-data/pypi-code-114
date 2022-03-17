#!/usr/bin/python3
# -*- coding: utf-8 -*-

# setup.py file is part of subtrs.

# Copyright 2022 Dimitris Zlatanidis <d.zlatanidis@gmail.com>
# All rights reserved.

# subtrs is a simple tool that translates video subtitles

# https://gitlab.com/dslackw/subtrs

# subtrs is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


from setuptools import setup

INSTALLATION_REQUIREMENTS = ['googletrans==3.1.0a0', 'colored>=1.4.3']
DOCS_REQUIREMENTS = []
OPTIONAL_REQUIREMENTS = []


setup(
    name='subtrs',
    packages=['subtrs'],
    scripts=['bin/subtrs'],
    version='1.1',
    description='A simple tool that translates video subtitles',
    long_description=open('README.rst').read(),
    keywords=['video', 'translate', 'subtitles', 'google'],
    author='Dimitris Zlatanidis',
    author_email='d.zlatanidis@gmail.com',
    package_data={'': ['README.rst', 'CHANGES.md']},
    data_files=[],
    url='https://gitlab.com/dslackw/subtrs',
    install_requires=INSTALLATION_REQUIREMENTS,
    extras_require={
        'optional': OPTIONAL_REQUIREMENTS,
        'docs': DOCS_REQUIREMENTS,
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.9',
        'Topic :: Text Processing',
        'Topic :: Terminals',
        ],
    python_requires='>=3.9'
)
