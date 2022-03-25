# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['snakesay']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'snakesay',
    'version': '0.9.0',
    'description': 'speaking snake',
    'long_description': None,
    'author': 'PythonAnywhere Developers',
    'author_email': 'developers@pythonanywhere.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
