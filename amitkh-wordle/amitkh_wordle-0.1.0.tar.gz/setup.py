# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['amitkh_wordle']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.22.3,<2.0.0',
 'scipy>=1.8.0,<2.0.0',
 'tqdm>=4.63.0,<5.0.0',
 'typer>=0.4.0,<0.5.0',
 'wordfreq>=3.0.0,<4.0.0']

entry_points = \
{'console_scripts': ['wordle = amitkh_wordle.wordle:app']}

setup_kwargs = {
    'name': 'amitkh-wordle',
    'version': '0.1.0',
    'description': 'Entropy based Wordle Solver (CLI). Inspired by 3 Blue 1 Brown',
    'long_description': '## Entropy based wordle solver\n\nCLI built with Typer\n\n## Installation\n#### Install dependencies\nRun\n```\npip install -r requirements.txt\n```\n',
    'author': 'Amit Kumar',
    'author_email': 'amitkh@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/amit-kumarh/wordle-solver',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
