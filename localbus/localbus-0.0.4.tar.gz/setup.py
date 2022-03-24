import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="localbus",
    version="0.0.4",
    author="",
    author_email="itsstefan@protonmail.com",
    description="Lightweight python IPC package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/itsstefan/localbus",
    packages=["localbus"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License", 
    ],
    python_requires=">=3.6",
)

