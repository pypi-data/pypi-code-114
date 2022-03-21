import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="prometeo-cli",
    version="0.0.1-alpha.4",
    author="Diego Moraes",
    author_email="dmoraes11cb@gmail.com",
    description="CLI Tool for the Prometeo Open Banking AP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
