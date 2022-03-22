# -*- coding: utf-8 -*-
import re
from pathlib import Path
from pkg_resources import VersionConflict, require
from setuptools import setup
import sys

try:
    with open('setup.cfg') as fin:
        for line in fin:
            matched = re.match(r'\s*version\s*=\s*([.0-9abrc])\b', line)
            if matched:
                global __version__
                __version__ = (matched.groups()[-1] or '').strip()
                break
except Exception as e:
    print('ERROR in setup.py: Unable to find version in setup.cfg')
    print(e)

REPO_DIR = Path(__file__).resolve().absolute().parent
name = REPO_DIR.name
package_data = {
    name: [str(p) for p in REPO_DIR.glob(f'src/{name}/data')]
}

try:
    require('setuptools>=38.3')
except VersionConflict:
    print("Error: version of setuptools is too old (<38.3)!")
    sys.exit(1)


if __name__ == "__main__":
    setup(
        name=name,
        package_data=package_data)
