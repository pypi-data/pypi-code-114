# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['blocksim_poetry_plugin']

package_data = \
{'': ['*']}

install_requires = \
['MarkupSafe==2.0.1',
 'docutils>=0.14,<0.18',
 'jinja2==2.11.3',
 'mock>=4.0.3,<5.0.0',
 'sphinx-autoapi>=1.8.4,<2.0.0',
 'sphinx-gallery>=0.10.0,<0.11.0',
 'sphinx==3.3.1',
 'sphinx_rtd_theme>=1.0.0,<2.0.0',
 'sphinxcontrib-apidoc>=0.3.0,<0.4.0',
 'sphinxcontrib-napoleon>=0.7,<0.8']

entry_points = \
{'poetry.application.plugin': ['blocksim_poetry_plugin = '
                               'blocksim_poetry_plugin.plugin:BlocksimApplicationPlugin']}

setup_kwargs = {
    'name': 'blocksim-poetry-plugin',
    'version': '0.1.4',
    'description': 'A plugin for more poetry commands',
    'long_description': 'None',
    'author': 'John Gray',
    'author_email': 'manawenuz@johncloud.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitlab.com/manawenuz/blocksim-poetry-plugin',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
