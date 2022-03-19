# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['panndas', 'panndas.data', 'panndas.nn', 'panndas.nn.modules']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.3,<2.0']

setup_kwargs = {
    'name': 'panndas',
    'version': '0.0.2',
    'description': 'Neural networks in pandas',
    'long_description': '<div align="center">\n  <img src="https://charlesfrye.github.io/img/panndas-logo.jpeg"><br>\n</div>\n\n-----------------\n\n# `panndas`: neural networks in `pandas`\n[![Tests](https://github.com/charlesfrye/panndas/workflows/Tests/badge.svg)](https://github.com/charlesfrye/panndas/actions?workflow=Tests)\n[![Coverage](https://codecov.io/github/charlesfrye/panndas/coverage.svg?branch=main)](https://codecov.io/gh/charlesfrye/panndas)\n[![Read the Docs](https://readthedocs.org/projects/panndas/badge/)](https://panndas.readthedocs.io/)\n[![PyPI Latest Release](https://img.shields.io/pypi/v/panndas.svg)](https://pypi.org/project/panndas/)\n[![License](https://img.shields.io/pypi/l/panndas.svg)](https://github.com/pandas-dev/pandas/blob/main/LICENSE)\n[![Downloads](https://static.pepy.tech/personalized-badge/panndas?period=month&units=international_system&left_color=black&right_color=orange&left_text=PyPI%20downloads%20per%20month)](https://pepy.tech/project/panndas)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n## What is it?\n\n**Pandas** are bears endemic to China characterized by a bold black-and-white coat, a rotund body, and a [remarkable similarity](https://wp.technologyreview.com/wp-content/uploads/2019/05/adversarial-10.jpg) to [gibbons](https://www.memphiszoo.org/assets/2510/10_white_cheek_gibbon.jpg).\n\n**`pandas`** is a Python package that provides fast, flexible, and expressive data\nstructures designed to make working with "relational" or "labeled" data both\neasy and intuitive.\n\n**`panndas`** is a neural network library built on top of `pandas` as a joke.\n\n## Main Features\nHere are just a few of the things that `panndas` does well:\n\n  -\n\n## Frequently asked questions\n\n#### How do you pronounce "`panndas`"?\n\nThere are two accepted pronunciations: "pa-`None`-das" and "🖕".\n\n### Why?\n\n> > > We do this not because it is easy, but because it is hard.\n> >\n> > _Wayne Gretsky_\n>\n> _Michael Scott_\n\n_Me_\n\n## Contributing to `panndas` [![Open Source Helpers](https://www.codetriage.com/charlesfrye/panndas/badges/users.svg)](https://www.codetriage.com/charlesfrye/panndas)\n\nAll contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas are unwelcome.\n\n## License\n[YOLO](http://swansonquotes.com/wp-content/uploads/s05-ep01-permits1-1000x500.jpg)\n',
    'author': 'Charles Frye',
    'author_email': 'cfrye59@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/charlesfrye/panndas',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
