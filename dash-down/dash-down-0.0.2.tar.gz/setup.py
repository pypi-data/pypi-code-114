# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dash_down']

package_data = \
{'': ['*']}

install_requires = \
['dash-extensions==0.1.0rc2',
 'dash-iconify>=0.1.0,<0.2.0',
 'dash-labs>=1.0.3,<2.0.0',
 'dash-mantine-components>=0.6.0,<0.7.0',
 'dash==2.3.0',
 'mistletoe>=0.8.2,<0.9.0',
 'mistune>=2.0.2,<3.0.0']

setup_kwargs = {
    'name': 'dash-down',
    'version': '0.0.2',
    'description': '',
    'long_description': None,
    'author': 'emher',
    'author_email': 'emil.h.eriksen@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
