# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['td_connect']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0',
 'fsspec[gcs]>=2021.11.1,<2022.0.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'ready-logger>=0.1.0,<0.2.0',
 'requests>=2.26.0,<3.0.0',
 'websockets>=10.1,<11.0']

setup_kwargs = {
    'name': 'td-connect',
    'version': '0.1.1',
    'description': 'Authentication manager for TD Ameritrade REST APIs.',
    'long_description': None,
    'author': 'Dan Kelleher',
    'author_email': 'dan@danklabs.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
