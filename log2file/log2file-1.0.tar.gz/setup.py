import setuptools

with open("README.md", "r") as inf:
    long_description = inf.read()

setuptools.setup(
    name="log2file",
    version="1.0",
    author="dwSun",
    author_email="",
    description="A python logging wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dwSun/pylog2file",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=("Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License", "Operating System :: OS Independent",),
)
