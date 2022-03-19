from setuptools import setup
from mkutils import __version__, __url__, __author__

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="utils-mkmenta",
    version=__version__,
    description="Utils for debugging and fast implementation of scripts.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=__url__,
    author=__author__,
    author_email="thisisnotmyemail@gmail.com",
    packages=["mkutils"],
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=["tqdm",
                      "Pillow",
                      "plotly"]
)
