# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Raff Libraries for Effective Data Visualization'
LONG_DESCRIPTION = 'Make your data visualization more attractive and effective with Ralifore. Built from Matplotlib and Seaborn which will make it easy for you to tell stories with data effectively. Can be used for exploratory analysis, explanatory analysis, and even reporting at once. Enjoy the convenience of creating effective graphics with Ralifore: Raff Libraries for Effective Data Visualization.'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="ralifore", 
        version=VERSION,
        author="Rafka Imanda Putra",
        author_email="rafka.0312@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['matplotlib','seaborn'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'data visualization'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
