# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['aryan',
 'aryan.contact',
 'aryan.event',
 'aryan.event.events',
 'aryan.message',
 'aryan.message.code',
 'aryan.message.data']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0',
 'click>=8.0.4,<9.0.0',
 'loguru>=0.5.3,<0.6.0',
 'pydantic>=1.9.0,<2.0.0']

setup_kwargs = {
    'name': 'aryan',
    'version': '0.1.0',
    'description': 'A small package',
    'long_description': '# Aryan\n\n## 简介\n简单介绍一下本项目有何优点以及为何值得使用  \n* 本项目~~写的很烂~~源码通俗易懂 方便阅读与使用\n* 作者（也就是我）单纯 善良 可爱 迷人 友善...（省略一万字）\n\n## 安装\n``pip install aryan``  \n或使用包管理工具poetry  \n``poetry add aryan``\n\n## 部署\n### 配置mirai-api-http（mah）\n本项目要求使用mah v2.0 并开启http与websocket（别问 问就是我懒\n\n### 配置你的python文件\n```python\nimport asyncio\nfrom aryan import Mirai, MiraiSession, BotConfiguration, Bot\nfrom aryan import GroupMessage, GlobalEventChannel\n\napp = Mirai(\n    MiraiSession(\n        verify_key="verifyKey",  # 配置mirai-api-http时保存的verifyKey\n        host="localhost:8080",  # mah存在的地址\n    ),\n    loop=asyncio.new_event_loop(),\n    bots=[\n        Bot(BotConfiguration(account=...)),\n        Bot(BotConfiguration(account=...))\n    ]\n)\n\n\nasync def main(event: GroupMessage):\n    print("received event:", type(event))\n\n\nGlobalEventChannel.INSTANCE.subscribeAlways(GroupMessage, main)\n\napp.launch_blocking()\n```\n\n查看更多用法可以参考[这里](https://github.com/qianmo527/Aryan/blob/master/example.py)\n\n如果在使用本项目中遇到任何问题，请不要生气，不要砸电脑，可以提个issue|pr或者加入qq交流群~~喷项目~~交流\n\n[qq交流群](https://jq.qq.com/?_wv=1027&k=BUU9hkkN)\n',
    'author': 'qianmo527',
    'author_email': '2816661524@qq.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
