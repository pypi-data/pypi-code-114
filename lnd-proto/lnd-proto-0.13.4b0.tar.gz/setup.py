# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lnd_proto']

package_data = \
{'': ['*']}

install_requires = \
['grpcio>=1.43.0,<2.0.0', 'protobuf>=3.19.1,<4.0.0']

setup_kwargs = {
    'name': 'lnd-proto',
    'version': '0.13.4b0',
    'description': 'Protobuf generated libraries for LND',
    'long_description': None,
    'author': 'Hashbeam',
    'author_email': 'hashbeam@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/hashbeam/lnd-proto',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.0,<4.0.0',
}


setup(**setup_kwargs)
