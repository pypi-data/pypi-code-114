#!/usr/bin/env python3

import setuptools

setuptools.setup(
    name="libembroidery",
    version="1.0-alpha",
    description="Official Python binding to the libembroidery library.",
    author="The Embroidermodder Team",
    author_email="embroidermodder@gmail.com",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6"
)
