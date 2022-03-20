# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kosmorro', 'kosmorro.i18n']

package_data = \
{'': ['*'],
 'kosmorro': ['assets/moonphases/png/*',
              'assets/moonphases/svg/*',
              'assets/pdf/*',
              'assets/png/*',
              'assets/svg/*',
              'locales/*',
              'locales/de/LC_MESSAGES/*',
              'locales/es/LC_MESSAGES/*',
              'locales/fr/LC_MESSAGES/*',
              'locales/nb_NO/LC_MESSAGES/*',
              'locales/nl/LC_MESSAGES/*',
              'locales/ru/LC_MESSAGES/*']}

install_requires = \
['Babel>=2.9,<3.0',
 'importlib-metadata>=4.11,<5.0',
 'kosmorrolib>=1.0,<2.0',
 'python-dateutil>=2.8,<3.0',
 'tabulate>=0.8,<0.9',
 'termcolor>=1.1,<2.0']

entry_points = \
{'console_scripts': ['kosmorro = kosmorro.__main__:main']}

setup_kwargs = {
    'name': 'kosmorro',
    'version': '0.10.10',
    'description': 'A program to compute the ephemerides.',
    'long_description': None,
    'author': 'Jérôme Deuchnord',
    'author_email': 'jerome@deuchnord.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
