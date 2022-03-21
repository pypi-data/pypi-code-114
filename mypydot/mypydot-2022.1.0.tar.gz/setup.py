# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mypydot', 'mypydot.src']

package_data = \
{'': ['*'],
 'mypydot': ['template/*',
             'template/language/*',
             'template/language/go/*',
             'template/language/java/*',
             'template/language/python/*',
             'template/os/*',
             'template/shell/*',
             'template/shell/bash/*',
             'template/shell/zim/*',
             'template/shell/zsh/*',
             'template/tools/docker/*',
             'template/tools/editors/*',
             'template/tools/editors/vim/*',
             'template/tools/git/*']}

install_requires = \
['PyYAML==6.0', 'emoji>=1.6.1,<2.0.0']

entry_points = \
{'console_scripts': ['mypydot = mypydot.src.main:entry_point']}

setup_kwargs = {
    'name': 'mypydot',
    'version': '2022.1.0',
    'description': 'Python package to manage your dotfiles',
    'long_description': '[![PyPI version](https://badge.fury.io/py/mypydot.svg)](https://badge.fury.io/py/mypydot)\n![CI](https://github.com/andres-ortizl/mypydot/actions/workflows/main.yml/badge.svg)\n[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=mypydot&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=mypydot)\n[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=mypydot&metric=coverage)](https://sonarcloud.io/summary/new_code?id=mypydot)\n[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=mypydot&metric=bugs)](https://sonarcloud.io/summary/new_code?id=mypydot)\n## Mypydot\n\nMypydot is a tool created for managing your dotfiles using a Python application\n\n## Status\n\nIn development\n\n## Instructions\nTBD\n\n',
    'author': 'Andrés Ortiz',
    'author_email': 'andrs.ortizl@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/andres-ortizl/mypydot',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
