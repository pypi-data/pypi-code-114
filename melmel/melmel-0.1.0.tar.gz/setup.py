from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1.0'
DESCRIPTION = 'Simplifies and adds fun things to Python'
LONG_DESCRIPTION = 'Today Melonpod.exe has made a module for the python coding langauge that makes many long functions simpler and adds a few new interesting things to try out as well'

# Setting up
setup(
    name="melmel",
    version=VERSION,
    author="Melonpod",
    author_email="<melonnator32@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['random','math','os','datetime','colorama'],
    keywords=['python', 'simple', 'code','fun'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
