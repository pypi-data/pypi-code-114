# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_setu_now']

package_data = \
{'': ['*']}

install_requires = \
['anyio>=3.5.0,<4.0.0',
 'httpx>=0.18.0,<1.0.0',
 'nonebot-adapter-onebot>=2.0.0-beta.1,<3.0.0',
 'nonebot-plugin-apscheduler>=0.1.2,<0.2.0',
 'nonebot2>=2.0.0-beta.1,<3.0.0',
 'pydantic>=1.5.0,<2.0.0',
 'webdav4>=0.9.3,<0.10.0']

setup_kwargs = {
    'name': 'nonebot-plugin-setu-now',
    'version': '0.1.0',
    'description': '另一个色图插件',
    'long_description': '# nonebot-plugin-setu-now\n\n- 另一个色图插件\n- 根据别人的改了亿点点\n- 现在可以色图保存到 `WebDAV` 服务器中来节省服务器空间(可选)\n- 采用**即时下载**并保存的方式来扩充*自己*色图库(可选)\n- 支持私聊获取~~特殊~~色图\n- 对临时聊天不生效\n\n## 安装配置\n\n```sh\npip install -U nonebot-plugin-setu-now\n```\n\n### .env 默认配置 (爱看不看，不看也能用)\n\n```ini\nsetu_cd=60\nsetu_save=\nsetu_path=\nsetu_porxy=\nsetu_reverse_proxy=\nsetu_dav_url=\nsetu_dav_username=\nsetu_dav_password=\nsetu_send_info_message=\nsetu_send_custom_message_path=\n```\n\n- `setu_cd` CD(单位秒) 可选 默认`60`秒\n- `setu_save` 保存模式 可选 `webdav`(保存到 webdav 服务器中) 或 `local`(本地) 或 留空,不保存\n- `setu_path` 保存路径 可选 当选择保存模式时可按需填写, 可不填使用默认\n  - webdav 可选 默认`/setu` `/setur18`\n  - 本地 可选 默认`./data/setu` `./data/setur18`\n- `setu_porxy` 代理地址 可选 当 pixiv 反向代理不能使用时可自定义\n- `setu_reverse_proxy` pixiv 反向代理 可选 默认 `i.pixiv.re`\n- webdav 设置 当选择保存保存模式为 `webdav` 时必须填写\n  - `setu_dav_username` 用户名\n  - `setu_dav_password` 密码\n  - `setu_dav_url` webdav 服务器地址\n- `setu_send_info_message` 是否发送图片信息 可选 默认 `ture` 填写 `false` 可关闭\n- `setu_send_custom_message_path` 自定义发送消息路径 可选 当填写路径时候开启 可以为相对路径\n  - 文件应该为 `json` 格式如下\n  - 可在 `setu_message_cd` 中添加 `{cd_msg}` 提示CD时间\n  ```json\n  {\n    "setu_message_send": ["abc"],\n    "setu_message_cd": ["cba cd: {cd_msg}"]\n  }\n  ```\n\n\n~~所有配置都可选了,还能出问题吗?~~\n\n### bot.py\n\n```py\nnonebot.load_plugin("nonebot_plugin_setu_now")\n```\n\n## 使用\n\n- 指令 `(setu|色图|涩图|来点色色|色色|涩涩)\\s?(r18)?\\s?(.*)?`\n  - 看不懂？\n    - `setu|色图|涩图|来点色色|色色|涩涩` 任意关键词\n    - `r18` 可选 仅在私聊可用 群聊直接忽视\n    - `关键词` 可选\n- 例子\n  - `来点色色 妹妹`\n  - `setur18`\n',
    'author': 'kexue',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/kexue-z/nonebot-plugin-setu-now',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.3,<4.0.0',
}


setup(**setup_kwargs)
