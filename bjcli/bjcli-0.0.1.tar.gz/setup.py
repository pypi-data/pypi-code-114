import os
import codecs
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'

DESCRIPTION = 'Simple command line utility to run Bjoern WSGI'

LONG_DESCRIPTION = DESCRIPTION

# Setting up
setup(
    name="bjcli",
    version=VERSION,
    author="Kapustlo",
    author_email="<kapustlo@protonmail.com>",
    description=DESCRIPTION,
    ur="https://notabug.org/kapustlo/bjcli",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    keywords=['python', 'bjoern', 'cli', 'bjoern-cli', 'wsgi'],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Server",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
    ],
    python_requires=">=3.8"
)
