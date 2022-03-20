# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aleksis',
 'aleksis.apps.tezor',
 'aleksis.apps.tezor.migrations',
 'aleksis.apps.tezor.models',
 'aleksis.apps.tezor.util']

package_data = \
{'': ['*'],
 'aleksis.apps.tezor': ['locale/*',
                        'locale/de_DE/LC_MESSAGES/*',
                        'static/*',
                        'templates/templated_email/*',
                        'templates/tezor/client/*',
                        'templates/tezor/invoice/*',
                        'templates/tezor/invoice_group/*']}

install_requires = \
['aleksis-core>=2.8.1.dev0,<3.0.0',
 'django-payments-sepa>=1.0.1,<2.0.0',
 'django-payments[sofort]>=1.0.0,<2.0.0']

entry_points = \
{'aleksis.app': ['tezor = aleksis.apps.tezor.apps:DefaultConfig']}

setup_kwargs = {
    'name': 'aleksis-app-tezor',
    'version': '1.2',
    'description': 'AlekSIS (School Information System)\u200a—\u200aApp Tezor (account and payment system)',
    'long_description': 'AlekSIS (School Information System)\u200a—\u200aApp Tezor (account and payment system)\n==================================================================================================\n\nAlekSIS\n-------\n\nThis is an application for use with the `AlekSIS®`_ platform.\n\nFeatures\n--------\n\nThe author of this app did not describe it yet.\n\nLicence\n-------\n\n::\n\n  Copyright © 2022 Dominik George <dominik.george@teckids.org>\n  Copyright © 2022 Tom Teichler <tom.teichler@teckids.org>\n\n  Licenced under the EUPL, version 1.2 or later\n\nPlease see the LICENCE.rst file accompanying this distribution for the\nfull licence text or on the `European Union Public Licence`_ website\nhttps://joinup.ec.europa.eu/collection/eupl/guidelines-users-and-developers\n(including all other official language versions).\n\nTrademark\n---------\n\nAlekSIS® is a registered trademark of the AlekSIS open source project, represented\nby Teckids e.V. Please refer to the `trademark policy`_ for hints on using the trademark\nAlekSIS®.\n\n.. _AlekSIS®: https://edugit.org/AlekSIS/AlekSIS\n.. _European Union Public Licence: https://eupl.eu/\n.. _trademark policy: https://aleksis.org/pages/about\n',
    'author': 'Dominik George',
    'author_email': 'dominik.george@teckids.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://aleksis.org',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
