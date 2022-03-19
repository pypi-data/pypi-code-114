#!/usr/bin/env python
# coding: utf-8
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="django_global_log",
    version="0.0.2",
    author="Oren Zhang",
    url="https://www.oren.ink/",
    author_email="oren_zhang@outlook.com",
    description="A Log Tool for Django",
    packages=["django_global_log", "django_global_log.migrations"],
    install_requires=[
        "django>=3.0",
        "djangorestframework>=3.9.3",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
