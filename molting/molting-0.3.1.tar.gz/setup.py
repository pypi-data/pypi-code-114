# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['molting']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.6.0,<0.7.0']

entry_points = \
{'console_scripts': ['molting = molting.main:cli']}

setup_kwargs = {
    'name': 'molting',
    'version': '0.3.1',
    'description': 'Automatically bump your project files to the latest version.',
    'long_description': '# 🐍🐍 molting\n\nAutomatically bump your project files to the latest version.\n\n![PyPI](https://img.shields.io/pypi/v/molting?color=%2316a34a)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/molting?color=%230fb882)\n[![CI - nox sessions](https://github.com/lucasmelin/molting/actions/workflows/ci.yaml/badge.svg)](https://github.com/lucasmelin/molting/actions/workflows/ci.yaml)\n\n---\n\n## Overview\n\nSimplifies the process of creating new releases by bumping version numbers, updating release notes, and creating a GitHub release.\n\n- **Easy to use** - Can be called without any arguments; let `molting` figure out the specifics.\n- **Built for CI/CD** - Run from GitHub Actions or similar CI/CD tool to completely automate your release process.\n\n## How it works\n\n```mermaid\ngraph TD\n    A[Invoke molting CLI] -->|Specify semver type| B(Calculate new version)\n    A -->|Omit semver type| C(Get commit messages)\n    C --> D[Guess change type]\n    D --> B\n    B --> G(Get changelog notes)\n    G -->|Changelog notes found| E(Update version in files)\n    G -->|No Changelog notes exist| J(Get commit messages)\n    J -->|Write commit messages to Changelog| G\n    E --> F(Create new git tag)\n    F --> K(Create GitHub release with Changelog notes)\n```\n',
    'author': 'Lucas Melin',
    'author_email': 'lucas.melin@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/lucasmelin/molting',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
