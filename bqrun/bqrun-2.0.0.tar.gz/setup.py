# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bqrun']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.0.3,<4.0.0', 'networkx>=2.6.3,<3.0.0', 'pydot>=1.4.2,<2.0.0']

entry_points = \
{'console_scripts': ['bqrun = bqrun.cli:main']}

setup_kwargs = {
    'name': 'bqrun',
    'version': '2.0.0',
    'description': 'Query runner for BigQuery. It automatically analyzes dependencies and runs only necessary queries in parallel.',
    'long_description': '# bqrun\n\n## 概要\nディレクトリの中にあるsqlファイルを全て読み、依存関係を解析し（あるファイルAで`select .. from`されているテーブルが別のファイルBで`create table`されていた場合、\nBはAより前に実行される）、順番に実行するためのMakefileを作成、makeを実行する。\n\n## 外部依存\n1. docker\n2. graphviz（dotコマンド）\n\n## インストール\n1. `pip install bqrun`\n\n## 前提\n1. 1つのディレクトリの中に全てのSQLファイルが入っていること\n1. 全てのSQLファイルは拡張子`.sql`を持つこと、かつ、クエリ以外に`.sql`で終わるファイルがないこと\n## 大まかな動作\n1. 全SQLファイルを読んで依存関係を解析、依存関係に従ったMakefileを作成する\n1. このMakefileにより、各ファイルに対し以下のようなコマンドが実行される\n    1. 各SQLファイルを`bq query`に投げる\n    1. `done.<base name>` というファイルを作成する(`<base name>`は、ファイル名の拡張子以外)\n1. 2回目以降の実行では、各ファイルについて`done.<base name>`ファイルのタイムスタンプと、依存先のファイルのタイムスタンプを比較し再実行が必要な部分だけが実行される\n\n## オプション\n1. `-p=<num>`または`--parallel=<num>`: 並列実行数を指定（デフォルトは8）\n',
    'author': 'Yasunori Horikoshi',
    'author_email': 'horikoshi.et.al@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/hotoku/bqrun',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
