# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['client']

package_data = \
{'': ['*']}

install_requires = \
['pyln-bolt7>=1.0.186,<2.0.0', 'pyln-proto>=0.10.2,<0.11.0']

setup_kwargs = {
    'name': 'pyln-client',
    'version': '0.10.2.post3',
    'description': 'Client library and plugin library for c-lightning',
    'long_description': None,
    'author': 'Christian Decker',
    'author_email': 'decker.christian@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
