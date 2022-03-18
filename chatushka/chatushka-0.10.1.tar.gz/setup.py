# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chatushka',
 'chatushka.bot',
 'chatushka.bot.internal',
 'chatushka.bot.matchers',
 'chatushka.bot.matchers.admin',
 'chatushka.bot.models',
 'chatushka.core',
 'chatushka.core.matchers',
 'chatushka.core.services',
 'chatushka.core.services.mongodb',
 'chatushka.core.transports',
 'chatushka.webui',
 'chatushka.webui.routes']

package_data = \
{'': ['*'], 'chatushka.bot': ['data/*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'aiocron>=1.6,<2.0',
 'click>=8.0.1,<9.0.0',
 'httpx>=0.22.0,<0.23.0',
 'motor>=2.5.0,<3.0.0',
 'pydantic[dotenv]>=1.8.2,<2.0.0']

setup_kwargs = {
    'name': 'chatushka',
    'version': '0.10.1',
    'description': 'Bot that can make your chat explode!',
    'long_description': '# Chatushka bot\n\nБот для чатиков (пока только для телеграмушки)\n\n\n# Usage\n\n## Installation\n\n```shell\npip install chatushka\n```\n\n## Start bot\n\n```shell\npython -m chatushka --token <telegrambotapitoken>\n```\n\n## Test bot\n\n- [x] добавить ботика в чат\n- [x] делегировать боту админские права\n- [x] написать в чатик /help\n\n```shell\npython -m chatushka --token <telegrambotapitoken>\n```\n',
    'author': 'Aleksandr Shpak',
    'author_email': 'shpaker@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/shpaker/chatushka',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
