# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['laozi']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.5.3,<0.6.0']

setup_kwargs = {
    'name': 'laozi',
    'version': '1.1.8',
    'description': 'Serialization library outputting a human-readable format',
    'long_description': None,
    'author': 'David Francos Cuartero',
    'author_email': 'me@davidfrancos.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
