import os
import sys
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
def read(rel_path: str) -> str:
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, rel_path)) as fp:
        return fp.read()


def get_version(rel_path: str) -> str:
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")

setuptools.setup(
    name="controlx",
    version=get_version("src/controlx/__init__.py"),
    author="Than Nguyen",
    author_email="jonyvanthan@gmail.com",
    description="Python library to controlbox from Delta X Robot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VanThanBK/python-controlx",
    project_urls={
        "Bug Tracker": "https://github.com/VanThanBK/python-controlx",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)