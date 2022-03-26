# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tourscraper']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.4,<9.0.0',
 'python-dotenv>=0.20.0,<0.21.0',
 'selenium>=4.1.3,<5.0.0']

entry_points = \
{'console_scripts': ['tourscraper = tourscraper.app:main']}

setup_kwargs = {
    'name': 'tourscraper',
    'version': '0.1.0',
    'description': 'Web scraper that aggregates tour dates in desired cities',
    'long_description': None,
    'author': 'Dalton Black',
    'author_email': 'projectdjswag@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
