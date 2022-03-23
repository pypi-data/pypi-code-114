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
    'version': '0.0.2',
    'description': 'An asynchronous Redis-based Socket.IO emitter for Python',
    'long_description': '# Socket.IO Redis Emitter\n\nThis is an asynchronous Redis-based [Socket.IO emitter](https://socket.io/docs/v4/emitting-events/) for Python.\n\n## Installation\n\n```bash\npip install socket.io-redis-emitter\n# or\npoetry add socket.io-redis-emitter\n```\n\n## Features\n\n- High quality, typed and modern Python codebase\n- Clean, concise and Pythonic API\n- Uses [aioredis](https://aioredis.readthedocs.io/en/latest/) as a Redis client\n- Supports namespaces, rooms and regular Socket.IO message emitting\n\n```python\nfrom aioredis import Redis\nfrom socketio_emitter import Emitter\n\nclient = Redis(...)\nemitter = Emitter(client=client)\n\nwith emitter.namespace("/nsp") as nsp:\n    with nsp.rooms("room1", "room2") as clients:\n        await clients.emit("machineStatus", {"status": "ok"})\n```\n\n- Remote requests to join, leave rooms or to disconnect \n\n```python\nfrom aioredis import Redis\nfrom socketio_emitter import Emitter\n\nclient = Redis(...)\nemitter = Emitter(client=client)\n\nwith emitter.namespace("/nsp") as nsp:\n    with nsp.rooms("room1", "room2") as clients:\n        await clients.join("room3")\n        # await clients.leave("room3")\n        # await clients.disconnect()\n```',
    'author': 'Roman Glushko',
    'author_email': 'roman.glushko.m@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/roma-glushko/socket.io-redis-emitter',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
