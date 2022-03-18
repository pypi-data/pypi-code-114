# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['stefan_utils']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.22.3,<2.0.0',
 'pandas>=1.4.1,<2.0.0',
 'pyarrow>=7.0.0,<8.0.0',
 'python-json-logger>=2.0.2,<3.0.0']

setup_kwargs = {
    'name': 'stefan-utils',
    'version': '0.0.2',
    'description': '',
    'long_description': None,
    'author': 'Stefan Bader',
    'author_email': 'baderstefan@gmx.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
