"""Setup.py script for packaging project."""

from setuptools import setup, find_packages

import json
import os

from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


with open('requirements.txt') as f:
    required = f.read().splitlines()

if __name__ == '__main__':
    setup(
        version=os.getenv('GITVERSION_SEMVER'),
        package_dir={'': 'src'},
        packages=find_packages('src', include=[
            'demo*'
        ]),
        long_description=long_description,
        long_description_content_type='text/markdown',
        description='A demo package.',
        install_requires= required
    )
