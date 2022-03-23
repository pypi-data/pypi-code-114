# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['archimedes',
 'archimedes.data',
 'archimedes.organizer',
 'archimedes.testdata',
 'archimedes.utils']

package_data = \
{'': ['*'], 'archimedes.testdata': ['datasets/*']}

install_requires = \
['dynaconf>=3.1.2',
 'matplotlib>=3.2.2',
 'mlflow>=1.12.0',
 'msal-extensions>=1.0.0,<2.0.0',
 'msal>=1.10.0,<2.0.0',
 'pandas>=1.0.5',
 'prefect>=1.0.0,<2.0.0',
 'psycopg2-binary>=2.8.6',
 'records>=0.5.3',
 'requests>=2.27.0']

setup_kwargs = {
    'name': 'archimedes-python-client',
    'version': '3.8.0',
    'description': 'The Python library for Archimedes',
    'long_description': None,
    'author': 'Optimeering AS',
    'author_email': 'dev@optimeering.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
