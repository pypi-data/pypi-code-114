# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['auto_markdown_badges']

package_data = \
{'': ['*']}

install_requires = \
['click-help-colors>=0.9.1,<0.10.0',
 'simpleicons>=6.13.0,<7.0.0',
 'typer>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['auto-markdown-badges = auto_markdown_badges.cli:app']}

setup_kwargs = {
    'name': 'auto-markdown-badges',
    'version': '0.2.1',
    'description': 'Auto-generated markdown badges.',
    'long_description': '# auto-markdown-badges\n\n[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/feluelle/auto-markdown-badges/main.svg)](https://results.pre-commit.ci/latest/github/feluelle/auto-markdown-badges/main)\n![test workflow](https://github.com/feluelle/auto-markdown-badges/actions/workflows/test.yml/badge.svg)\n![codeql-analysis workflow](https://github.com/feluelle/auto-markdown-badges/actions/workflows/codeql-analysis.yml/badge.svg)\n[![codecov](https://codecov.io/gh/feluelle/auto-markdown-badges/branch/main/graph/badge.svg?token=J8UEP8IVY4)](https://codecov.io/gh/feluelle/auto-markdown-badges)\n[![PyPI version](https://img.shields.io/pypi/v/auto-markdown-badges)](https://pypi.org/project/auto-markdown-badges/)\n[![License](https://img.shields.io/pypi/l/auto-markdown-badges)](https://github.com/feluelle/auto-markdown-badges/blob/main/LICENSE)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/auto-markdown-badges)](https://pypi.org/project/auto-markdown-badges/)\n[![PyPI version](https://img.shields.io/pypi/dm/auto-markdown-badges)](https://pypi.org/project/auto-markdown-badges/)\n\n> Auto-generated markdown badges. 🧙🖼\n\nInspired by [markdown-badges](https://github.com/Ileriayo/markdown-badges), I wanted to have a tool which automatically creates badges for me.\n\n## 🚀 Get started\n\nTo install it from [PyPI](https://pypi.org/) run:\n\n```console\npip install auto-markdown-badges\n```\n\nThen just call it like this:\n\n```console\nUsage: auto-markdown-badges generate [OPTIONS] INPUT_FILE\n\n  Generates badges from a file.\n\nOptions:\n  INPUT_FILE                      The file to use for generation of badges.\n                                  [required]\n  -o, --output-file FILE          The file to output to.\n  -p, --placement [header|inplace|footer]\n                                  Specify where to place the badge.  [default:\n                                  Placement.INPLACE]\n  -h, --help                      Show this message and exit.\n```\n\n_Examples of generated badges can be found in the [examples](examples) directory._\n\n## 🤔 How it Works\n\n1. It reads the given file, line by line\n2. It tries to find [simple-icons](https://github.com/simple-icons/simple-icons) for every word\n3. It replaces the word with a badge\n\n## ❤️ Contributing\n\nContributions are very welcome. Please go ahead and raise an issue if you have one or open a PR. Thank you.\n',
    'author': 'Felix Uellendall',
    'author_email': 'feluelle@pm.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
