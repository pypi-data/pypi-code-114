# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['python_mealie_api',
 'python_mealie_api.client',
 'python_mealie_api.exception',
 'python_mealie_api.model']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0', 'pydantic>=1.9.0,<2.0.0']

setup_kwargs = {
    'name': 'python-mealie-api',
    'version': '0.0.1a0',
    'description': 'A python based mealie client',
    'long_description': None,
    'author': 'Marvin Straathof',
    'author_email': 'marvinstraathof@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
