# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['clockwork_tools']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.27.1,<3.0.0']

setup_kwargs = {
    'name': 'clockwork-tools',
    'version': '0.1.0',
    'description': 'Tools to interact with Clockwork cluster',
    'long_description': None,
    'author': 'Mila team',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
