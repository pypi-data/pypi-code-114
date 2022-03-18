# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['juridecomposer']

package_data = \
{'': ['*']}

install_requires = \
['nltk>=3.5,<4.0',
 'pandas>=1.0.5,<2.0.0',
 'pattern>=3.6,<4.0',
 'xmltodict>=0.12.0,<0.13.0']

setup_kwargs = {
    'name': 'juridecomposer',
    'version': '0.2.0',
    'description': '',
    'long_description': None,
    'author': 'Roos Bakker',
    'author_email': 'roos.bakker@tno.nl',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.1,<3.7',
}


setup(**setup_kwargs)
