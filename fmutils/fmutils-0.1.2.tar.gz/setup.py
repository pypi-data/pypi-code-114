# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

VERSION = '0.1.2'
DESCRIPTION = "Package for directories, files & paths management utilities."

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
INSTALL_REQUIRES = [
                    'numpy'
                    ]
# Setting up
setup(

        name="fmutils", 
        version=VERSION,
        author="Talha Ilyas",
        LICENSE = 'MIT License',
        author_email="mr.talhailyas@gmail.com",
        description=DESCRIPTION,
        long_description= long_description,
        long_description_content_type="text/markdown",
        packages=find_packages(),
        install_requires=INSTALL_REQUIRES, 
        
        url = 'https://github.com/Mr-TalhaIlyas/FPUtils',
        
        keywords=['python', 'files listing', 'directories listing', 
                  'deleting files', 'randomly selecting file'],
        classifiers= [
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ]
)