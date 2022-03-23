# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['git_river', 'git_river.commands', 'git_river.ext', 'git_river.tests']

package_data = \
{'': ['*']}

install_requires = \
['GitPython>=3.1.27,<4.0.0',
 'PyGithub>=1.55,<2.0',
 'appdirs>=1.4.4,<2.0.0',
 'click>=8.0.4,<9.0.0',
 'colorama>=0.4.4,<0.5.0',
 'giturlparse>=0.10.0,<0.11.0',
 'inflect>=5.4.0,<6.0.0',
 'pydantic>=1.9.0,<2.0.0',
 'python-gitlab>=3.2.0,<4.0.0',
 'structlog>=21.5.0,<22.0.0']

entry_points = \
{'console_scripts': ['git-river = git_river.cli:main']}

setup_kwargs = {
    'name': 'git-river',
    'version': '1.2.0',
    'description': 'Tools for working with upstream repositories',
    'long_description': None,
    'author': 'Sam Clements',
    'author_email': 'sclements@datto.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
