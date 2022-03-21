# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aws_sm_import']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'boto3>=1.21.22,<2.0.0',
 'click>=8.0.4,<9.0.0',
 'python-dotenv>=0.19.2,<0.20.0']

entry_points = \
{'console_scripts': ['aws-secrets = aws_sm_import.cli:cli']}

setup_kwargs = {
    'name': 'aws-sm-import',
    'version': '0.1.0',
    'description': 'Import AWS SecretsManager secrets from specific file',
    'long_description': None,
    'author': 'Epsy Engineering',
    'author_email': 'engineering@epsyhealth.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
