#!/usr/bin/env python3

from setuptools import setup


setup(name='qt5_levelmeter',
      version='1.0',
#      install_requires=["PyQT5"],
      python_requires='>=3',
      license="bsd-3-clause",
      description="Level Meter (VU Meter) for QT5",
      long_description_content_type='text/markdown',
      long_description="""# Level Meter (VU Meter) for QT5

## Installation:

### From source:

    git clone https://gitlab.com/t-5/python3-qt5-levelmeter.git
    cd python3-qt5-levelmeter
    pip3 install .

### Debian Package:

I have a prebuilt debian package for this module.
Please refer to the page https://t-5.eu/hp/Software/Debian%20repository/ to setup the repo.
After the repo is setup you can install the package by issueing

    apt install python3-qt5-levelmeter

in a shell.


## Usage:

Usage:
from qt5_levelmeter import QLevelMeter

meter = QLevelMeter(parent)

call periodically:
meter.levelChanged(levelInDb)""",
      author='Jürgen Herrmann',
      author_email='t-5@t-5.eu',
      url='https://gitlab.com/t-5/qt5_levelmeter',
      packages=['qt5_levelmeter'],
      package_dir={'qt5_levelmeter': 'src'},
      package_data={'': ['src/*.css']},
      include_package_data=True,
     )
