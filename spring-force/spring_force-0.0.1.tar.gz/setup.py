from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="spring_force",
    version="0.0.1",
    author="Egleidson Frederik",
    description="A tool for generating solutions and plots for Hooke Law and Harmonic Oscillation",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tiemi/image-processing-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.5',
)