# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['eagerx_interbotix',
 'eagerx_interbotix.vx300s',
 'eagerx_interbotix.vx300s.pybullet',
 'eagerx_interbotix.vx300s.real']

package_data = \
{'': ['*']}

install_requires = \
['eagerx-gui>=0.1.4,<0.2.0',
 'eagerx-pybullet>=0.1.0,<0.2.0',
 'eagerx-reality>=0.1.4,<0.2.0']

setup_kwargs = {
    'name': 'eagerx-interbotix',
    'version': '0.1.1',
    'description': 'EAGERx interface to interbotix robot arms.',
    'long_description': None,
    'author': 'Jelle Luijkx',
    'author_email': 'j.d.luijkx@tudelft.nl',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/eager-dev/eagerx_interbotix',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
