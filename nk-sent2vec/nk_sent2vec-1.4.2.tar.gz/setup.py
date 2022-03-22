import os
from distutils.core import setup
from setuptools.command.develop import develop
from setuptools.command.install import install


setup(
    name="nk_sent2vec",
    version="1.4.2",
    description="Embeds text documents using sent2vec",
    author="New Knowledge",
    license='BSD-3-Clause',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=["nk_sent2vec"],
    install_requires=[
        "Cython==0.29.24",
        "numpy>=1.15.4",
        "pytest",
        "sent2vec>=0.2,<0.3",
    ],
)
