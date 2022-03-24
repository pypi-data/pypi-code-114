# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gladiator',
 'gladiator.generate',
 'gladiator.parse',
 'gladiator.prepare',
 'gladiator.resources',
 'gladiator.tools']

package_data = \
{'': ['*'],
 'gladiator.resources': ['data/*',
                         'templates/*',
                         'templates/_include/*',
                         'templates/_util/*',
                         'templates/loader/*',
                         'templates/resource_wrapper/*']}

install_requires = \
['ConfigArgParse>=1.5.3,<2.0.0',
 'Jinja2>=3.0.3,<4.0.0',
 'attrs>=20.3,<21.0',
 'pyyaml>=5.3,<6.0']

setup_kwargs = {
    'name': 'gladiator-gen',
    'version': '0.2.0',
    'description': 'Generate type-safe, zero-overhead OpenGL wrappers for C++',
    'long_description': None,
    'author': 'hellcat17',
    'author_email': 'dodgehellcat17@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/hellcat17/gladiator',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
