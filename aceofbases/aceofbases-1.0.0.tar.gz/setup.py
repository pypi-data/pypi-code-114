#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="aceofbases",
    version="1.0.0",
    packages=["aceofbases"],
    
    python_requires=">=3.5",
    
    install_requires=["bx-python"],
    
    entry_points = {
        'console_scripts': ['aceofbases=aceofbases.main:main',
        'gff2bedFiles=aceofbases.gff2bedFiles:main'],
    },
    
    author="Juan L. Mateo",
    author_email="mateojuan@uniovi.es",
    description="ACEofBASEs, a careful evaluation of BaseEdits",
    long_description = long_description,
    long_description_content_type="text/markdown",
    keywords="CRISPR",
    url="https://bitbucket.org/juanlmateo/aceofbases_standalone",
    project_urls={
        "Bug Tracker": "https://bitbucket.org/juanlmateo/aceofbases_standalone/issues",
    },
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License"
    ],
)
