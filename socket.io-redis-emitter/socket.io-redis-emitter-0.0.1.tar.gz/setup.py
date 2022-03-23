# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['socketio_emitter']

package_data = \
{'': ['*']}

install_requires = \
['aioredis>=2.0.1,<3.0.0', 'msgpack>=1.0.3,<2.0.0', 'pydantic>=1.9.0,<2.0.0']

setup_kwargs = {
    'name': 'socket.io-redis-emitter',
    'version': '0.0.1',
    'description': '',
    'long_description': None,
    'author': 'Roman Glushko',
    'author_email': 'roman.glushko.m@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
