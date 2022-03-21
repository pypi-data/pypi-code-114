# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['qbuspy']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.27.1,<3.0.0']

setup_kwargs = {
    'name': 'qbuspy',
    'version': '0.1.0',
    'description': 'Qbuspy is the python package for easy interfacing with the Qbus home automation system.',
    'long_description': '# qbuspy',
    'author': 'vlaminckaxel',
    'author_email': 'axel.vlaminck@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/vlaminckaxel/qbuspy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
