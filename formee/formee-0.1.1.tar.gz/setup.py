# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['formee', 'formee.auth', 'formee.formTools']

package_data = \
{'': ['*']}

install_requires = \
['PyInquirer>=1.0.3,<2.0.0',
 'PyYAML>=6.0,<7.0',
 'aiohttp>=3.8.1,<4.0.0',
 'gql>=3.1.0,<4.0.0',
 'pyfiglet>=0.8.post1,<0.9',
 'python-dotenv>=0.20.0,<0.21.0',
 'requests>=2.27.1,<3.0.0',
 'rich>=12.0.1,<13.0.0']

setup_kwargs = {
    'name': 'formee',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Arpan Pandey',
    'author_email': 'arpanpandey.aps@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
