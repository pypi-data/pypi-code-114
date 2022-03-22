# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pytest_metadata', 'pytest_metadata.ci']

package_data = \
{'': ['*']}

install_requires = \
['pytest>=7.1.1,<8.0.0']

setup_kwargs = {
    'name': 'pytest-metadata',
    'version': '2.0.0',
    'description': 'pytest plugin for test session metadata',
    'long_description': None,
    'author': 'Dave Hunt',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
