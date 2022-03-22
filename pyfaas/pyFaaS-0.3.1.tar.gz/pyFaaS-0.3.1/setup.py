# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['faas']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyfaas',
    'version': '0.3.1',
    'description': 'Python client for Fluent as a Server',
    'long_description': None,
    'author': 'AlwinW',
    'author_email': '16846521+alwinw@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
