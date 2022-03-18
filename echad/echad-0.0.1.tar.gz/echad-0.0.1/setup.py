import codecs
from setuptools import setup
from pathlib import Path

ECHAD_VERSION = "0.0.1"
DOWNLOAD_URL = ""


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [str(path.parent) for path in Path(package).glob("**/__init__.py")]


def read_file(filename):
    """
    Read a utf8 encoded text file and return its contents.
    """
    with codecs.open(filename, "r", "utf8") as f:
        return f.read()


setup(
    name="echad",
    packages=get_packages("urge"),
    version=ECHAD_VERSION,
    description="A rapid python ehcarts tool",
    long_description="",
    license="MIT",
    author="Hou",
    author_email="hhhoujue@gmail.com",
    url="",
    download_url=DOWNLOAD_URL,
    keywords=["ehcarts", "html"],
    install_requires=[
        "domonic >= 0.9.7",
        "path",
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Natural Language :: English",
    ],
    python_requires=">=3.9",
)
