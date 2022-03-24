# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['basilo']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'basilo',
    'version': '0.0.0',
    'description': 'An opinionated data manipulation Python package.',
    'long_description': None,
    'author': 'chris pryer',
    'author_email': 'christophpryer@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
