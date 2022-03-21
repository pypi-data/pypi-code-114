from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.0.0.1'
DESCRIPTION = 'Converts integers (1, 2, 3) into ranks (1st, 2nd, 3rd)'
LONG_DESCRIPTION = "Description:\n\nA package that allows the conversion between integers, for example 1, 2 or 3, to ranks, for example 1st, 2nd or 3rd.\n\nExample Usage:\n\n ```from num2rank import num2rank\n\nprint(num2rank(5))```"

# Setting up
setup(
    name="num2rank",
    version=VERSION,
    author="AnnoyingRains",
    author_email="<annoyingrain5@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', "number", "1st", "2nd", "3rd", "1 to 1st", "number converter", "number suffix converter", "number suffix"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)