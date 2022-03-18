# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sklearn_transformer_extensions',
 'sklearn_transformer_extensions.compose',
 'sklearn_transformer_extensions.preprocessing',
 'sklearn_transformer_extensions.tests']

package_data = \
{'': ['*']}

install_requires = \
['numpy', 'scikit-learn>=1.0.0,<2.0.0']

setup_kwargs = {
    'name': 'sklearn-transformer-extensions',
    'version': '0.2.0',
    'description': 'Some scikit-learn transformer extensions to make using pandas dataframes in scikit-learn pipelines easier.',
    'long_description': None,
    'author': 'Random Geek',
    'author_email': 'randomgeek78@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/randomgeek78/sklearn-transformer-extensions',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
