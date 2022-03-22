from setuptools import setup
from setuptools import find_packages

setup(
    name = 'Trip advisor',
    version = '0.0.1',
    description = 'Mock packages that allows to get information about hotels',
    Author = 'Misha Siddiqui',
    packages = find_packages(),
    install_requires=['requests']
)