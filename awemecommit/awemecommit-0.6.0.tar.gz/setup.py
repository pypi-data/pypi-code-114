# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['awemecommit']

package_data = \
{'': ['*']}

install_requires = \
['GitPython>=3.1.27,<4.0.0',
 'pyperclip>=1.8.2,<2.0.0',
 'questionary>=1.10.0,<2.0.0',
 'typer>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['awemecommit = awemecommit.main:app']}

setup_kwargs = {
    'name': 'awemecommit',
    'version': '0.6.0',
    'description': '',
    'long_description': '# `awemecommit`\n\ncommit message 辅助工具\n\n**Usage**:\n\n```console\n$ awemecommit [OPTIONS] COMMAND [ARGS]...\n```\n\n**Options**:\n\n* `--install-completion`: Install completion for the current shell.\n* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.\n* `--help`: Show this message and exit.\n\n**Commands**:\n\n* `commit`: 用规范的 message 提交 commit\n* `owncommit`: 查看目前分支上所有新增的 commit, 但不包含 merge 来的\n\n## `awemecommit commit`\n\n用规范的 message 提交 commit\n\n**Usage**:\n\n```console\n$ awemecommit commit [OPTIONS]\n```\n\n**Options**:\n\n* `-g, --gits`: 多仓创建 commit  [default: False]\n* `-c, --clipboard`: 将 commit message 复制到剪切板  [default: False]\n* `-p, --push`: 创建 commit 后直接push  [default: False]\n* `--help`: Show this message and exit.\n\n## `awemecommit owncommit`\n\n查看目前分支上所有新增的 commit, 但不包含 merge 来的\n\n**Usage**:\n\n```console\n$ awemecommit owncommit [OPTIONS]\n```\n\n**Options**:\n\n* `-b, --branch TEXT`: 作比较的分支  [default: develop]\n* `--help`: Show this message and exit.\n',
    'author': 'Zijie Fang',
    'author_email': 'fangzijie.proalex@bytedance.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
