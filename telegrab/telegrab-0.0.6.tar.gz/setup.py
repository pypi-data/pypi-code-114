# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['telegrab']

package_data = \
{'': ['*']}

install_requires = \
['Telethon>=1.24.0,<2.0.0',
 'click>=8.0.4,<9.0.0',
 'loguru>=0.6.0,<0.7.0',
 'pydantic>=1.9.0,<2.0.0',
 'questionary>=1.10.0,<2.0.0']

entry_points = \
{'console_scripts': ['telegrab = telegrab.__main__:cli']}

setup_kwargs = {
    'name': 'telegrab',
    'version': '0.0.6',
    'description': 'A tool for downloading files from Telegram.',
    'long_description': None,
    'author': 'James Hodgkinson',
    'author_email': 'james@terminaloutcomes.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
