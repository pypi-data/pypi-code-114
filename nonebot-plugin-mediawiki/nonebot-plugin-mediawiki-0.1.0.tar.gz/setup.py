# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_mediawiki']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<3.9.0',
 'nonebot-adapter-onebot>=2.0.0b1,<2.1.0',
 'nonebot2>=2.0.0b2,<2.1.0']

setup_kwargs = {
    'name': 'nonebot-plugin-mediawiki',
    'version': '0.1.0',
    'description': 'nonebot2 mediawiki 查询插件',
    'long_description': '# nonebot-plugin-mediawiki\n适用于 nonebot2 的 MediaWiki 查询插件\n\n本项目是 [Flandre](https://github.com/KoishiStudio/Flandre) 的一部分，经简单修改成为独立插件发布\n\n使用方法位于插件源代码内，也可以使用 [nonebot-plugin-help](https://github.com/XZhouQD/nonebot-plugin-help) 在运行时查询帮助\n',
    'author': 'KoishiChan',
    'author_email': '68314080+KoishiStudio@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/KoishiStudio/nonebot-plugin-mediawiki',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
