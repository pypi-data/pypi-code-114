# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['djfritz',
 'djfritz.admin',
 'djfritz.management',
 'djfritz.management.commands',
 'djfritz.migrations',
 'djfritz.models',
 'djfritz.tests',
 'djfritz.tests.fixtures',
 'djfritz_project',
 'djfritz_project.settings',
 'djfritz_project.tests']

package_data = \
{'': ['*'],
 'djfritz': ['locale/de/LC_MESSAGES/*', 'locale/en/LC_MESSAGES/*'],
 'djfritz_project': ['templates/admin/*']}

install_requires = \
['bx_django_utils',
 'bx_py_utils',
 'colorlog',
 'django',
 'django-debug-toolbar',
 'django-tools',
 'fritzconnection']

entry_points = \
{'console_scripts': ['devshell = djfritz_project.dev_shell:devshell_cmdloop',
                     'run_testserver = '
                     'djfritz_project.manage:start_test_server']}

setup_kwargs = {
    'name': 'django-fritzconnection',
    'version': '0.0.1a0',
    'description': 'Web based FritzBox management using Python/Django.',
    'long_description': '# django-fritzconnection\n\nWeb based FritzBox management using Python/Django.\n\nCurrent state: **planning**\n\n## Quick start for developers\n\n```\n~$ git clone https://github.com/jedie/django-fritzconnection.git\n~$ cd django-fritzconnection\n~/django-fritzconnection$ ./devshell.py\n...\nDeveloper shell - djfritz - v0.0.1.pre-alpha0\n...\n\n(djfritz) run_testserver\n```\n\n## versions\n\n* v0.0.1-alpha\n  * init the project\n',
    'author': 'JensDiemer',
    'author_email': 'git@jensdiemer.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jedie/django-fritzconnection',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0.0',
}


setup(**setup_kwargs)
