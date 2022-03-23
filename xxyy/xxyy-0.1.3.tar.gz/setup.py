# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xxyy', 'xxyy.requests']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.27,<3.0']

setup_kwargs = {
    'name': 'xxyy',
    'version': '0.1.3',
    'description': '',
    'long_description': None,
    'author': 'laibin',
    'author_email': 'laibin1994@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
