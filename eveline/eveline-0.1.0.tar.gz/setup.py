# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['eveline']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.0.3,<4.0.0']

setup_kwargs = {
    'name': 'eveline',
    'version': '0.1.0',
    'description': 'Placeholder for eveline protocol',
    'long_description': None,
    'author': 'Stanislav',
    'author_email': 'me@h3xco.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
