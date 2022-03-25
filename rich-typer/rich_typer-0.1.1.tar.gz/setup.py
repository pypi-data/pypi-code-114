# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rich_typer']

package_data = \
{'': ['*']}

install_requires = \
['rich>=11.2.0,<12.0.0', 'typer>=0.4.0,<0.5.0']

setup_kwargs = {
    'name': 'rich-typer',
    'version': '0.1.1',
    'description': 'more beautiful Typer',
    'long_description': '# Rich Typer\n\n## 介绍\n\n本项目是将Rich和Typer结合在一起，将CLI打造的更加美观漂亮。\n\n![](images/example.png)\n\n## 安装\n\n```bash\npip install rich_typer\n```\n\n或者使用`poetry` 安装\n\n```bash\ngit clone https://github.com/Elinpf/rich_typer\ncd rich_typer\npoetry build\npip install dist/<whl_file>\n```\n\n## 使用\n\n完全兼容[Typer](https://github.com/tiangolo/typer)语法，具体语法细节参考[Typer官方文档](https://typer.tiangolo.com/)\n\n\n除此之外增加了如下几个参数：\n\n- `banner`  增加标题\n- `banner_justify` 标题位置\n- `epilog_blend` 底部信息的渐变色\n- `usage` 自定义Usage\n\n## Example\n\n```py\nfrom rich_typer import RichTyper, Argument, Option\n\n\napp = RichTyper()\nbanner = f"[b]Rich Typer[/b] [magenta][/] 🤑\\n\\n[dim]将 Rich 与 Typer 结合起来，使界面更加漂亮。\\n"\n\nurl = "♥ https://github.com/Elinpf/rich_typer"\n\n\n@app.command(banner=banner, banner_justify=\'center\', epilog=url)\ndef main(\n    name: str = Argument(...,\n                         help="Name of the [green]person to greet[/]."),\n    message: str = Option(\'ms\', \'-m\', \'--message\',\n                                help="The message [red]to[/] display"),\n    version: bool = Option(False, \'-v\', \'--version\',\n                           help="Show the [u]version[/] and exit"),\n) -> None:\n    """[bold][blue]Rich Typer[/] example."""\n    ...\n\n\napp()\n```\n',
    'author': 'Elin',
    'author_email': '365433079@qq.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Elinpf/rich_typer',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
