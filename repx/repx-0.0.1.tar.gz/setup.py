# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['repx']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['repx = repx.main:cmdline_entry_point']}

setup_kwargs = {
    'name': 'repx',
    'version': '0.0.1',
    'description': 'Search and replace in files with regular expressions',
    'long_description': None,
    'author': 'Malthe Jørgensen',
    'author_email': 'malthe.jorgensen@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/malthejorgensen/repx',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
