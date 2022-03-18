# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['testing']

package_data = \
{'': ['*']}

install_requires = \
['Flask>=2.0.3,<3.0.0',
 'cheroot>=8.6.0,<9.0.0',
 'ephemeral-port-reserve>=1.1.4,<2.0.0',
 'jsonschema>=4.4.0,<5.0.0',
 'psutil>=5.9.0,<6.0.0',
 'psycopg2-binary>=2.9.3,<3.0.0',
 'pyln-client @ ../pyln-client',
 'pytest>=7.0.1,<8.0.0',
 'python-bitcoinlib>=0.11.0,<0.12.0']

setup_kwargs = {
    'name': 'pyln-testing',
    'version': '0.10.2',
    'description': 'Test your c-lightning integration, plugins or whatever you want',
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
