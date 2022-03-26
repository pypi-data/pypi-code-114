# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ohmypika']

package_data = \
{'': ['*']}

install_requires = \
['PyPika>=0.48.9,<0.49.0', 'omymodels>=0.11.0,<0.12.0']

setup_kwargs = {
    'name': 'ohmypika',
    'version': '0.1.0',
    'description': 'oh-my-pika is not an ORM, but it can give Python developers a better SQL writing experience',
    'long_description': '',
    'author': 'so1n',
    'author_email': 'qaz6803609@163.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/so1n/oh-my-pika',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
