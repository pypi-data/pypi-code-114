from os import path

from setuptools import find_packages, setup

def strip_comments(l):
    return l.split("#", 1)[0].strip()


def reqs():
    file = path.join(path.dirname(__file__), "requirements.txt")
    with open(file) as fh:
        reqs = [strip_comments(l) for l in fh.readlines()]
        return [r for r in reqs if r]


def long_description():
    with open("README.md", "r") as fh:
        return fh.read()


def version():
    with open(path.join(path.dirname(__file__), "collimator", "VERSION")) as f:
        return f.read().strip()


setup(
    name="Collimator",
    version=version(),
    description="Electronic collimator for your telescope",
    url="http://github.com/wlatanowicz/collimator",
    author="Wiktor Latanowicz",
    author_email="collimator@wiktor.latanowicz.com",
    license="MIT",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    packages=["collimator"],
    zip_safe=False,
    install_requires=reqs(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    include_package_data=True,
)
