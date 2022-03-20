"""Some Docstring"""
from skbuild import setup
from setuptools import find_packages

from pathlib import Path


setup(
    name="{{cookiecutter.module_name}}",
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.email}}",
    version="{{cookiecutter.version}}",
    url="{{cookiecutter.url}}",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "{{cookiecutter.module_name}}": [
            "py.typed",
            "_{{cookiecutter.module_name}}/__init__.pyi",
            "*.h",
            "*.cpp",
            "*.txt",
            "rtl/*.sv",
            "rtl/*.svh",
            "rtl/*.v",
            "rtl/*.vhd",
        ],
    },
    cmake_install_dir="{{cookiecutter.module_name}}",
)
