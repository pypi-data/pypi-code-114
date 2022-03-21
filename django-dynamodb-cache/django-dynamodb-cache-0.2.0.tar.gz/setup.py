# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_dynamodb_cache',
 'django_dynamodb_cache.encode',
 'django_dynamodb_cache.management',
 'django_dynamodb_cache.management.commands']

package_data = \
{'': ['*']}

install_requires = \
['Django>=3.2,<4.0', 'boto3>=1.21.9,<2.0.0', 'botocore>=1.24.9,<2.0.0']

setup_kwargs = {
    'name': 'django-dynamodb-cache',
    'version': '0.2.0',
    'description': '',
    'long_description': '# django-dynamodb-cache\n\nFast, safe, cost-effective DynamoDB cache backend for Django\n\n<p align="center">\n<a href="https://github.com/xncbf/django-dynamodb-cache/actions/workflows/tests.yml" target="_blank">\n    <img src="https://github.com/xncbf/django-dynamodb-cache/actions/workflows/tests.yml/badge.svg" alt="Tests">\n</a>\n<a href="https://codecov.io/gh/xncbf/django-dynamodb-cache" target="_blank">\n    <img src="https://img.shields.io/codecov/c/github/xncbf/django-dynamodb-cache?color=%2334D058" alt="Coverage">\n</a>\n<a href="https://pypi.org/project/django-dynamodb-cache" target="_blank">\n    <img src="https://img.shields.io/pypi/v/django-dynamodb-cache?color=%2334D058&label=pypi%20package" alt="Package version">\n</a>\n<a href="https://pypi.org/project/django-dynamodb-cache" target="_blank">\n    <img src="https://img.shields.io/pypi/pyversions/django-dynamodb-cache.svg?color=%2334D058" alt="Supported Python versions">\n</a>\n<a href="https://pypi.org/project/django-dynamodb-cache" target="_blank">\n    <img src="https://img.shields.io/pypi/djversions/django-dynamodb-cache.svg" alt="Supported django versions">\n</a>\n<a href="http://pypi.python.org/pypi/django-dynamodb-cache/blob/main/LICENSE" target="_blank">\n    <img src="https://img.shields.io/github/license/xncbf/django-dynamodb-cache?color=gr" alt="License">\n</a>\n</p>\n\n- [django-dynamodb-cache](#django-dynamodb-cache)\n  - [Installation](#installation)\n  - [Setup on Django](#setup-on-django)\n  - [Aws credentials](#aws-credentials)\n  - [Create cache table command](#create-cache-table-command)\n  - [How to contribute](#how-to-contribute)\n\n## Installation\n\n```sh\npip install django-dynamodb-cache\n```\n\n## Setup on Django\n\nOn Django `settings.py`\n\n```python\n\n\nINSTALLED_APPS = [\n    ...\n    "django_dynamodb_cache"\n]\n\nCACHES = {\n    "default": {\n        "BACKEND": "django_dynamodb_cache.backend.DjangoCacheBackend",\n        "LOCATION": "table-name",  # default: django-dynamodb-cache\n        "TIMEOUT": 120,  # seconds\n        "KEY_PREFIX": "django_dynamodb_cache",\n        "VERSION": 1,\n        "KEY_FUNCTION": "path.to.function",  # f"{prefix}:{key}:{version}"\n        "OPTIONS": {\n            "aws_region_name": "us-east-1",\n            "read_capacity_units": 1,\n            "write_capacity_units": 1,\n            "encode": "django_dynamodb_cache.encode.PickleEncode"\n        }\n    }\n}\n```\n\n## Aws credentials\n\nThe same method as configuring-credentials provided in the boto3 documentation is used.\n<https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#configuring-credentials>\n\n## Create cache table command\n\nRun manage command to create cache table on Dynamodb before using\n\n```zsh\npython manage.py createcachetable\n```\n\n## How to contribute\n\nThis project is welcome to contributions!\n\nPlease submit an issue ticket before submitting a patch.\n\nPull requests are merged into the main branch and should always remain available.\n\nAfter passing all test code, it is reviewed and merged.\n',
    'author': 'xncbf',
    'author_email': 'xncbf12@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/xncbf/django-dynamodb-cache',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
