# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['reproduci']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0']

entry_points = \
{'console_scripts': ['reproduci = reproduci.main:cli']}

setup_kwargs = {
    'name': 'reproduci',
    'version': '0.6.0',
    'description': 'Companion project to github.com/gastrovec/reproduci',
    'long_description': None,
    'author': 'L3viathan',
    'author_email': 'git@l3vi.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
