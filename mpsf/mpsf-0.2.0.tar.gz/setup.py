# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mpsf']

package_data = \
{'': ['*']}

install_requires = \
['sphinx-rtd-theme>=1.0.0,<2.0.0']

setup_kwargs = {
    'name': 'mpsf',
    'version': '0.2.0',
    'description': 'Multiprocessing Single Function (mpsf)',
    'long_description': None,
    'author': 'morten',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
