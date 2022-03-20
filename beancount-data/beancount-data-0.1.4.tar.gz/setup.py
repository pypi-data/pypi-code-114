# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['beancount_data']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.9.0,<2.0.0']

setup_kwargs = {
    'name': 'beancount-data',
    'version': '0.1.4',
    'description': 'Pydantic data models for exporting Beancount data',
    'long_description': None,
    'author': 'Fang-Pen Lin',
    'author_email': 'fangpen@launchplatform.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
