import setuptools

with open("README.md", "r",encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="languageIdentiPackage",
    version="0.0.2",
    author="ken",
    author_email="kenbliky@gmail.com",
    description="Image kernel.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/taw19960426/languageIdentiPackage.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
