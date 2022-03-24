import os
from setuptools import setup
from setuptools import find_packages
import logging
from importlib import util
from os import path

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

spec = util.spec_from_file_location(
    "prismacloud.version", os.path.join("prismacloud", "version.py")
)

# noinspection PyUnresolvedReferences
mod = util.module_from_spec(spec)
spec.loader.exec_module(mod)  # type: ignore
version = mod.version  # type: ignore

setup(
    extras_require={},
    install_requires=[
        "requests",
        "pandas",
        "jsondiff",
        "ipython",
        "api-client",
        "click",
        "click_help_colors",
        "tabulate",
        "coloredlogs"
    ],
    name = "prismacloud-cli",
    version = version,
    python_requires=">=3.7",
    author = "Steven de Boer, Simon Melotte, Tom Kishel",
    author_email = "stdeboer@paloaltonetworks.com, smelotte@paloaltonetworks.com, tkishel@paloaltonetworks.com",
    description = ("Prisma Cloud CLI"),
    license = "BSD",
    keywords = "prisma cloud cli",
    url = "https://github.com/se-cloud-emea/prismacloud-cli",
    packages=find_packages(),
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License"
    ],
    entry_points="""
        [console_scripts]
        pc=prismacloud.cli:cli
    """,
)