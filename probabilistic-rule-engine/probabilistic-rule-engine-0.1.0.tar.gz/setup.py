# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['probabilistic_rule_engine']

package_data = \
{'': ['*']}

install_requires = \
['numpy', 'pandas']

setup_kwargs = {
    'name': 'probabilistic-rule-engine',
    'version': '0.1.0',
    'description': 'Probabilistic Rule Engine',
    'long_description': "# probabilistic-rule-engine\n\n## Getting Started\nInstall poetry: https://python-poetry.org/docs/#installation\n\n## Configure credentials\nYou'll need to ask Dmitry for the `PYPI_API_TOKEN`.\n`poetry config pypi-token.pypi $PYPI_API_TOKEN`\n\n## Package\n`poetry build`\n\n## Publish\n`poetry publish`",
    'author': 'Dmitry Lesnik',
    'author_email': 'dmitry@stratyfy.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/stratyfy/probabilistic-rule-engine',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
}


setup(**setup_kwargs)
