# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['uw_saml2', 'uw_saml2.idp']

package_data = \
{'': ['*']}

install_requires = \
['Werkzeug>=2.0.2,<3.0.0', 'cachelib>=0.4.1,<0.5.0', 'onelogin>=2.0.3,<3.0.0']

extras_require = \
{'python3-saml': ['python3-saml>=1.14.0,<2.0.0']}

setup_kwargs = {
    'name': 'uw-saml',
    'version': '1.1.1',
    'description': 'A UW-specific adapter to the python3-saml package.',
    'long_description': None,
    'author': None,
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
