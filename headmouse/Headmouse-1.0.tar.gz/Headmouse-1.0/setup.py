from distutils.core import setup
from setuptools import find_packages
import os

# Optional project description in README.md:
current_directory = os.path.dirname(os.path.abspath(__file__))

try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''
setup(

# Project name: 
name='Headmouse',

# Packages to include in the distribution: 
packages=find_packages(','),

# Project version number:
version='1.0',

# List a license for the project, eg. MIT License
license='MIT',

# Short description of your library: 
description='An augmentative tool to use the mouse with the movement of the head.',

# Long description of your library: .
long_description=long_description,

long_description_content_type='text/markdown',

author='Ramiro Fontalva',

author_email='ramirofontalva@gmail.com',

url='https://github.com/rfontalva',

download_url='https://github.com/rfontalva/Headmouse',

keywords=["headmouse", "HeadMouse", "Image processing", "mouse"],

install_requires=[
    'dlib',
    'opencv-python',
    'pynput',
    'scipy'
],

# https://pypi.org/classifiers/ 
classifiers=[
    'Development Status :: 4 - Beta', 
    'Topic :: Scientific/Engineering :: Image Processing', 
    'License :: OSI Approved :: MIT License',
    'Intended Audience :: End Users/Desktop'
]
)
