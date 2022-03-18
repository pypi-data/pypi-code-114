# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['core']

package_data = \
{'': ['*']}

install_requires = \
['paho-mqtt>=1.6.1,<2.0.0']

setup_kwargs = {
    'name': 'policumbent-bob-core',
    'version': '0.1.0.post0',
    'description': 'BOB common files',
    'long_description': None,
    'author': 'Stefano Loscalzo',
    'author_email': 'stefano.loscalzo@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.3,<4.0.0',
}


setup(**setup_kwargs)
