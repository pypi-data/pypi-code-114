# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['magicpyden', 'magicpyden.tests']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp[speedups]>=3.8.1,<4.0.0',
 'inflection>=0.5.1,<0.6.0',
 'pydantic>=1.9.0,<2.0.0']

setup_kwargs = {
    'name': 'magicpyden',
    'version': '0.1.1',
    'description': 'Async Python API wrapper for MagicEden',
    'long_description': None,
    'author': 'Christian Pérez Villanueva',
    'author_email': 'perez.villanueva.christian34@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
