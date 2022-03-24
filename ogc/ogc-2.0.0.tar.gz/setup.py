# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ogc', 'ogc.commands', 'ogc.tests']

package_data = \
{'': ['*']}

install_requires = \
['Mako>=1.1.6,<2.0.0',
 'PyYAML>=6.0,<7.0',
 'apache-libcloud>=3.5.0,<4.0.0',
 'celery[redis]>=5.2.3,<6.0.0',
 'click-didyoumean>=0.3.0,<0.4.0',
 'click>=8.0.4,<9.0.0',
 'colorama>=0.4.4,<0.5.0',
 'dict-deep>=4.1.2,<5.0.0',
 'dill>=0.3.4,<0.4.0',
 'gevent>=21.12.0,<22.0.0',
 'humanfriendly>=10.0,<11.0',
 'loguru>=0.6.0,<0.7.0',
 'melddict>=1.0.1,<2.0.0',
 'paramiko>=2.9.2,<3.0.0',
 'peewee>=3.14.10,<4.0.0',
 'psycopg2-binary>=2.9.3,<3.0.0',
 'python-dotenv>=0.19.2,<0.20.0',
 'retry>=0.9.2,<0.10.0',
 'rich>=12.0.1,<13.0.0',
 'scp>=0.14.4,<0.15.0',
 'sh>=1.14.2,<2.0.0']

entry_points = \
{'console_scripts': ['ogc = ogc.commands.base:start']}

setup_kwargs = {
    'name': 'ogc',
    'version': '2.0.0',
    'description': 'Provisioner',
    'long_description': None,
    'author': 'Adam Stokes',
    'author_email': '51892+adam-stokes@users.noreply.github.com',
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
