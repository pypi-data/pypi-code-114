# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['plummet']

package_data = \
{'': ['*']}

install_requires = \
['pendulum>=2.1.2,<3.0.0', 'py-buzz>=3.1.0,<4.0.0']

extras_require = \
{'time-machine': ['time-machine>=2.4.0,<3.0.0']}

setup_kwargs = {
    'name': 'plummet',
    'version': '1.1.0',
    'description': 'Utilities for testing with pendulum timestamps',
    'long_description': '# Plummet\n\nMethods for testing with [pendulum](https://pendulum.eustace.io/) timestamps.\n\nThe most useful method for testing is the [frozen_time()](#frozen_time)\nmethod which allows you to fix a moment in time so that all calls to\n`pendulum.now()` return the provided timestamp.\n\nIt is also possible to freeze timestamps given by `datetime.now()` by\n[installing the time-machine](#feezing_datetime_now) extra dependency.\n\n\n## Methods\n\nHere is a breakdown of the methods provided, what they do, and examples of how to use them\n\n\n### momentize()\n\nThis method is used to turn a variety of different timestamps into pendulum.DateTime instances\nin the UTC timezone.\n\n\n#### Accepted types\n\n* String timestamps (anything that pendulum can parse)\n* datetime.datetime instances\n* pendulum.DateTime instances (that might be in other timezones)\n* None -- returns the current moment in UTC\n\n\n#### Examples\n\nGet the current time in UTC:\n\n```\n>>> momentize()\nDateTime(2021, 11, 17, 21, 15, 0, 20728, tzinfo=Timezone(\'UTC\'))\n```\n\n\nConvert a string timestamp:\n\n```\n>>> momentize("2021-11-17 21:29:00")\nDateTime(2021, 11, 17, 21, 29, 0, tzinfo=Timezone(\'UTC\'))\n```\nSee [pendulum\'s documentation](https://pendulum.eustace.io/docs/#parsing) for more info.\n\n\nConvert a datetime.datetime:\n\n```\n>>> momentize(datetime.datetime(2021, 11, 17, 21, 29, 0))\nDateTime(2021, 11, 17, 21, 29, 0, tzinfo=Timezone(\'UTC\'))\n```\n\n\nIf momentize cannot convert the provided object, it will raise an exception.\n\n\n### moments_match()\n\nThis method is used to compare two possibly different forms of timestamps to make sure they\nare exactly equal. Under the hood, it is using `momentize()` to convert the arguments to\n`pendulum.DateTime` instances and then compares the two.\n\n\n#### Accepted types\n\n* String timestamps (anything that pendulum can parse)\n* datetime.datetime instances\n* pendulum.DateTime instances (that might be in other timezones)\n* None -- compares the current moment in UTC\n\n\n#### Examples\n\nCompare a string to a `datetime.datetime`:\n\n```\n>>> moments_match("2021-11-17 21:41:00", datetime.datetime(2021, 11, 17, 21, 41, 0))\nTrue\n```\n\n\nCompare a `pendulum.DateTime` to a `datetime.datetime` in different timezones:\n\n```\n>>> moments_match(\n...     pendulum.datetime(\n...         2021, 11, 17, 13, 44, 0,\n...         tz="America/Los_Angeles",\n...         ),\n...     datetime.datetime(\n...         2021, 11, 17, 16, 44, 0,\n...         tzinfo=datetime.timezone(datetime.timedelta(hours=-4)),\n...     ),\n... )\n...\nTrue\n```\n\n\n### frozen_time()\n\nThe `frozen_time` method is the main functionality of this package. It allows you to freeze the\ntime returned by `pendulum.now()` (and it\'s relatives) to a given moment.\n\n\n#### Accepted types\n\n* String timestamps (anything that pendulum can parse)\n* datetime.datetime instances\n* pendulum.DateTime instances (that might be in other timezones)\n* None -- freeze at the current moment in UTC\n\n\n#### Examples\n\nFreeze time at a specific moment:\n\n```\n>>> with frozen_time("2021-11-17 22:03:00"):\n...     now = pendulum.now("UTC")\n...     print(now)\n...\n2021-11-17T22:03:00+00:00\n```\n\n\n## Freezing datetime.now()\n\nBy default, the `frozen_time` method only works for `pendulum.now()`. However, if you\ninstall with the extra "time-machine", it is possible to make `frozen_time` work with\n`datetime.now()` as well.\n\n\n### Installing the extra "time-machine" dependency\n\nTo install the extra dependency with pip:\n\n```\n$ pip install plummet[time-machine]\n```\n\nTo install the extra dependency with poetry:\n\n```\n$ poetry add plummet[time-machine]\n```\n\nNow, plummet will freeze `datetime.now()` as well:\n\n```\n>>> with frozen_time("2021-11-17 22:03:00"):\n...     pendulum_now = pendulum.now("UTC")\n...     datetime_now = datetime.now(tz=timezone.utc)\n...     print(pendulum_now)\n...     print(datetime_now)\n...\n2021-11-17T22:03:00+00:00\n2021-11-17 22:03:00+00:00\n```\n\n\n## Testing\n\nTo run the testing suite:\n\n```\n$ make test\n```\n\n\nTo run the full set of quality checks:\n\n```\n$ make qa\n```\n',
    'author': 'Tucker Beck',
    'author_email': 'tucker.beck@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/dusktreader/plummet',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
