#!/usr/bin/env python

from setuptools import find_packages, setup

with open("README.md") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read()

setup(
    version="0.0.1",
    name="georacle",
    url="https://github.com/georacleapi/pygeoracle",
    author="Georacle",
    author_email="opensource@georacle.io",
    description="Georacle Python SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    license="MIT",
    test_suite="tests",
    include_package_data=True,
    packages=find_packages(),
    keywords="georacle,ethereum,bitcoin,blockchain,smart-contracts",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Topic :: Security",
        "Topic :: Scientific/Engineering :: GIS",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Typing :: Typed",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
