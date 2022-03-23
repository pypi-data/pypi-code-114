#!/usr/bin/python3
# -*- coding:Utf-8 -*-

"""
Docstring to stop linter whining.
"""

import setuptools

VERSION = "2022.03.23"
DESCRIPTION = "Command lines reminder"

with open("README.pypi.rst", "r") as fh:
    long_description = fh.read()

REQUIRED = [
    "docopt",
    "rich",
    "appdirs",
    "pypandoc",
    "stop-words",
]

setuptools.setup(
    name="pensum",
    version=VERSION,
    author="Étienne Nadji",
    author_email="etnadji@eml.cc",
    description=DESCRIPTION,
    long_description=long_description,
    packages=setuptools.find_packages(),
    package_data={
        "pensum": [
            "topics/*.md",
        ],
    },
    platforms="any",
    license="GNU General Public License v3 or later (GPLv3+)",
    classifiers=[
        "Topic :: Documentation",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
    ],
    project_urls={
        "Source Code": "https://framagit.org/etnadji/pensum",
        "Issue tracker": "https://framagit.org/etnadji/pensum/-/issues",
        "Documentation": "https://framagit.org/etnadji/pensum/-/wikis/Pensum",
        "License": "https://framagit.org/etnadji/pensum/-/blob/main/LICENSE",
    },
    entry_points={
        'console_scripts': ['pm=pensum.pm:main']
    },
    python_requires=">=3.8",
    install_requires=REQUIRED,
    keywords=[],
)

# vim:set shiftwidth=4 softtabstop=4 spl=en:
