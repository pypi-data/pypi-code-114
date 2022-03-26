# -*- coding: utf-8 -*-
"""
@ author      : Di Hu
@ contact     : hudi_0011@yeah.net
@ date        : 2022/3/26 14:52
@ file        : __init__.py
@software     : win10  python3.7
@ description :
"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="FEWS",
    version="1.0.2",
    author="胡迪-华中科技大学",
    author_email="hudi_0011@yeah.net",
    description="早期故障预警系统工具",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
