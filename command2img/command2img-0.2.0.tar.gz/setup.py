# -*- coding: utf-8 -*-

from setuptools import setup
from os.path import join

with open("README.md") as f:
    readme = f.read()

setup(
    name="command2img",
    version="0.2.0",
    description="This is an simple program to convert a command line to image.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Emanuel Alves",
    author_email="emanuel.alves@unifei.edu.br",
    url="https://github.com/emanuel-alves/command2img",
    license="MIT",
    packages=["command2img", join("command2img", "txt2img")],
    scripts=["bin/command2img"],
    include_package_data=True,
    install_requires=[""],
    zip_safe=False,
    classifiers=[
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Utilities",
    ],
)
