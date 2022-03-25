from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="tradutor",
    version="0.0.1",
    author="Paulo Ricardo Diniz",
    author_email="prtdiniz@hotmail.com",
    description="Translate English into Portuguese and Portuguese into English",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prtdiniz/tradutor.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
