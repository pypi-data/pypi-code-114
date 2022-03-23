"""
Setup, package, and build file for the bn254 cryptography library.
"""
from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

name = "bn254"
version = "0.1.0"

setup(
    name=name,
    version=version,
    packages=[name,],
    install_requires=[],
    license="MIT",
    # url="https://github.com/nthparty/bn254",
    # author="Wyatt Howe",
    # author_email="",
    description="Python library that supports operations on the "+\
                "BN(2,254) pairing-friendly curve.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
)
