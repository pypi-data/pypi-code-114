# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['prometheus_query_builder']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'prometheus-query-builder',
    'version': '0.1.4',
    'description': 'Package for generation Prometheus Query Language queries.',
    'long_description': 'prometheus-query-builder\n========================\n\n[![PyPI version](https://badge.fury.io/py/prometheus-query-builder.svg)](https://badge.fury.io/py/prometheus-query-builder)\n[![PyPI version](https://img.shields.io/pypi/pyversions/prometheus-query-builder.svg)](https://pypi.org/project/prometheus-query-builder/)\n[![MIT licensed](https://img.shields.io/pypi/l/prometheus-query-builder)](./LICENSE)\n\nPackage for generation Prometheus Query Language queries.\n\n## Installation\n\nUse pip for to install from Pypi:\n\n```commandline\npip install prometheus-query-builder\n```\n\nThe package is still in alpha development, so better pin version in your requirements:\n\n```\nprometheus-query-builder==0.1\n```\n\n## Usage\n\nSee usage examples in [tests](./tests) directory.\n\n## TODO\n\n- Subqueries - https://prometheus.io/docs/prometheus/latest/querying/basics/#subquery\n- Functions - https://prometheus.io/docs/prometheus/latest/querying/basics/#functions\n',
    'author': 'Michail Tsyganov',
    'author_email': 'tsyganov.michail@yandex.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/m-chrome/prometheus-query-builder',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
