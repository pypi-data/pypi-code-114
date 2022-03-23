import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DataExtractionPackage",
    version="1.0.0",
    author="Chris_Lynch",
    author_email="c.lynch278@gmail.com",
    description="A package to extract data from Collibra",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cjlynch278/DSDataExtraction",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)