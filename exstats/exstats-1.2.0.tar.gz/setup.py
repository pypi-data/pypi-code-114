from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.2.0'
DESCRIPTION = 'A better statistics library'
LONG_DESCRIPTION = 'ExStats includes a variety of mathematical functions used in recieving data.'

# Setting up
setup(
    name="exstats",
    version=VERSION,
    author="Eccentrici (Austin Eccentrici)",
    author_email="xzntrc@protonmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'math', 'statistics','statistical mathematics'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
