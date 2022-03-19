# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['footing', 'footing.tests']

package_data = \
{'': ['*']}

install_requires = \
['click>=6.7',
 'cookiecutter>=1.6.0',
 'python-gitlab>=2.10.1',
 'pyyaml>=3.12',
 'requests>=2.13.0',
 'tldextract>=3.1.2']

entry_points = \
{'console_scripts': ['footing = footing.cli:main']}

setup_kwargs = {
    'name': 'footing',
    'version': '0.1.1',
    'description': 'Keep templated projects in sync with their template',
    'long_description': 'footing\n########################################################################\n\nDocumentation\n=============\n\n`View the footing docs here\n<https://footing.readthedocs.io/>`_.\n\nInstallation\n============\n\nInstall footing with::\n\n    pip3 install footing\n\n\nContributing Guide\n==================\n\nFor information on setting up footing for development and\ncontributing changes, view `CONTRIBUTING.rst <CONTRIBUTING.rst>`_.\n',
    'author': 'Opus 10 Engineering',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Opus10/footing',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.0,<4',
}


setup(**setup_kwargs)
