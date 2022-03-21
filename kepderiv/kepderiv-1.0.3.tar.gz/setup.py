# -*- coding: utf-8 -*-

# Copyright 2019-2021 Jean-Baptiste Delisle
#
# This file is part of kepderiv.
#
# kepderiv is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# kepderiv is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with kepderiv.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, Extension
import numpy.distutils.misc_util
import os

path = os.path.abspath(os.path.dirname(__file__))

info = {}
with open(os.path.join(path, 'kepderiv', '__info__.py'), 'r') as f:
  exec(f.read(), info)
with open('README.rst', 'r', encoding='utf-8') as readme:
  long_description = readme.read()

c_ext = Extension('kepderiv.libkeplerian',
  sources=['kepderiv/pywrapkeplerian.c', 'kepderiv/libkeplerian.c'],
  language='c')

setup(name=info['__title__'],
  version=info['__version__'],
  author=info['__author__'],
  author_email=info['__author_email__'],
  license=info['__license__'],
  description=info['__description__'],
  long_description=long_description,
  url=info['__url__'],
  packages=['kepderiv'],
  ext_modules=[c_ext],
  include_dirs=numpy.distutils.misc_util.get_numpy_include_dirs(),
  python_requires='>=3.6',
  install_requires='numpy>=1.16')
