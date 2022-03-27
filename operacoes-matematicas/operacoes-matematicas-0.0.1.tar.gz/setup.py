from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="operacoes-matematicas",
    version="0.0.1",
    author="Renato Olmedo", 
    author_email="renato78563@gmail.com",
    description="This package is used to general math operations in python",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RenatoOlmedo/math-python-package.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)