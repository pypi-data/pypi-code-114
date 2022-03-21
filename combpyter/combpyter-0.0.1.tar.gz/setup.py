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
    'version': '0.0.1',
    'description': '',
    'long_description': None,
    'author': 'Benjamin Hackl',
    'author_email': 'devel@benjamin-hackl.at',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
