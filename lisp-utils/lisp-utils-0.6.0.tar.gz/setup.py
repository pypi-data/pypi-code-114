import setuptools
import sys
import os

with open("README-package.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    install_requires = [ x.strip() for x in fh.read().split('\n') if len(x.strip()) > 0 ]

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).split('\n'):
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1].strip()
    else:
        raise RuntimeError("Unable to find version string.")


setuptools.setup(
    name="lisp-utils", 
    version=get_version('lisp_utils/__init__.py'),
    author="Linkspirit Team",
    author_email="tecnici@linkspirit.it",
    description="This package contains some Linkspirit classes such as Database, Configuration.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.linkspirit.it/linkspirit/python-lisp-utils.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=install_requires,
    
    python_requires='>=3',
)
