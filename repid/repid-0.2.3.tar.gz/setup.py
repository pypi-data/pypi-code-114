# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['repid']

package_data = \
{'': ['*']}

install_requires = \
['orjson>=3.6.7,<4.0.0', 'redis>=4.2.0,<5.0.0']

setup_kwargs = {
    'name': 'repid',
    'version': '0.2.3',
    'description': 'Async Redis queue for Python.',
    'long_description': '# repid\n\n[![PyPI version](https://img.shields.io/pypi/v/repid.svg)](https://pypi.org/project/repid/)\n[![codecov](https://codecov.io/gh/aleksul/repid/branch/main/graph/badge.svg?token=IP3Z1VXB1G)](https://codecov.io/gh/aleksul/repid)\n[![Tests](https://github.com/aleksul/repid/actions/workflows/tests.yaml/badge.svg)](https://github.com/aleksul/repid/actions/workflows/tests.yaml)\n[![PyPI pyversions](https://img.shields.io/pypi/pyversions/repid.svg)](https://pypi.python.org/pypi/repid/)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n**Repid** is a job queuing library for Python with focus on simplicity.\n\n```bash\npip install repid\n```\n\n## Quickstart\n\nMake sure Redis is running, then start 2 processes/containers with code as below.\n\nOn producer side:\n\n```python\nimport repid\nimport asyncio\nfrom redis.asyncio import Redis\n\nmyredis = Redis(host="localhost", port=6379, db=0, decode_responses=True)\nmyrepid = repid.Repid(myredis)\n\nasync def main():\n    await myrepid.enqueue("my_first_job")\n\nasyncio.run(main())\n```\n\nOn consumer side:\n\n```python\nimport repid\nimport asyncio\nfrom redis.asyncio import Redis\n\nmyredis = Redis(host="localhost", port=6379, db=0, decode_responses=True)\nmyworker = repid.Worker(myredis)\n\n@myworker.actor()\nasync def my_first_job():\n    return "Hello Repid!"\n\nasyncio.run(myworker.run_forever())\n```\n\nCheck out [user guide] to learn more!\n\n## License\n\n**Repid** is licensed under the MIT. Please see [License.md] for more information.\n\n[License.md]: https://github.com/aleksul/repid/blob/master/LICENSE\n[user guide]: http://aleksul.github.io/repid\n',
    'author': 'aleksul',
    'author_email': 'aleksandrsulimov@bk.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/aleksul/repid',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
