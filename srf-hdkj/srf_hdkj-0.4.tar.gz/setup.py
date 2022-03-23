from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()
setup(
    name="srf_hdkj",
    version="0.4",
    author="hdkj",
    author_email="",
    description="SDK about postgres",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    install_requires=['ujson==5.1.0', 'openpyxl==3.0.9'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
