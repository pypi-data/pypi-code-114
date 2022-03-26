# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['docker_compose_diagram']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML==5.3.1', 'click>=8.0.3,<9.0.0', 'diagrams>=0.20.0,<0.21.0']

entry_points = \
{'console_scripts': ['compose-diagram = docker_compose_diagram:process_cli']}

setup_kwargs = {
    'name': 'docker-compose-diagram',
    'version': '0.1.2.5',
    'description': '',
    'long_description': None,
    'author': 'Skonik',
    'author_email': 's.konik.dev@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
