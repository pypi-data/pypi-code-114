# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['messages_sender']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.0.3,<4.0.0', 'Telethon>=1.24.0,<2.0.0']

setup_kwargs = {
    'name': 'messages-sender',
    'version': '0.1.2',
    'description': 'Message sender is a library which create a message to send from a python dictionnary and a Jinja template and send it by the method of your choice.',
    'long_description': None,
    'author': 'Ermite28',
    'author_email': 'benoitdewitte28@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
