# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['boostpi']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['boostpi = boostpi.main:main']}

setup_kwargs = {
    'name': 'boostpi',
    'version': '0.1.6',
    'description': 'A simple overclocking configuration tool for Raspberry Pi',
    'long_description': '# boostpi\nA simple overclocking configuration tool for the raspberry pi built with python\n\n\n[link to a helpful guide while developing](https://medium.com/nerd-for-tech/how-to-build-and-distribute-a-cli-tool-with-python-537ae41d9d78)\n',
    'author': 'Alexander Swensen',
    'author_email': 'alex.swensen@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/AlexSwensen/boostpi',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
