from setuptools import setup, find_packages
from os.path import abspath, dirname, join

README_MD = open(join(dirname(abspath(__file__)), "README.md")).read()

setup(
    name="numtoolsfpat",
    version="0.0.4",
    packages=find_packages(),
    description="Number tools",
    long_description=README_MD,
    long_description_content_type="text/markdown",
    url="https://github.com/fptiangco/numtoolsfpat",
    download_url="https://github.com/fptiangco/numtoolsfpat",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Only",
    ],
    project_urls={
        "Bug Reports": "https://github.com/fptiangco/numtoolsfpat/issues",
        "Source": "https://github.com/fptiangco/numtoolsfpat/",
    },
    keywords="numtoolsfpat",
)
