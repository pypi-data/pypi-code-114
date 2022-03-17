# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_another_jwt_auth']

package_data = \
{'': ['*']}

install_requires = \
['PyJWT>=2.3.0,<3.0.0',
 'cryptography>=36.0.2,<37.0.0',
 'fastapi>=0.75.0,<0.76.0']

setup_kwargs = {
    'name': 'fastapi-another-jwt-auth',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Mariusz Masztalerczuk',
    'author_email': 'mariusz@masztalerczuk.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
