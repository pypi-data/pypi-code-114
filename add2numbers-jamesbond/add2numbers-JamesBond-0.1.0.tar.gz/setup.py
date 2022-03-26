# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['add2numbers_jamesbond']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'add2numbers-jamesbond',
    'version': '0.1.0',
    'description': 'add two numbers',
    'long_description': '',
    'author': 'James Bond',
    'author_email': 'JamesBond07@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
