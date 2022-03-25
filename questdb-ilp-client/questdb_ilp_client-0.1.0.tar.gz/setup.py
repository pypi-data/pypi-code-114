# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['questdb_ilp_client']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'questdb-ilp-client',
    'version': '0.1.0',
    'description': 'A Python3 API for ingesting data into QuestDB through the InfluxDB Line Protocol.',
    'long_description': '\n# Python QuestDB ILP TCP client\n\n## Requirements\n\nThis repository contains a Python 3.9 API for ingesting data into QuestDB through the InfluxDB Line Protocol. \n\nWe use [make](https://www.gnu.org/software/make/) as a CLI to various convenient work developer flows.\n\n### Install Flow\n\nWe require **Python 3.9.\\*, or above** installed in your system, and `pip` needs to be up-to-date:\n\n```shell\n$ python3 --version\n$ Python 3.9.<some-integer>\n$ pip3 install --upgrade pip\n```\n\nNow we can install the project\'s dependencies in a virtual environment and activate it:\n\n```shell\n$ make install-dependencies\n```\n\nOr for development (Required for code quality and test flows):\n\n```shell\n$ make install-dependencies-dev\n```\n\nTo activate the environment:\n\n```shell\n$ poetry shell\n$ echo $SHLVL\n2\n```\n\nTo deactivate the environment:\n\n```shell\n$ exit\n$ echo $SHLVL\n1\n```\n\n### Code Quality Flow (Requires dev dependencies)\n\nFor convenience, we can let standard tools apply standard code formatting; the second command will report\nissues that need to be addressed before using the client in production environments.\n\n```shell\n$ make format-code\n$ make check-code-quality\n```\n\n### Test Flow (Requires dev dependencies)\n\nTo run all tests in the `tests` module:\n\n```shell\n$ make test\n```\n\n### Start/stop QuestDB Docker container Flow\n\nTo start QuestDB:\n\n```shell\n$ make compose-up\n```\n\nThis creates a folder `questdb_root` to store QuestDB\'s table data/metadata, server configuration files,\nand the web UI. \n\n**The Web UI is avaliable at**: [localhost:9000](http://localhost:9000).\n\nLogs can be followed on the terminal:\n\n```shell\n$ docker logs -f questdb\n```\n\nTo stop QuestDB:\n\n```shell\n$ make compose-down\n```\n\nData is available, even when QuestDB is down, in folder `questdb_root`. \n\n## Basic usage\n\n```py\nwith LineTcpSender(HOST, PORT, SIZE) as ls:\n    ls.table("metric_name")\n    ls.symbol("Symbol", "value")\n    ls.column_int("number", 10)\n    ls.column_float("double", 12.23)\n    ls.column_str("string", "born to shine")\n    ls.at_utc_datetime(datetime(2021, 11, 25, 0, 46, 26))\n    ls.flush()\n```\n\nAs an object\n\n```py\nls = LineTcpSender(HOST, PORT, SIZE)\nls.table("metric_name")\nls.symbol("Symbol", "value")\nls.column_int("number", 10)\nls.column_float("double", 12.23)\nls.column_str("string", "born to shine")\nls.at_utc_datetime(datetime(2021, 11, 25, 0, 46, 26))\nls.flush()\n```\n\nMulti-line send\n\n```py\nwith LineTcpSender(HOST, PORT, SIZE) as ls:\n    for i in range(int(1e6)):\n        ls.table("metric_name")\n        ls.column_int("counter", i)\n        ls.at_now()\n    ls.flush()\n```\n\nObject multi-line send\n\n```py\nls = LineTcpSender(HOST, PORT, SIZE)\nfor i in range(int(1e6)):\n    ls.table("metric_name")\n    ls.column_int("counter", i)\n    ls.at_now()\nls.flush()\n```\n\n## Notes\n\n- On file `setup.py`: It is deprecated. To publish a package on PyPi you \n  can [follow this](https://www.brainsorting.com/posts/publish-a-package-on-pypi-using-poetry).\n',
    'author': 'Nathan Scott',
    'author_email': 'nathan@nathanscott.co.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/nsco1/py-questdb-client',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
