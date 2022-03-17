import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="archipelagos",
    version="0.0.2",
    description="The Python Client for the Archipelagos platform.",

    long_description=README,
    long_description_content_type="text/markdown",

    url="https://www.archipelagos-labs.com",
    license="Copyright 2022. Archipelagos Labs",

    author="Archipelagos Labs",
    author_email="support@archipelagos-labs.com",

    classifiers=["Programming Language :: Python :: 3",
                 "Programming Language :: Python :: 3.7",
                 "Programming Language :: Python :: 3.8",
                 "Programming Language :: Python :: 3.9",
                 "Programming Language :: Python :: 3.10"],

    packages=["archipelagos",
              "archipelagos.common",
              "archipelagos.common.data"],

    install_requires=["geopandas>=0.10.2,<=0.10.2",
                      "numpy>=1.21.2,<=1.21.2",
                      "pandas>=1.3.5,<=1.3.5",
                      "protobuf>=3.19.1,<=3.19.1",
                      "requests>=2.27.1,<=2.27.1"],

    include_package_data=True
)
