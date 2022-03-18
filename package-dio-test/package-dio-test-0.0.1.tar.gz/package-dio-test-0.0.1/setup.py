from setuptools import setup,find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package-dio-test",
    version="0.0.1",
    author="raila",
    description="test publication python package",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RailaAndrade/py-package-example",
    packages=find_packages('package-dio-test'),
    install_requires=requirements,
    python_requires='>=3.8',
)