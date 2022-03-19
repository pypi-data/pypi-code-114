from setuptools import setup, find_packages
from os.path import abspath, dirname, join

README_MD = open(join(dirname(abspath(__file__)), "README.md")).read()

setup(
    name="stringtoolsfpat",
    version="0.0.43",
    packages=find_packages(),
    description="String tools",
    long_description=README_MD,
    long_description_content_type="text/markdown",
    url="https://github.com/fptiangco/stringtoolsfpat",
    download_url="https://github.com/fptiangco/stringtoolsfpat",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Only",
    ],
    project_urls={
        "Bug Reports": "https://github.com/fptiangco/stringtoolsfpat/issues",
        "Source": "https://github.com/fptiangco/stringtoolsfpat/",
    },
    keywords="stringtoolsfpat",
)
