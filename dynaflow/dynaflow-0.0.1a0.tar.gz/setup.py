# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dynaflow']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.4,<9.0.0', 'mlflow>=1.24.0,<2.0.0', 'pynamodb>=5.2.1,<6.0.0']

entry_points = \
{'console_scripts': ['dynaflow = dynaflow.cli:dynaflow'],
 'mlflow.model_registry_store': ['dynamodb = '
                                 'dynaflow.model_registry:DynamodbModelStore'],
 'mlflow.tracking_store': ['dynamodb = '
                           'dynaflow.tracking_store:DynamodbTrackingStore']}

setup_kwargs = {
    'name': 'dynaflow',
    'version': '0.0.1a0',
    'description': 'AWS Dynamodb backend tracking store for MLFlow',
    'long_description': None,
    'author': 'ArrichM',
    'author_email': 'maximilianjakob.arrich@student.unisg.ch',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
