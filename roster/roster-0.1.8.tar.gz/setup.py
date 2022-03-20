# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['roster']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'roster',
    'version': '0.1.8',
    'description': 'Python object registers. Keep track of your classes, functions and data.',
    'long_description': "# roster\nPython object registers. Keep track of your classes, functions and data.\n\n## Installation\n`roster` can be installed from [PyPI](https://pypi.org/project/roster/)\n```console\npip install roster\n```\n\n## Usage:\n\n### `Record`\n\n#### Default Record\n```python\nfrom roster import Record\n\nnumbers: Record[int] = Record()\n\nnumbers(1)\nnumbers(2)\nnumbers(3)\n```\n\n```python\n>>> numbers\n[1, 2, 3]\n```\n\n#### Generate each `item`\n```python\nfrom roster import Record\n\ncharacters: Record[str] = Record()\n\n@characters.item\ndef character(char: str, /) -> str:\n    return char.upper()\n\ncharacter('a')\ncharacter('b')\ncharacter('c')\n```\n\n```python\n>>> characters\n['A', 'B', 'C']\n```\n\n### `Register`\n\n#### Default Register\n```python\nfrom roster import Register\n\nservices: Register[str, type] = Register()\n\n@services('youtube')\nclass YouTube: pass\n\n@services('spotify')\nclass Spotify: pass\n```\n\n```python\n>>> services\n{'youtube': <class '__main__.YouTube'>, 'spotify': <class '__main__.Spotify'>}\n```\n\n#### Generate each `key`\n```python\nfrom roster import Register\nfrom typing import Callable\n\nfunctions: Register[str, Callable] = Register()\n\n@functions.key\ndef function(name: str, /) -> str:\n    return name.upper()\n\n@function('foo')\ndef foo(): pass\n\n@function('bar')\ndef bar(): pass\n```\n\n```python\n>>> functions\n{'FOO': <function foo at 0x7f9c4f065790>, 'BAR': <function bar at 0x7f9c4f065820>}\n```\n\n#### Generate each `value`\n```python\nfrom roster import Register\nfrom typing import Callable\n\nfunctions: Register[str, Callable] = Register()\n\n@functions.value\ndef function(name: str, /) -> str:\n    return name.upper()\n\n@function('foo')\ndef foo(): pass\n\n@function('bar')\ndef bar(): pass\n```\n\n```python\n>>> functions\n{<function foo at 0x7f26443aa790>: 'FOO', <function bar at 0x7f26443aa820>: 'BAR'}\n```\n\n#### Generate each `entry`\n```python\nfrom roster import Register\nfrom typing import Tuple\n\nidentifiers: Register[str, str] = Register()\n\n@identifiers.entry\ndef identifier(code: str, /) -> Tuple[str, str]:\n    return (code[0], code.upper())\n\nidentifier('foo')\nidentifier('bar')\n```\n\n```python\n>>> identifiers\n{'f': 'FOO', 'b': 'BAR'}\n```",
    'author': 'Tom Bulled',
    'author_email': '26026015+tombulled@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/tombulled/roster',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
