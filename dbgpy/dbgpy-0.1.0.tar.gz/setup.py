# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dbgpy']

package_data = \
{'': ['*']}

extras_require = \
{':python_version < "3.9"': ['astunparse>=1,<2']}

setup_kwargs = {
    'name': 'dbgpy',
    'version': '0.1.0',
    'description': "Python implementation of Rust's dbg! macro using CSTs",
    'long_description': None,
    'author': 'Marcel Rød',
    'author_email': 'marcelroed@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
