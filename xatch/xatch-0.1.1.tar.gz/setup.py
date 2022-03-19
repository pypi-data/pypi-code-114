# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xatch']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'xatch',
    'version': '0.1.1',
    'description': 'Basic Python libraries and tools used for various frameworks.',
    'long_description': 'Welcome to the Xatch Project!\n\nThe project is currently under development and is not ready for use in\nproduction.\n\nThe Xatch Projects are a collection of Python libraries and tools used as the\nmost basic level for various frameworks.\n',
    'author': 'Medardo Antonio Rodriguez',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
