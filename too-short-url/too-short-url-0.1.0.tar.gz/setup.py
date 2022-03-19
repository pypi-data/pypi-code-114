# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['too_short_url']

package_data = \
{'': ['*']}

install_requires = \
['Brotli>=1.0.9,<2.0.0',
 'environs>=9.5.0,<10.0.0',
 'furl>=2.1.3,<3.0.0',
 'httpx>=0.22.0,<0.23.0',
 'icecream>=2.1.2,<3.0.0',
 'logzero>=1.7.0,<2.0.0',
 'pyquery>=1.4.3,<2.0.0',
 'typer>=0.4.0,<0.5.0',
 'validators>=0.18.2,<0.19.0']

entry_points = \
{'console_scripts': ['too-st = too_short_url.__main__:app']}

setup_kwargs = {
    'name': 'too-short-url',
    'version': '0.1.0',
    'description': 'short url based on too.st',
    'long_description': '# too-short-url\n[![pytest](https://github.com/ffreemt/too-short-url/actions/workflows/routine-tests.yml/badge.svg)](https://github.com/ffreemt/too-short-url/actions)[![python](https://img.shields.io/static/v1?label=python+&message=3.8%2B&color=blue)](https://www.python.org/downloads/)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/too-short-url.svg)](https://badge.fury.io/py/too-short-url)\n\nshorturl based on too.st\n\n## Install it\n```bash\npip install too-short-url\n\n# or pip install git+https://github.com/ffreemt/too-short-url\n# or clone the repo and\n```\n\n## Use it\n\n### Command line\n```bash\ntoo-st http://baid.com\n# too.st/b\n\n```\n\n### With in `python`\n```python\nfrom too_short_url import too_st\n\nprint(too_st("http://baidu.com"))\n# too.st/b\n```\n\n### Docs\n```bash\ntoo-st --help\n\nUsage: too-st [OPTIONS] URL\n\n  Generate too.st short url.\n\n  e.g.\n\n  * too-st baidu.com  # https://too.st/b\n\n  * too-st baidu.com -k abc  # https://too.st/b\n\n  * too-st baidu.com -k abc -b  # https://too.st/abc or https://too.st/b\n  dependent on whether https://too.st/abc is already taken or reserved by th\n  admin of too.st.\n\nArguments:\n  URL  url to be shortened  [required]\n\nOptions:\n  -k, --keyword, --kw KEYWORD     desired keyword, e.g. https://too.st/abc for\n                                  KEYWORD set to abc\n  -b, --best-effort, --besteffort\n                                  whether to try hard to generaet the desired\n                                  shorturl https://too.st/KEYWORD\n  -v, -V, --version               Show version info and exit.\n  --help                          Show this message and exit.\n```\n',
    'author': 'ffreemt',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ffreemt/too-short-url',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
