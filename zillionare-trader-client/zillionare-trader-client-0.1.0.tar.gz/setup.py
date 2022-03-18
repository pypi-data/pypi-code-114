# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tests', 'traderclient']

package_data = \
{'': ['*']}

install_requires = \
['arrow>=1.2.2,<2.0.0', 'enum34>=1.1.10,<2.0.0', 'requests>=2.27.1,<3.0.0']

extras_require = \
{'dev': ['tox>=3.20.1,<4.0.0',
         'virtualenv>=20.2.2,<21.0.0',
         'pip>=20.3.1,<21.0.0',
         'twine>=3.3.0,<4.0.0',
         'pre-commit>=2.12.0,<3.0.0',
         'toml>=0.10.2,<0.11.0'],
 'doc': ['mkdocs>=1.1.2,<2.0.0',
         'mkdocs-include-markdown-plugin>=1.0.0,<2.0.0',
         'mkdocs-material>=6.1.7,<7.0.0',
         'mkdocstrings>=0.13.6,<0.14.0',
         'mkdocs-autorefs==0.1.1'],
 'test': ['black==20.8b1',
          'isort==5.6.4',
          'flake8==3.8.4',
          'flake8-docstrings>=1.6.0,<2.0.0',
          'pytest==6.1.2',
          'pytest-cov==2.10.1']}

setup_kwargs = {
    'name': 'zillionare-trader-client',
    'version': '0.1.0',
    'description': 'Skeleton project created by Python Project Wizard (ppw).',
    'long_description': '# zillionare-trader-client\n\n\n<p align="center">\n<a href="https://pypi.python.org/pypi/zillionare-trader-client">\n    <img src="https://img.shields.io/pypi/v/zillionare-trader-client.svg"\n        alt = "Release Status">\n</a>\n\n<a href="https://github.com/zillionare/zillionare-trader-client/actions">\n    <img src="https://github.com/zillionare/zillionare-trader-client/actions/workflows/main.yml/badge.svg?branch=release" alt="CI Status">\n</a>\n\n<a href="https://zillionare-trader-client.readthedocs.io/en/latest/?badge=latest">\n    <img src="https://readthedocs.org/projects/zillionare-trader-client/badge/?version=latest" alt="Documentation Status">\n</a>\n\n</p>\n\n\nSkeleton project created by Python Project Wizard (ppw)\n\n\n* Free software: MIT\n* Documentation: <https://zillionare-trader-client.readthedocs.io>\n\n\n## Features\n\n* TODO\n\n## Credits\n\nThis package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [zillionare/cookiecutter-pypackage](https://github.com/zillionare/cookiecutter-pypackage) project template.\n',
    'author': 'Aaron Yang',
    'author_email': 'code@jieyu.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/zillionare/trader-client',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<3.9',
}


setup(**setup_kwargs)
