# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zora', 'zora.core', 'zora.indexer', 'zora.v3']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0',
 'asyncio>=3.4.3,<4.0.0',
 'pandas>=1.4.1,<2.0.0',
 'requests>=2.27.1,<3.0.0']

setup_kwargs = {
    'name': 'zora',
    'version': '0.2.1',
    'description': '',
    'long_description': None,
    'author': 'franalgaba',
    'author_email': 'f.algaba@outlook.es',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
