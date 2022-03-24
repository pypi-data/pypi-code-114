# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pybotx_fsm']

package_data = \
{'': ['*']}

install_requires = \
['pybotx>=0.32.0,<0.33.0']

setup_kwargs = {
    'name': 'pybotx-fsm',
    'version': '0.3.0',
    'description': 'FSM middleware for using with pybotx',
    'long_description': None,
    'author': None,
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
