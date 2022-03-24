# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot', 'nonebot.adapters.qqguild', 'nonebot.adapters.qqguild.api']

package_data = \
{'': ['*']}

install_requires = \
['nonebot2>=2.0.0-beta.1,<3.0.0', 'pydantic>=1.9.0,<2.0.0']

setup_kwargs = {
    'name': 'nonebot-adapter-qqguild',
    'version': '0.1.1',
    'description': 'QQ Guild adapter for nonebot2',
    'long_description': '<p align="center">\n  <a href="https://v2.nonebot.dev/"><img src="https://raw.githubusercontent.com/nonebot/adapter-qqguild/master/website/static/img/logo.png" width="500" alt="nonebot-adapter-onebot"></a>\n</p>\n\n<div align="center">\n\n# NoneBot-Adapter-QQGuild\n\n_✨ QQ 频道协议适配 ✨_\n\n</div>\n',
    'author': 'yanyongyu',
    'author_email': 'yyy@nonebot.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://v2.nonebot.dev/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.3,<4.0.0',
}


setup(**setup_kwargs)
