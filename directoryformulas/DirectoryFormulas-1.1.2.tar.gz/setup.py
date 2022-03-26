# Always prefer setuptools over distutils
from setuptools import setup, find_packages


# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: MacOS :: MacOS X',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.9'
]

setup(
    name='DirectoryFormulas',
    version='1.1.2',
    description='Module for Directory Value and other formulas',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='',
    author='FrankieOliverTrading',
    author_email='ceruttifra@gmail.com',
    license='MIT',
    py_modules=['DirectoryFormulas'],
    classifiers=classifiers,
    packages=find_packages(),
    install_requires=[''],
    include_package_data=True,
)