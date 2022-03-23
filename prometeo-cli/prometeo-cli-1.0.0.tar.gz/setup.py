import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="prometeo-cli",
    version="1.0.0",
    author="Diego Moraes",
    author_email="dmoraes11cb@gmail.com",
    description="CLI Tool for the Prometeo Open Banking API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dieg0moraes/prometeo-cli",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
