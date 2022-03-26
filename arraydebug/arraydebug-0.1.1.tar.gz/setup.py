#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("HISTORY.md") as history_file:
    history = history_file.read()

with open("requirements.txt") as requirements_file:
    requirements = requirements_file.read().splitlines()

with open("requirements_dev.txt") as requirements_dev_file:
    test_requirements = requirements_dev_file.read().splitlines()

setup(
    author="Qimai Li",
    author_email="liqimai@qq.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    description="ArrayDebug generates human-friendly debug information for array-like objects.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="arraydebug",
    name="arraydebug",
    package_dir={"": "src"},
    packages=find_packages(where="src", include=["arraydebug", "arraydebug.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/liqimai/arraydebug",
    project_urls={
        "Bug Tracker": "https://github.com/liqimai/arraydebug/issues",
    },
    version="0.1.1",
    zip_safe=True,
)
