from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

requirements = ["aiohttp~=3.8.1", "certifi~=2021.10.8", "ujson~=5.1.0"]

setup(
    name='auto1_api',
    version='0.1.2',
    author='bl4ckm45k',
    author_email='nonpowa@gmail.com',
    description='Async library for auto1.by API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bl4ckm45k/auto1_api",
    license="Apache License, Version 2.0 see LICENSE file",
    packages=['auto1_api'],
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7'
)
