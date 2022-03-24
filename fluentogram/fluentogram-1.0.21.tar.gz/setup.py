# coding=utf-8
import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="fluentogram",
    version="1.0.21",
    author="Aleksandr",
    author_email="",
    description="An addon for i18n via Project Fluent by Mozilla with telegram bots built on Aiogram3.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    keywords="example documentation tutorial",
    url="https://packages.python.org/fluentogram",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=[
        'aiogram>=3.0.0b2',
        'fluent-compiler>=0.3',
    ],
    entry_points={
        'console_scripts': [
            'i18n=fluentogram.cli:cli',
        ],
    },
)
