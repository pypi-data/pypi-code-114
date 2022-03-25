# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gourav']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'hitler',
    'version': '0.1.1',
    'description': 'this is random code unnecessary',
    'long_description': None,
    'author': 'Gourav Saini',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
