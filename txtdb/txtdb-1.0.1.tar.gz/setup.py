from setuptools import setup, find_packages
from pathlib import Path

VERSION = "1.0.1"
DESCRIPTION = "A simple NoSQL database that uses .txt files."
path = Path(__name__).parent
long_description = (path / "README.md").read_text()

# Setting up
setup(
    name="txtdb",
    version=VERSION,
    author="Marco Vidali",
    author_email="<vidali.marco@protonmail.com>",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=["db", "database", "txt", "text", "nosql"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
