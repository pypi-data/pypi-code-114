# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gendiff', 'gendiff.scripts']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0', 'pytest-cov>=3.0.0,<4.0.0']

entry_points = \
{'console_scripts': ['gendiff = gendiff.scripts.gendiff_s:main']}

setup_kwargs = {
    'name': 'hexlet-code-at-shiffter',
    'version': '0.1.0',
    'description': 'Generate diff',
    'long_description': None,
    'author': 'shifter',
    'author_email': 'vanfre93@gmail.com.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
