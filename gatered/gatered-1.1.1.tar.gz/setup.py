# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gatered']

package_data = \
{'': ['*']}

install_requires = \
['aiometer>=0.3.0', 'httpx[http2]>=0.21.0']

setup_kwargs = {
    'name': 'gatered',
    'version': '1.1.1',
    'description': 'Reddit Gateway API Library',
    'long_description': '# GateRed\n\nA utils for interacting with Reddit Gateway API (Web API), w/ pushshift historical posts support.\n\n[![Latest Version](https://img.shields.io/pypi/v/gatered.svg)](https://pypi.python.org/pypi/gatered)\n[![Supported Python Versions](https://img.shields.io/pypi/pyversions/gatered)](https://pypi.python.org/pypi/gatered)\n[![CI](https://github.com/countertek/gatered/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/countertek/gatered/actions/workflows/ci.yml)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![GitHub license](https://img.shields.io/github/license/countertek/gatered)](https://github.com/countertek/gatered/blob/main/LICENSE)\n\n**[Documentation](https://countertek.github.io/gatered)**\n\n## Why this library?\n\nAlthough Reddit has developer APIs and there are existing libraries (e.g. praw) to interact with reddit, there are still several drawbacks in terms of collecting data:\n\n- An API key is needed to collect data.\n- Rate limit is based on API keys.\n- Some fields are missing using developer APIs.\n\nTherefore, **gatered** exists just to counter this problem. It directly access Reddit\'s web API to get the whole information. No authentication is needed, and it supports proxy provided by [httpx](https://www.python-httpx.org/advanced/#http-proxying).\n\n## Install\n\nYou can install this library easily from pypi:\n\n```bash\n# with pip\npip install gatered\n\n# with poetry\npoetry add gatered\n```\n\n## Using\n\nThe library provides easy functions to get start fast:\n- `gatered.func.get_post_comments`\n- `gatered.func.get_posts`\n- `gatered.func.get_comments`\n- `gatered.func.get_pushshift_posts`\n\nAlternatively you can directly use `gatered.client.Client` and `gatered.pushshift.PushShiftAPI` classes as your base to implement your own logics.\n\nErrors can be handled by importing either `gatered.RequestError` or `gatered.HTTPStatusError`, see [httpx exceptions](https://www.python-httpx.org/exceptions/) to learn more.\n\nSee [`examples/`](https://github.com/countertek/gatered/tree/main/examples/) for more examples.\n\n## License\n\nCopyright 2022 countertek\n\nLicensed under the Apache License, Version 2.0 (the "License");\nyou may not use this file except in compliance with the License.\nYou may obtain a copy of the License at\n\n    http://www.apache.org/licenses/LICENSE-2.0\n\nUnless required by applicable law or agreed to in writing, software\ndistributed under the License is distributed on an "AS IS" BASIS,\nWITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\nSee the License for the specific language governing permissions and\nlimitations under the License.\n',
    'author': 'DaRekaze',
    'author_email': 'darekaze@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/CounterTek/gatered',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
