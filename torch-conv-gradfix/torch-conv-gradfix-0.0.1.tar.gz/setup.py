#!/usr/bin/env python

from dunamai import Version
from setuptools import find_packages, setup

setup(
    author="Peter Yuen",
    author_email="ppeetteerrsx@gmail.com",
    python_requires=">=3.8",
    description="A clean, automated setup for publishing simple Python packages to PyPI and Anaconda.",
    install_requires=[
        x.strip() for x in open("requirements.txt").readlines() if x.strip() != ""
    ],
    license="MIT license",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="torch-conv-gradfix",
    name="torch-conv-gradfix",
    packages=find_packages(
        include=["torch_conv_gradfix", "torch_conv_gradfix.*"],
        exclude=["docs"],
    ),
    package_data={
        "": ["*.txt"],
    },
    test_suite="tests",
    url="https://github.com/ppeetteerrs/torch-conv-gradfix",
    version=Version.from_any_vcs().serialize(),
    zip_safe=False,
    options={"bdist_wheel": {"universal": True}},
)
