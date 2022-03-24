# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['blocksim_poetry_plugin']

package_data = \
{'': ['*']}

install_requires = \
['MarkupSafe==2.0.1', 'jinja2==2.11.3', 'sphinx==3.3.1']

entry_points = \
{'poetry.application.plugin': ['baseline = '
                               'blocksim_poetry_plugin.plugin:BlocksimApplicationPlugin']}

setup_kwargs = {
    'name': 'blocksim-poetry-plugin',
    'version': '0.1.2',
    'description': 'A plugin for more poetry commands',
    'long_description': 'None',
    'author': 'John Gray',
    'author_email': 'manawenuz@johncloud.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitlab.com/manawenuz/blocksim_poetry_plugin',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
