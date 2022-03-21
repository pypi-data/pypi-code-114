# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['botx',
 'botx.bot',
 'botx.bot.api',
 'botx.bot.api.responses',
 'botx.bot.middlewares',
 'botx.client',
 'botx.client.bots_api',
 'botx.client.chats_api',
 'botx.client.events_api',
 'botx.client.exceptions',
 'botx.client.files_api',
 'botx.client.notifications_api',
 'botx.client.smartapps_api',
 'botx.client.stickers_api',
 'botx.client.users_api',
 'botx.models',
 'botx.models.message',
 'botx.models.system_events']

package_data = \
{'': ['*']}

install_requires = \
['aiofiles>=0.7.0,<0.9.0',
 'httpx>=0.18.0,<0.22.0',
 'loguru>=0.6.0,<0.7.0',
 'mypy-extensions>=0.2.0,<0.5.0',
 'pydantic>=1.6.0,<1.9.0',
 'typing-extensions>=3.7.4,<5.0.0']

setup_kwargs = {
    'name': 'botx',
    'version': '0.30.0',
    'description': 'A python library for interacting with eXpress BotX API',
    'long_description': None,
    'author': 'Sidnev Nikolay',
    'author_email': 'nsidnev@ccsteam.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ExpressApp/pybotx',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
