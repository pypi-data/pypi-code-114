#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import find_packages
from setuptools import setup

# Read the contents of the README file
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="haploblock-shuffler",
    version="0.0.6",
    license="MIT",
    description="Create all possible combinations of phased and unphased blocks in a vcf",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Redmar van den Berg",
    author_email="RedmarvandenBerg@lumc.nl",
    url="https://github.com/redmar-van-den-berg/haploblock-shuffler",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        "Topic :: Utilities",
    ],
    project_urls={
        "Changelog": "https://github.com/redmar-van-den-berg/haploblock-shuffler/blob/master/CHANGELOG.md",
        "Issue Tracker": "https://github.com/redmar-van-den-berg/haploblock-shuffler/issues",
    },
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    python_requires=">=3.7.*",
    install_requires=["pyvcf3"],
    extras_require={},
    setup_requires=["pytest-runner"],
    entry_points={
        "console_scripts": ["haploblock-shuffler=haploblock_shuffler.cli:main"]
    },
)
