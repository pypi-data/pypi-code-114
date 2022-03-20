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
    'version': '0.1.1',
    'description': "Python implementation of Rust's dbg! macro",
    'long_description': None,
    'author': 'Marcel Rød',
    'author_email': 'marcelroed@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/marcelroed/dbgpy',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3,<4',
}


setup(**setup_kwargs)
