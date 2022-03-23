# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['geolocate']

package_data = \
{'': ['*']}

install_requires = \
['p-tqdm>=1.3.3,<2.0.0', 'requests>=2.27.1,<3.0.0']

setup_kwargs = {
    'name': 'geolocate',
    'version': '0.1.0',
    'description': 'Georeferencing large amounts of data for free.',
    'long_description': None,
    'author': 'Gabriel Gazola Milan',
    'author_email': 'gabriel.gazola@poli.ufrj.br',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
