# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['combpyter', 'combpyter.lattice_paths']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib[plot]>=3.5.1,<4.0.0', 'numpy>=1.22.3,<2.0.0']

setup_kwargs = {
    'name': 'combpyter',
    'version': '0.0.2',
    'description': 'A lightweight Python library for generating combinatorial structures.',
    'long_description': 'combpyter\n---------\n\nA lightweight Python library for generating combinatorial objects.\nMostly a personal project used in conjunction with bijection hunting\nand general analysis of combinatorial objects.\n',
    'author': 'Benjamin Hackl',
    'author_email': 'devel@benjamin-hackl.at',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/behackl/combpyter',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
