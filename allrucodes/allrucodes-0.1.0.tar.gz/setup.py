# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['allrucodes']

package_data = \
{'': ['*'], 'allrucodes': ['data/*']}

install_requires = \
['fuzzywuzzy>=0.18.0,<0.19.0', 'numpy>=1.22.3,<2.0.0']

setup_kwargs = {
    'name': 'allrucodes',
    'version': '0.1.0',
    'description': 'Python package with a collection of official all-russian codes catalogs.',
    'long_description': None,
    'author': 'Alexey Naydyonov',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
