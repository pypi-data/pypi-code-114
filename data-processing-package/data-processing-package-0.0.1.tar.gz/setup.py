from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="data-processing-package",
    version="0.0.1",
    author="Thomas",
    author_email="thomasfurtado21@gmail.com",
    description="Machine Learning package",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ThomasFurtado/data-processing-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
