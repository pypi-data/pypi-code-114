from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.0.1'
DESCRIPTION = 'Test'
LONG_DESCRIPTION = 'Test'

# Setting up
setup(
    name="encode_ai",
    version=VERSION,
    author="Test",
    author_email="klmsathish@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)