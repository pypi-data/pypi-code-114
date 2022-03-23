import setuptools

from loci_checkmarx import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="loci-checkmarx",
    author="TheTwitchy",
    version=__version__,
    author_email="thetwitchy@thetwitchy.com",
    description="The official Loci Notes Checkmarx results importer.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/loci-notes/loci-checkmarx",
    packages=setuptools.find_packages(),
    install_requires=[
        "click",
        "requests",
        "rich",
        "defusedxml"
    ],
    entry_points={
        "console_scripts": [
            "loci-checkmarx = loci_checkmarx.main:loci_checkmarx",
        ],
    },
)
