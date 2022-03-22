# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['glacier']

package_data = \
{'': ['*']}

install_requires = \
['click-completion>=0.5.2,<0.6.0',
 'click-help-colors>=0.9.1,<0.10.0',
 'click>=8.0.4,<9.0.0',
 'importlib-metadata>=4.11.3,<5.0.0',
 'typing-extensions>=4.1.1,<5.0.0']

setup_kwargs = {
    'name': 'glacier',
    'version': '0.3.4',
    'description': '',
    'long_description': None,
    'author': 'Hiroki Konishi',
    'author_email': 'relastle@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
