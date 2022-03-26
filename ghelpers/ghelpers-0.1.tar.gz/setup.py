from setuptools import setup,find_packages
# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

__VERSION__ = "0.1"
__NAME__ = 'ghelpers'
setup(
    name=__NAME__,
    version=__VERSION__,
    packages=find_packages(),
    install_requires=[
        'google',
        'google-cloud',
        'google-cloud-secret-manager',
    ],  # add any additional packages that
    extras_require={
        'secretmanager': ['google-cloud-secret-manager'],
    },
    url=f'https://github.com/rimedinaz/{__NAME__}',
    license='Apache License 2.0',
    author='Richard Medina',
    author_email='rimedinaz@gmail.com',
    description='Grouping of common functions used in Google Cloud Platform, intended to help other processes.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.4.*",
)
