# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['redys']
setup_kwargs = {
    'name': 'redys',
    'version': '0.9.7',
    'description': 'A simple redis-like in pure python3, fully asyncio compliant',
    'long_description': "# redys\n\nA simple redis-like in pure python3, fully asyncio/thread/process compliant !\n\n[on pypi/redys](https://pypi.org/project/redys/)\n\n### features\n\n- asyncio compliant\n- client Sync (Client) & Async (AClient)\n- very quick\n- `classics` commands : get/set/delete/keys & incr/decr\n- `sets` commands : sadd/srem\n- `queue` commands : rpush/lpush/rpop/lpop\n- `pubsub` commands : subscribe/unsubscribe/get_event & publish\n- `cache` commands : setex\n- `ping` command ;-)\n- exchange everything that is pickable (except None)\n- raise real python exception in client side\n- minimal code size\n- works well on GAE Standard (2nd generation/py37)\n- unittests are autonomous (it runs a server)\n- just in-memory !\n\n### why ?\n\nRedis is great, but overbloated for my needs. Redys is simple, you can start\nthe server side in an asyncio loop, and clients can interact with a simple\nin-memory db. Really useful when clients are in\nasync/threads/process(workers)/multi-hosts world, to share a unique source of truth.\n\n### nb\n\n- The sync client (`Client`) use threads, so it can't live in the same loop as the server (`Server`). It's better to use it in another thread or process.\n- The async client (`AClient`) can live in the same loop as the server (`Server`), but don't forget to await each methods (which are coroutines in async version)\n- Not fully/concurrency tested. Use at own risk ;-)\n- See [tests](https://github.com/manatlan/redys/blob/master/tests.py) for examples\n\nBTW, I use it in production for one year : and no problems at all !!!! (it works as excepted)\n",
    'author': 'manatlan',
    'author_email': 'manatlan@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/manatlan/redys',
    'py_modules': modules,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
