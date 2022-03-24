# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vdx_helper']

package_data = \
{'': ['*']}

install_requires = \
['nndict==1.0.0', 'requests==2.22.0']

setup_kwargs = {
    'name': 'vdx-helper',
    'version': '3.1.0',
    'description': '',
    'long_description': None,
    'author': 'Joana Teixeira',
    'author_email': 'joana.teixeira@vizidox.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
