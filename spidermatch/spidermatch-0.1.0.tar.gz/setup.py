# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['spidermatch', 'tests']

package_data = \
{'': ['*'], 'spidermatch': ['assets/*', 'windows/*']}

install_requires = \
['PyQt6>=6.2.3,<7.0.0', 'qt-material>=2.10,<3.0']

setup_kwargs = {
    'name': 'spidermatch',
    'version': '0.1.0',
    'description': 'Top-level package for SpiderMatch.',
    'long_description': 'SpiderMatch\n===========\n\n[![image](https://img.shields.io/pypi/v/spidermatch.svg)](https://pypi.python.org/pypi/spidermatch)\n\nAn open-source app for setting up automated spider lookups of incidents\ncovered by local news in a certain country. Used for OSINT\ninvestigations in policing.\n\n-   Free software: GNU General Public License v3\n-   Documentation: <https://spidermatch.readthedocs.io>.\n\nFeatures\n--------\n\n-   TODO\n\nCredits\n-------\n\nThis package was created with\n[Cookiecutter](https://github.com/audreyr/cookiecutter) and the\n[audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)\nproject template.\n',
    'author': 'Agustín Covarrubias',
    'author_email': 'agucova@uc.cl',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/agucova/spidermatch',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
