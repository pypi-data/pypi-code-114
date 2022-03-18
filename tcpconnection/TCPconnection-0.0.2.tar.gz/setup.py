from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="TCPconnection",
    version="0.0.2",
    author="Vinicius Costa",
    author_email="viniciusgcto@gmail.com",
    description="Simple TCP connection",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/viniciusgcto/DIO/tree/main/Desafio_Pacotes_IMG_Python",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)