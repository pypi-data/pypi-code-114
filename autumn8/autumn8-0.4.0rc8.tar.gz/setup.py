from setuptools import find_namespace_packages, setup
from lib.common._version import __version__

dependencies = [
    "appdirs",
    "wheel>=0.31.0",
    "boto3>=1.20.15",
    "tensorflow",
    "click>=8.0.1",
    "questionary>=1.10.0",
    "torch",
    "torchvision",
]

setup(
  name='autumn8',
  version=__version__,
  author='Autumn8',
  author_email='marcink@radcode.co', # TODO use some common support mail from autumn8?
    install_requires=dependencies,
    setup_requires=dependencies,
    packages=find_namespace_packages(include=['lib.*']),
    description="Utilities to export models to autumn8",
    entry_points={
        "console_scripts": [
            "autumn8-cli=lib.cli.main:main",
        ],
    },
)
