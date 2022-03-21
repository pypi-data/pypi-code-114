# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hot_shelve']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'hot-shelve',
    'version': '0.1.0',
    'description': 'A wrapper for Python shelve that supports updating nested dictionaries in a simple way.',
    'long_description': None,
    'author': 'likianta',
    'author_email': 'likianta@foxmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
