# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['example']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.4,<9.0.0']

entry_points = \
{'ops.plugins': ['example_cli_commands = example.cli:cli']}

setup_kwargs = {
    'name': 'ops-plugin-example',
    'version': '0.1.3',
    'description': 'Example OPS Plugin',
    'long_description': None,
    'author': 'Pascal Prins',
    'author_email': 'pascal.prins@foobar-it.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
