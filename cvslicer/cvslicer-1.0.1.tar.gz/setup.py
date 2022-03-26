#!/usr/bin/env python
import os 

HERE = os.path.dirname(__file__)

def read(file):
  with open(os.path.join(HERE, file), "r") as fh:
    return fh.read()

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


long_description = read("./README.md")

setup(name='cvslicer',
      version='1.0.1',
      description='CV Slicer',
      author='Quek JY',
      packages=['cvslicer'],
      long_description=long_description,
      long_description_content_type='text/markdown',
      platforms='any',
      install_requires=['numpy', 'Pillow'],
      extras_require={ 'extra' : ['opencv-python'] }, # To run the test script and sample
      keywords = ['slice', 'crop', 'smart', 'image recognition', 'object', 'opencv', 'cv', 'vision'],
      classifiers = [],
      url = "https://github.com/JY-Quek/CVSlicer",
    )
