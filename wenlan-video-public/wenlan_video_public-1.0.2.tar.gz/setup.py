#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: Haoyu Lu
# Mail: lhy1998@ruc.edu.cn
# Created Time:  2022-3-18 19:17:34
#############################################

import os

from setuptools import setup, find_packages   

with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as readme:
    README = readme.read()
 
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

         

setup(
    name = "wenlan_video_public",      
    version = "1.0.2",  
    keywords = ("pip", "wenlan"),
    description = "Wenlan - Large scale cross-modal pre-training model",
    long_description = "A large-scale video-language pre-training model.",
    license = "MIT Licence",

    url = "https://github.com/rucmlcv/Wenlan-Video-Public",     
    author = "Haoyu Lu",
    author_email = "lhy1998@ruc.edu.cn",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["numpy"],        

    classifiers=[                   
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
