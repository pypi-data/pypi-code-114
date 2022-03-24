import setuptools
# lo
with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="hmrcCurrencyRate",  
    version="0.2.0",
    author="James Huang",
    author_email="yichan.huang93@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YChanHuang/hmrcCurrencyRate",
    packages=setuptools.find_packages(),
    # packages = ['hmrc_currency_rate'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)