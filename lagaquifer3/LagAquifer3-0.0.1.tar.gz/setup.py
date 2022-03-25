#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'The solution developed by Lin and Yeh (2017)'
# Setting up
setup(name="LagAquifer3",
    version=VERSION,
    author="YF Lin",
    author_email="<aar246860@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['Aquifer', 'pumping test', 'lagging effects'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows"],)

