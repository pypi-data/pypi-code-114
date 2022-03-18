# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['betag']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.3,<2.0', 'streamlit>=1.5.1,<2.0.0']

entry_points = \
{'console_scripts': ['betag = betag.main:cli']}

setup_kwargs = {
    'name': 'betag',
    'version': '0.1.4',
    'description': '',
    'long_description': None,
    'author': 'Jaume Ferrarons',
    'author_email': 'jaume.ferrarons@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
