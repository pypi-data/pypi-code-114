# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['difftree']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['difftree = difftree.main:entry']}

setup_kwargs = {
    'name': 'difftree',
    'version': '0.1.0',
    'description': 'Diff two directories recursively',
    'long_description': None,
    'author': 'Malthe Jørgensen',
    'author_email': 'malthe.jorgensen@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
