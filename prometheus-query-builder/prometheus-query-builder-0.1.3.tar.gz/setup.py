# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['prometheus_query_builder']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'prometheus-query-builder',
    'version': '0.1.3',
    'description': 'Package for generation Prometheus Query Language queries.',
    'long_description': 'prometheus-query-builder\n########################\n\nPackage for generation Prometheus Query Language queries.\n\nInstallation\n************\n\nUse pip for to install from Pypi: ::\n\n    pip install prometheus-query-builder\n\nThe package is still in alpha development, so better pin version in your requirements: ::\n\n    prometheus-query-builder==0.1.0\n\nUsage\n*****\n\nSee usage examples in tests directory.\n\nTODO\n****\n\nSupport PromQL:\n\n- Subqueries - https://prometheus.io/docs/prometheus/latest/querying/basics/#subquery\n- Functions - https://prometheus.io/docs/prometheus/latest/querying/basics/#functions\n',
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
