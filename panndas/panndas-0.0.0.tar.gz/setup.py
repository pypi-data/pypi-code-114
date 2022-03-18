# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['panndas', 'panndas.data', 'panndas.nn']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.3,<2.0']

setup_kwargs = {
    'name': 'panndas',
    'version': '0.0.0',
    'description': 'Neural networks in pandas',
    'long_description': '<div align="center">\n  <!-- <img src="https://pandas.pydata.org/static/img/pandas.svg"><br> -->\n</div>\n\n-----------------\n\n# panndas: neural networks in pandas\n[![PyPI Latest Release](https://img.shields.io/pypi/v/panndas.svg)](https://pypi.org/project/panndas/)\n[![Package Status](https://img.shields.io/pypi/status/panndas.svg)](https://pypi.org/project/panndas/)\n[![License](https://img.shields.io/pypi/l/panndas.svg)](https://github.com/pandas-dev/pandas/blob/main/LICENSE)\n[![Coverage](https://codecov.io/github/charlesfrye/panndas/coverage.svg?branch=main)](https://codecov.io/gh/charlesfrye/panndas)\n[![Downloads](https://static.pepy.tech/personalized-badge/panndas?period=month&units=international_system&left_color=black&right_color=orange&left_text=PyPI%20downloads%20per%20month)](https://pepy.tech/project/panndas)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n## What is it?\n\n**pandas** is a Python package that provides fast, flexible, and expressive data\nstructures designed to make working with "relational" or "labeled" data both\neasy and intuitive.\n\n**panndas** is a neural network library built on top of pandas as a joke.\n\n## Main Features\nHere are just a few of the things that panndas does well:\n\n  -\n\n## License\n[YOLO](LICENSE)\n\n## Contributing to panndas [![Open Source Helpers](https://www.codetriage.com/pandas-dev/pandas/badges/users.svg)](https://www.codetriage.com/pandas-dev/pandas)\n\nAll contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas are unwelcome.\n',
    'author': 'Charles Frye',
    'author_email': 'cfrye59@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/charlesfrye/panndas',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0.0',
}


setup(**setup_kwargs)
