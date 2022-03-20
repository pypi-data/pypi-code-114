#!/usr/bin/python3
"""
Setup
"""
from setuptools import find_packages
from distutils.core import setup

version = "1.0.0"

with open("README.md") as f:
    long_description = f.read()

setup(
    name="ofxstatement-equabankcz",
    version=version,
    author="Jan Koscielniak",
    author_email="jkosci@gmail.com",
    url="https://github.com/kosciCZ/ofxstatement-equabankcz",
    description=("ofxstatement plugin for Equa Bank (CZ)"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GPLv3",
    keywords=["ofx", "banking", "statement"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Natural Language :: English",
        "Topic :: Office/Business :: Financial :: Accounting",
        "Topic :: Utilities",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
    namespace_packages=["ofxstatement", "ofxstatement.plugins"],
    entry_points={
        "ofxstatement": [
            "equabankcz = ofxstatement.plugins.equabankcz:EquaBankCZPlugin"
        ]
    },
    install_requires=["ofxstatement"],
    include_package_data=True,
    zip_safe=True,
)
