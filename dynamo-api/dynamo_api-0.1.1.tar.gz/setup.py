# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dynamo_api']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.17.75,<2.0.0']

setup_kwargs = {
    'name': 'dynamo-api',
    'version': '0.1.1',
    'description': 'Package to perform simple operations on AWS DynamoDB for personal use and playing around with Github Actions',
    'long_description': None,
    'author': 'Justin Lei',
    'author_email': 'jun.lei@mail.mcgill.ca',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
