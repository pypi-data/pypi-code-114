# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tokamak', 'tokamak.radix_tree', 'tokamak.web']

package_data = \
{'': ['*']}

extras_require = \
{'examples': ['hypercorn>=0.13.2,<0.14.0'],
 'full': ['hypercorn>=0.13.2,<0.14.0', 'trio>=0.20.0,<0.21.0'],
 'web': ['trio>=0.20.0,<0.21.0']}

setup_kwargs = {
    'name': 'tokamak',
    'version': '0.3.0',
    'description': 'HTTP Router based on radix trees',
    'long_description': None,
    'author': 'Erik Aker',
    'author_email': 'eraker@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
