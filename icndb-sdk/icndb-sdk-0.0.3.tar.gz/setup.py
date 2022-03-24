from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name="icndb-sdk",
    version="0.0.3",
    author="Julio Perez",
    author_email="julio@juliopdx.com",
    license="MIT",
    install_requires=["requests >= 2.1.0"],
    url="https://github.com/JulioPDX/icndb-sdk",
    description="A simple Python SDK for some Chuck Norris jokes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
