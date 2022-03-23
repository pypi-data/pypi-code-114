# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name="pykb",
    version="2.1.0",
    license="BSD",
    description="Python API to access a KB-API conformant knowledge base",
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
    ],
    url="https://github.com/severin-lemaignan/pykb",
    author="Séverin Lemaignan",
    author_email="severin.lemaignan@brl.ac.uk",
    py_modules=["kb"],
)
