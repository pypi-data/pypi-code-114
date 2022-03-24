# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rygforms']

package_data = \
{'': ['*'], 'rygforms': ['templates/*']}

install_requires = \
['authlib>=1.0.0,<2.0.0',
 'click>=8.0.3,<9.0.0',
 'flask>=2.0.3,<3.0.0',
 'gunicorn>=20.1.0,<21.0.0',
 'itsdangerous>=2.1.2,<3.0.0',
 'python-dotenv>=0.15.0,<0.16.0',
 'requests>=2.25.1,<3.0.0']

setup_kwargs = {
    'name': 'rygforms',
    'version': '0.5.8',
    'description': 'OAuth2 Login for Typeform and Tripetto',
    'long_description': None,
    'author': 'Stefano Pigozzi',
    'author_email': 'me@steffo.eu',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
