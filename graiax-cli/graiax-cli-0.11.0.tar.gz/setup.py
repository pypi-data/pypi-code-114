# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['graiax', 'graiax.cli', 'graiax.cli.command', 'graiax.cli.prompt']

package_data = \
{'': ['*']}

install_requires = \
['click-completion>=0.5.2,<0.6.0',
 'prompt-toolkit>=3.0.26,<4.0.0',
 'pyfiglet>=0.8.post1,<0.9',
 'tomlkit>=0.9.2,<0.10.0',
 'typer>=0.4.0,<0.5.0']

extras_require = \
{'fwatch': ['watchgod>=0.7,<0.8'], 'watchgod': ['watchgod>=0.7,<0.8']}

entry_points = \
{'console_scripts': ['graiax = graiax.cli:main']}

setup_kwargs = {
    'name': 'graiax-cli',
    'version': '0.11.0',
    'description': 'Command line tool for Graia Framework.',
    'long_description': '<div align="center">\n\n# Graiax-CLI\n\n_一个简明易用的 Graia 命令行工具_\n\n\n<a href="https://pypi.org/project/graiax-cli"><img alt="Python Version" src="https://img.shields.io/pypi/pyversions/graiax-cli" /></a>\n<a href="https://pypi.org/project/graiax-cli"><img alt="Python Implementation" src="https://img.shields.io/pypi/implementation/graiax-cli" /></a>\n<a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-black.svg" alt="black" /></a>\n<a href="https://pycqa.github.io/isort/"><img src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat" alt="isort"/></a>\n<a href="https://github.com/GraiaCommunity/CLI/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/GraiaCommunity/CLI"></a>\n\n</div>\n\n# 开始使用\n\n`pipx install graiax-cli` (推荐，防止污染全局环境)\n\n或者\n\n`pip install graiax-cli`\n\n## 新建项目\n\n`graiax init` 交互式初始化一个 `Graia Framework` 项目 (Partly WIP)\n\n## 管理插件 (WIP)\n\n`graiax plugin new` 新建插件\n\n`graiax plugin list` 查看插件列表\n\n`graiax plugin add` 添加插件\n',
    'author': 'BlueGlassBlock',
    'author_email': 'blueglassblock@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/GraiaCommunity/CLI',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
