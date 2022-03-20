# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tui_progress']

package_data = \
{'': ['*']}

install_requires = \
['asciimatics>=1.13.0,<2.0.0',
 'cached-property>=1.5.2,<2.0.0',
 'cursor>=1.3.4,<2.0.0',
 'halo>=0.0.31,<0.0.32',
 'humanize>=4.0.0,<5.0.0',
 'log-symbols>=0.0.14,<0.0.15',
 'terminaltables>=3.1.10,<4.0.0',
 'tqdm>=4.63.0,<5.0.0',
 'wcwidth>=0.2.5,<0.3.0',
 'wrapt>=1.14.0,<2.0.0']

setup_kwargs = {
    'name': 'tui-progress',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Zach Kanzler',
    'author_email': 'they4kman@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
