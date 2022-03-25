#
# Copyright (c) 2019-2021 Thomas Kramer.
#
# This file is part of liberty-parser 
# (see https://codeberg.org/tok/liberty-parser).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
from setuptools import setup, find_packages


def readme():
    with open("README.md", "r") as f:
        return f.read()


setup(name='liberty-parser',
      version='0.0.14',
      description='Liberty format parser.',
      long_description=readme(),
      long_description_content_type="text/markdown",
      keywords='liberty parser',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)',
          'Programming Language :: Python :: 3'
      ],
      url='https://codeberg.org/tok/liberty-parser',
      author='T. Kramer',
      author_email='dont@spam.me',
      license='GPLv3',
      packages=find_packages(),
      install_requires=[
          'numpy==1.*',
          'sympy==1.6.*',
          'lark>=0.12.1'
      ],
      zip_safe=False)
