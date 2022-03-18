# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tele-pyro', 'tele-pyro.utils']

package_data = \
{'': ['*']}

install_requires = \
['Pyrogram>=1.4.8,<2.0.0', 'Telethon>=1.24.0,<2.0.0', 'TgCrypto>=1.2.3,<2.0.0']

entry_points = \
{'console_scripts': ['tele-pyro = __main__:main']}

setup_kwargs = {
    'name': 'tele-pyro',
    'version': '0.1.1.5',
    'description': 'Script for convert telethon sesession file to pyrogram session file',
    'long_description': '<h1>Telethon to Pyrogram</h1>\nPyPi\nIsort\nTest\nLint\nlicense\nGitter\nDownloads\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n<h4>Simple script for convert telethon session file to pyrogram session file</h4>\n\n<h3>For use:</h3>\n\n1. Clone repo `git clone git@github.com:semenovsd/Telethon-To-Pyrogram.git`\n2. Install Telethon and Pyrogram `poetry install` or user pip `pip install Telethon Pyrogram`\n3. Run convertor.py `python convertor.py` and follow instructions\n',
    'author': 'Stanislav Semenov',
    'author_email': 'semenov_sd@bk.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/semenovsd/Telethon-To-Pyrogram',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '==3.9.4',
}


setup(**setup_kwargs)
