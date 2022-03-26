# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ktdg']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.22.2,<2.0.0',
 'pydantic>=1.9.0,<2.0.0',
 'ruamel.yaml>=0.17.20,<0.18.0',
 'typer>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['ktdg = ktdg.cli:run_cli']}

setup_kwargs = {
    'name': 'ktdg',
    'version': '0.1.2',
    'description': 'Library to simulate knowledge tracing datasets',
    'long_description': None,
    'author': 'Antoine Lefebvre-Brossard',
    'author_email': 'antoinelb@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/antoinelb/ktdg',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
