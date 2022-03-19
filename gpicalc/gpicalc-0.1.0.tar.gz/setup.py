import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gpicalc",
    version="0.1.0",
    author="M. Y. Chia",
    author_email="chiamy94@gmail.com",
    description="a package for calculating global performance indicator (GPI)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/planta94/gpi",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)