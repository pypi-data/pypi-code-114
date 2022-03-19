# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ctfd']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'ctfd',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Brandon Ingalls',
    'author_email': 'brandon@t4r.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': '',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
