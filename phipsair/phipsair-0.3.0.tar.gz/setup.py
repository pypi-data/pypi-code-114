from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="phipsair",
    version="0.3.0",
    description="phipsair allows controlling Philips air purifiers via encrypted CoAP.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="betaboon, Michael Frister",
    url="https://github.com/mfrister/phipsair",
    project_urls={
        "Bug Tracker": "https://github.com/mfrister/phipsair/issues",
    },
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    install_requires=[
        "aiocoap>=0.4.1, <0.5",
        "pycryptodomex>=3.13, <4.0",
    ],
    entry_points={
        "console_scripts": [
            "phipsair=phipsair.__main__:main",
        ],
    },
)
