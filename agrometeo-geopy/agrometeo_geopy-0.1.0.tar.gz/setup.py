# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['agrometeo', 'tests']

package_data = \
{'': ['*']}

install_requires = \
['geopandas>=0.10.2,<0.11.0',
 'matplotlib>=3.5.1,<4.0.0',
 'requests>=2.27.1,<3.0.0']

extras_require = \
{'cx': ['contextily>=1.2.0,<2.0.0'],
 'dev': ['tox>=3.20.1,<4.0.0',
         'virtualenv>=20.2.2,<21.0.0',
         'pip>=20.3.1,<21.0.0',
         'twine>=3.3.0,<4.0.0',
         'pre-commit>=2.12.0,<3.0.0',
         'toml>=0.10.2,<0.11.0'],
 'doc': ['mkdocs>=1.2.3,<2.0.0',
         'mkdocs-include-markdown-plugin>=3.3.0,<4.0.0',
         'mkdocstrings>=0.18.0,<0.19.0',
         'mkdocs-autorefs>=0.3.1,<0.4.0'],
 'ox': ['osmnx>=1.1.2,<2.0.0'],
 'test': ['black==20.8b1',
          'isort==5.6.4',
          'flake8==3.8.4',
          'flake8-docstrings>=1.6.0,<2.0.0',
          'pytest>=6.2.5,<7.0.0',
          'pytest-cov==2.10.1']}

setup_kwargs = {
    'name': 'agrometeo-geopy',
    'version': '0.1.0',
    'description': 'Pythonic interface to access Agrometeo data.',
    'long_description': '[![PyPI version fury.io](https://badge.fury.io/py/agrometeo-geopy.svg)](https://pypi.python.org/pypi/agrometeo-geopy/)\n[![Documentation Status](https://readthedocs.org/projects/agrometeo-geopy/badge/?version=latest)](https://agrometeo-geopy.readthedocs.io/en/latest/?badge=latest)\n[![CI/CD](https://github.com/martibosch/agrometeo-geopy/actions/workflows/dev.yml/badge.svg)](https://github.com/martibosch/agrometeo-geopy/blob/main/.github/workflows/dev.yml)\n[![codecov](https://codecov.io/gh/martibosch/agrometeo-geopy/branch/main/graph/badge.svg?token=hKoSSRn58a)](https://codecov.io/gh/martibosch/agrometeo-geopy)\n[![GitHub license](https://img.shields.io/github/license/martibosch/agrometeo-geopy.svg)](https://github.com/martibosch/agrometeo-geopy/blob/main/LICENSE)\n\n# agrometeo-geopy\n\nPythonic interface to access [agrometeo.ch](https://agrometeo.ch) data.\n\n## Acknowledgements\n\n* This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [zillionare/cookiecutter-pypackage](https://github.com/zillionare/cookiecutter-pypackage) project template.\n',
    'author': 'Martí Bosch',
    'author_email': 'marti.bosch@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/martibosch/agrometeo-geopy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
