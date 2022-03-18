import pathlib
from setuptools import find_packages, setup
from setuptools.command.develop import develop
from setuptools.command.install import install
import os

# current directory
HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()
DESC = ('PSDR_CUDA')

REQUIRES_PYTHON = '>=3.8.0'

# run setup
setup(
    name='dodoco',
    version="0.0.1",
    description=DESC,
    long_description=README,
    long_description_content_type="text/markdown",
    author='Kai Yan',
    author_email='kyan8@uci.edu',
    python_requires=REQUIRES_PYTHON,
    url="https://psdr-cuda.readthedocs.io",
    keywords='differentiable rendering, SVBRDF, gradient descent, optimization',
    packages=['dodoco'],
    install_requires=[
        'numpy>=1.18.5',
        'matplotlib>=3.3.2',
        ],
    include_package_data=True,
    license='Massachusetts Institute of Technology Research License',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Topic :: Multimedia :: Graphics',
        'Programming Language :: Python :: 3.8',
    ]
)