# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['projectslib']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.22.3,<2.0.0',
 'pandas>=1.4.1,<2.0.0',
 'scipy>=1.8.0,<2.0.0',
 'tensorflow>=2.8.0,<3.0.0',
 'tqdm>=4.63.0,<5.0.0']

setup_kwargs = {
    'name': 'projectslib',
    'version': '0.1.0',
    'description': 'Library for code for my projects',
    'long_description': None,
    'author': 'jetm',
    'author_email': 'abhmul@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
