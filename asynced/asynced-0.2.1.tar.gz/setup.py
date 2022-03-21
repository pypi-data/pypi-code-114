# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['asynced']

package_data = \
{'': ['*']}

extras_require = \
{':python_version < "3.10"': ['typing-extensions>4.1.0']}

setup_kwargs = {
    'name': 'asynced',
    'version': '0.2.1',
    'description': 'Async python for Event-Driven applications',
    'long_description': '# AsyncED\n\n-----\n\n[![PyPI version shields.io](https://img.shields.io/pypi/v/asynced.svg)](https://pypi.python.org/pypi/asynced/)\n[![PyPI pyversions](https://img.shields.io/pypi/pyversions/asynced.svg)](https://pypi.python.org/pypi/asynced/)\n[![PyPI license](https://img.shields.io/pypi/l/asynced.svg)](https://pypi.python.org/pypi/asynced/)\n\n-----\n\n**Async** python for **E**vent-**D**riven applications\n\n## Installation\n\n```bash\npip install asynced\n```\n\n## High-level API\n\n*Coming soon...*\n\n## Low-level API\n\n### Promise\n\nInspired by (but not a clone of) Javascript promises, `asynced.Promise` is a\nthin wrapper around any coroutine. \n\nLike `asyncio.Task`, when a promise is created, the wrapped coroutine will run \nin the background, and can be awaited to get the result or exception. In \naddition, a `Promise` can be "chained" with sync or async functions, producing \nanother `Promise`.\n\nExample:\n\n```python\nimport asyncio\nfrom asynced import Promise\n\n\nasync def formulate_ultimate_question() -> str:\n    await asyncio.sleep(0.25)\n    return (\n        \'What is The Answer to the Ultimate Question of Life, the Universe, \'\n        \'and Everything?\'\n    )\n\n\nasync def compute_answer(question: str):\n    await asyncio.sleep(0.75)\n    return (len(question) >> 1) + 1\n\n\nasync def amain():\n    answer = await Promise(formulate_ultimate_question()).then(compute_answer)\n    print(answer)\n\n\nasyncio.run(amain())\n```\n\n\n\n### Perpetual\n\nWhere asyncio futures are the bridge between low-level events and a\ncoroutines, perpetuals are the bridge between event streams and async\niterators.\n\nIn it\'s essence, a perpetual is an asyncio.Future that can have its result\n(or exception) set multiple times, at least until it is stopped. Besides\na perpetual being awaitable just like a future, it is an async iterator as\nwell.\n\n\n### ensure_future\n\nWrap an async iterable in a perpetual, and automatically starts iterating. \n\nSee [perpetual_drumkit.py](examples/perpetual_drumkit.py) for an example.\n\n~\n\n*More docs and examples coming soon...*\n',
    'author': 'Joren Hammudoglu',
    'author_email': 'jhammudoglu@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jorenham/asynced',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4',
}


setup(**setup_kwargs)
