# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['showmemutil']

package_data = \
{'': ['*']}

install_requires = \
['colorama>=0.4.4,<0.5.0', 'psutil>=5.9.0,<6.0.0']

setup_kwargs = {
    'name': 'showmemutil',
    'version': '0.1.1',
    'description': 'Show memory utilization in the terminal (sort of like htop)',
    'long_description': 'This is me simultaneously learning how to use Poetry and how to publish a Python package to PyPI.\n\n# Installation\n`pip install showmemutil`\n',
    'author': 'Vikram Saraph',
    'author_email': 'vikram.saraph.22@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/vhxs/showmemutil',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
