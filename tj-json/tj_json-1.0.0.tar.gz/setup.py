# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tjson']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'tj-json',
    'version': '1.0.0',
    'description': 'Accesss utility for JSON-shaped Python objects',
    'long_description': None,
    'author': 'Filip Sufitchi',
    'author_email': 'fsufitchi@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
