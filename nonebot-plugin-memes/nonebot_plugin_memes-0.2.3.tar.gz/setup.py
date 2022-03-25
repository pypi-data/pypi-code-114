# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_memes']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=8.2.0',
 'aiocache>=0.11.0',
 'emoji>=1.7.0,<2.0.0',
 'fonttools>=4.31.2,<5.0.0',
 'httpx>=0.19.0',
 'imageio>=2.12.0,<3.0.0',
 'nonebot-adapter-onebot>=2.0.0-beta.1,<3.0.0',
 'nonebot2>=2.0.0-beta.1,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-memes',
    'version': '0.2.3',
    'description': 'Nonebot2 plugin for making memes',
    'long_description': '# nonebot-plugin-memes\n\n[Nonebot2](https://github.com/nonebot/nonebot2) 插件，用于表情包制作\n\n\n### 使用\n\n支持的表情包：\n\n发送“表情包制作”显示下图的列表：\n\n<div align="left">\n  <img src="https://s2.loli.net/2022/01/19/KNnsQxOrFgouV6z.jpg" width="500" />\n</div>\n\n\n每个表情包首次使用时会下载对应的图片和字体，可以手动下载 `resources` 下的 `images`，`thumbs` 和 `fonts` 文件夹，放置于机器人运行目录下的 `data/memes/` 文件夹中\n\n\n### 示例\n\n - `鲁迅说 我没说过这句话`\n\n<div align="left">\n  <img src="./examples/2.png" width="250" />\n</div>\n\n\n - `王境泽 我就是饿死 死外边 不会吃你们一点东西 真香`\n\n<div align="left">\n  <img src="./examples/3.gif" width="250" />\n</div>\n\n\n### 特别感谢\n\n- [Ailitonia/omega-miya](https://github.com/Ailitonia/omega-miya) 基于nonebot2的qq机器人\n\n- [HibiKier/zhenxun_bot](https://github.com/HibiKier/zhenxun_bot) 基于 Nonebot2 和 go-cqhttp 开发，以 postgresql 作为数据库，非常可爱的绪山真寻bot\n\n- [kexue-z/nonebot-plugin-nokia](https://github.com/kexue-z/nonebot-plugin-nokia) 诺基亚手机图生成\n',
    'author': 'meetwq',
    'author_email': 'meetwq@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/MeetWq/nonebot-plugin-memes',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.3,<4.0.0',
}


setup(**setup_kwargs)
