# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['github',
 'github.methods',
 'github.methods.activity',
 'github.methods.activity.events',
 'github.methods.activity.feeds',
 'github.methods.activity.notifications',
 'github.methods.activity.starring',
 'github.methods.activity.watching',
 'github.methods.auth',
 'github.methods.base',
 'github.methods.organizations',
 'github.methods.organizations.blocking',
 'github.methods.organizations.custom',
 'github.methods.organizations.members',
 'github.methods.organizations.outside_collabarators',
 'github.methods.organizations.webhooks',
 'github.methods.rate_limit',
 'github.methods.repos',
 'github.methods.search',
 'github.methods.users',
 'github.methods.users.blocking',
 'github.methods.users.emails',
 'github.methods.users.followers',
 'github.types',
 'github.utils']

package_data = \
{'': ['*']}

install_requires = \
['arrow>=1.2.2,<2.0.0', 'python-decouple>=3.6,<4.0', 'requests>=2.27.1,<3.0.0']

setup_kwargs = {
    'name': 'pyghc',
    'version': '0.1.0',
    'description': 'A Python Client for the GitHub REST API',
    'long_description': '# PyGithub\nA Python Client for the GitHub REST API\n',
    'author': 'taleb.zarhesh',
    'author_email': 'taleb.zarhesh@gmail.com',
    'maintainer': 'taleb.zarhesh',
    'maintainer_email': 'taleb.zarhesh@gmail.com',
    'url': 'https://github.com/appheap/PyGithub',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
