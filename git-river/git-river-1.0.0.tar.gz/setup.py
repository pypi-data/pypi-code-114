# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['git_river', 'git_river.commands', 'git_river.ext', 'git_river.tests']

package_data = \
{'': ['*']}

install_requires = \
['GitPython',
 'PyGithub>=1.55,<2.0',
 'appdirs',
 'click',
 'colorama>=0.4.4,<0.5.0',
 'giturlparse',
 'inflect>=5.3.0,<6.0.0',
 'pydantic>=1.8.2,<2.0.0',
 'python-gitlab',
 'structlog']

entry_points = \
{'console_scripts': ['git-river = git_river.cli:main']}

setup_kwargs = {
    'name': 'git-river',
    'version': '1.0.0',
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
