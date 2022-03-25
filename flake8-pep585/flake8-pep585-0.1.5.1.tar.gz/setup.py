# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flake8_pep585']

package_data = \
{'': ['*']}

entry_points = \
{'flake8.extension': ['PEA = flake8_pep585.plugin:Pep585Plugin']}

setup_kwargs = {
    'name': 'flake8-pep585',
    'version': '0.1.5.1',
    'description': 'flake8 plugin to enforce new-style type hints (PEP 585)',
    'long_description': '# flake8-pep585\n\nThis plugin enforces the changes proposed by [PEP 585](https://peps.python.org/pep-0585/).\n\n## What does PEP 585 change?\n\nBefore PEP 585, you had to import stuff from `typing` to annotate some objects from the standard library:\n\n- For context managers, you\'d import `typing.ContextManager`\n- For lists, you\'d import `typing.List`\n- For callables, you\'d import `typing.Callable`\n- ...and so on\n\nWith PEP 585, you can now use classes already present in the standard library. For example:\n- For a context manager giving an `int`, use `contextlib.AbstractContextManager[int]`\n- For a `list` of `dict`s mapping `str`s to `int`s, use `list[dict[str, int]]`\n- For a callable taking a `float` and returning an `int`, use `collections.abc.Callable[[float], int]`\n\n`typing.List`, `typing.Callable` etc. are now deprecated. This is pretty hard to discover, since these\nimports don\'t cause a deprecation warning. IDEs don\'t help either: the "auto-import" feature often suggests\nimporting a deprecated item.\n\nThis plugin lets you find these deprecated imports.\n\n## Examples\n\n### Direct import\n```py\nfrom typing import Callable\n```\n```\nPEA001 typing.Callable is deprecated, use collections.abc.Callable instead. See PEP 585 for details\n```\n\n### Qualified import\n```py\nfrom datetime import time\nimport typing as ty\n\ndef construct_time(match: ty.Match) -> time:\n    return time(\n        hour=int(match["hour"]),\n        minute=int(match["minute"]),\n    )\n```\n```\nPEA001 typing.Match is deprecated, use re.Match instead. See PEP 585 for details\n```\n\n# Installation\n\n1. Make sure you have `flake8` installed\n2. Run `pip install flake8-pep585`\n3. Run `flake8` on your code\n',
    'author': 'decorator-factory',
    'author_email': 'decorator-factory@yandex.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/decorator-factory/flake8-pep585',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
