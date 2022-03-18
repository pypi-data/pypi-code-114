#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/11 09:24
# @Author  : Lifeng
# @Site    : 
# @File    : setup.py
# @Software: PyCharm

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dfwsgroup_ios",
    description="快速启动-ios稳定性测试",

    version="2.0.2",
    author="debugfeng",
    author_email="960158047@qq.com",
    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://gitee.com/dongfang_rising_test/test-tool.git",

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.7",
    install_requires=[
        "Jinja2==3.0.3",
        "pyyaml==5.4.1",
        "tidevice==0.6.6",
    ],
    package_data={
        "": ["*.txt"],
        "dfwsgroup_ios": ["data/*.json"],
    }
)
