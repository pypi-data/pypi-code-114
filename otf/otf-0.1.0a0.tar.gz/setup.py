# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['otf']

package_data = \
{'': ['*']}

extras_require = \
{'dev-tools': ['pytest-watch>=4.2.0,<5.0.0']}

setup_kwargs = {
    'name': 'otf',
    'version': '0.1.0a0',
    'description': 'A python framework for on-the-fly distributed workflows',
    'long_description': '# On-the-fly distributed python workflows\n\n[![Tests](https://github.com/till-varoquaux/otf/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/till-varoquaux/otf/actions/workflows/ci.yml)\n[![codecov](https://codecov.io/gh/till-varoquaux/otf/branch/main/graph/badge.svg?token=ahhI117oFg)](https://codecov.io/gh/till-varoquaux/otf)\n[![PyPI](https://img.shields.io/pypi/v/otf.svg)](https://pypi.org/project/otf/)\n[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)\n\nOTF is a framework to programatically write, run and debug workflows.\n',
    'author': 'Till Varoquaux',
    'author_email': 'till.varoquaux@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/till-varoquaux/otf',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
