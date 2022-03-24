# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_giyf']

package_data = \
{'': ['*']}

install_requires = \
['nonebot-adapter-onebot>=2.0.0b1,<2.1.0', 'nonebot2>=2.0.0b2,<2.1.0']

setup_kwargs = {
    'name': 'nonebot-plugin-giyf',
    'version': '0.1.0',
    'description': 'nonebot2 群聊快速生成搜索引擎链接',
    'long_description': '<p align="center">\n  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>\n</p>\n\n<div align="center">\n\n# nonebot-plugin-giyf\n\n_适用于 [NoneBot2](https://v2.nonebot.dev) 的搜索引擎插件_\n\n</div>\n\n------\n\n![Python](https://img.shields.io/badge/python-3.8%2B-lightgrey)\n![nonebot2](https://img.shields.io/badge/nonebot2-2.0.0b2-yellowgreen)\n[![GitHub license](https://img.shields.io/github/license/KoishiStudio/nonebot-plugin-giyf)](https://github.com/KoishiStudio/nonebot-plugin-giyf/blob/main/LICENSE)\n[![pypi](https://img.shields.io/pypi/v/nonebot-plugin-giyf?color=blue)](https://pypi.org/project/nonebot-plugin-giyf/)\n\n[![GitHub issues](https://img.shields.io/github/issues/KoishiStudio/nonebot-plugin-giyf)](https://github.com/KoishiStudio/nonebot-plugin-giyf/issues)\n[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/KoishiStudio/nonebot-plugin-giyf?include_prereleases)](https://github.com/KoishiStudio/nonebot-plugin-giyf/releases)\n[![GitHub all releases downloads](https://img.shields.io/github/downloads/KoishiStudio/nonebot-plugin-giyf/total)](https://github.com/KoishiStudio/nonebot-plugin-giyf/releases)\n![GitHub contributors](https://img.shields.io/github/contributors/KoishiStudio/nonebot-plugin-giyf)\n![GitHub Repo stars](https://img.shields.io/github/stars/KoishiStudio/nonebot-plugin-giyf?style=social)\n\n------\n\n本项目是 [Flandre](https://github.com/KoishiStudio/Flandre) 的\n[wiki](https://github.com/KoishiStudio/Flandre/tree/main/src/plugins/wiki) 组件，经简单修改成为独立插件发布。\n\n同时，本插件和 [nonebot-plugin-mediawiki](https://github.com/KoishiStudio/nonebot-plugin-mediawiki) 有着类似的结构，至于原因嘛……(ಡωಡ)\n\n## 用途\n\n如题，`Google is your friend`，用于指引群友快速 访 ~~(tui)~~ 问 ~~(dao)~~ 谷歌娘（在中国大陆大概就是度娘了～）\n\n## 使用说明\n```plaintext\nTip：本插件的设置系统和 nonebot plugin-mediawiki 基本一致，因此如果你使用过前者，那么本插件的配置应该很容易上手\n```\n### TL;DR\n\n查询： `？前缀 关键词`\n\n添加（全局）搜索引擎： `search.add` `search.add.global`\n\n删除（全局）搜索引擎： `search.delete` `search.delete.global`\n\n修改（全局）搜索引擎： `search.default` `search.default.global`\n\n查看搜索引擎列表： `search.list` `search.list.global`\n\n**其中所有非全局指令均需要在目标群中进行，所有全局指令均只有Bot管理员能执行**\n\n### 参数说明：\n#### 前缀\n就是你给这个搜索引擎起的代号，好记就行，例如给谷歌娘叫`go`，给度娘叫`bd`，等等。**只支持英文和数字**\n\n#### 链接：\n需要使用搜索引擎的搜索url，**而非首页url**；这类url的明显特征就是，其中带有`%s`，并且在搜索时`%s`会被替换成你的搜索关键字\n\n例如：\n```plaintext\nGoogle: https://www.google.com/search?q=%s\nBaidu: https://www.baidu.com/s?wd=%s\nBing: https://www.bing.com/search?q=%s\nDuckduckgo: https://duckduckgo.com/?q=%s\n```\n\n获取这类链接有三种方法：\n\n1. ~~问谷歌~~\n\n（经过查找，只找到了谷歌和百度的……）\n\n\n2. 查看浏览器设置\n\n打开浏览器的搜索引擎设置，这里会出现默认配置好的搜索引擎，以及一些你访问过的搜索引擎。点击“编辑”，在“查询URL”一栏通常就是我们要找的\n\n```plaintext\nTip：部分搜索引擎在此可能显示的有一些变量，例如 {google:baseURL}search?q=%s ，本插件无法识别这种，还请留意\n```\n\n3. ~~人工智能（不是~~\n\n打开你要使用的搜索引擎，随便搜点什么（建议使用英文或数字，中文被编码后根本分不清……），把链接复制下来，把你原先输入的搜索关键字换成`%s`，大功告成！\n\n```plaintext\nTip：某些搜索引擎的链接可能包含你的一些个人信息，建议在隐私浏览窗口中进行上述操作。\n另外，通常情况下，搜索关键词后面的附加参数并不会影响搜索结果，因此一般可以去除\n例如： https://www.bing.com/search?q=%s&form=xxxx 其中的 &from=xxxx就可以去掉 \n```\n\n## TODO\n- [ ] 内置一些常用的搜索引擎，用来快速添加',
    'author': 'KoishiChan',
    'author_email': '68314080+KoishiStudio@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/KoishiStudio/nonebot-plugin-giyf',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
