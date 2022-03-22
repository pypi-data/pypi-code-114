# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['girder_pytest_pyppeteer']

package_data = \
{'': ['*']}

install_requires = \
['mkdocs[docs]>=1.2.3,<2.0.0',
 'mkdocstrings[docs]>=0.18.1,<0.19.0',
 'pytest>=7.0.1,<8.0.0']

extras_require = \
{'pyppeteer': ['pyppeteer>=1.0.2,<2.0.0', 'pytest-asyncio>=0.18.1,<0.19.0']}

entry_points = \
{'console_scripts': ['pytest-docker = '
                     'girder_pytest_pyppeteer.main:run_pytest_docker_compose'],
 'pytest11': ['pyppeteer = girder_pytest_pyppeteer.plugin']}

setup_kwargs = {
    'name': 'girder-pytest-pyppeteer',
    'version': '0.0.7',
    'description': 'Pytest plugin for using pyppeteer to test Girder 4 applications',
    'long_description': None,
    'author': 'Daniel Chiquito',
    'author_email': 'daniel.chiquito@kitware.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
