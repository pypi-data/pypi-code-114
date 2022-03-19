# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['djp_sepa', 'djp_sepa.migrations']

package_data = \
{'': ['*'], 'djp_sepa': ['locale/de_DE/LC_MESSAGES/*']}

install_requires = \
['django-localflavor>=3.1,<4.0',
 'django-payments>=1.0.0,<2.0.0',
 'sepaxml>=2.5.0,<3.0.0']

setup_kwargs = {
    'name': 'django-payments-sepa',
    'version': '1.1.1',
    'description': 'django-payments provider for SEPA',
    'long_description': None,
    'author': 'Dominik George',
    'author_email': 'dominik.george@teckids.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://edugit.org/AlekSIS/libs/django-payments-sepa',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
