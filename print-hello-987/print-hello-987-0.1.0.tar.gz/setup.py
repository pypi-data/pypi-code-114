# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['print_hello_987']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'print-hello-987',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Alexander Machado',
    'author_email': 'alexander.machado@unternehmertum.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
