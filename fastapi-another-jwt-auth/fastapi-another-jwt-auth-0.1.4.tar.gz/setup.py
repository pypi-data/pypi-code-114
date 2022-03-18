# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_another_jwt_auth']

package_data = \
{'': ['*']}

install_requires = \
['PyJWT>=2.3.0,<3.0.0',
 'cryptography>=36.0.2,<37.0.0',
 'fastapi>=0.65.3,<0.66.0']

setup_kwargs = {
    'name': 'fastapi-another-jwt-auth',
    'version': '0.1.4',
    'description': '',
    'long_description': '<h1 align="left" style="margin-bottom: 20px; font-weight: 500; font-size: 50px; color: black;">\n  FastAPI Another JWT Auth\n</h1>\n\n![Tests](https://github.com/GlitchCorp/fastapi-another-jwt-auth/workflows/Tests/badge.svg)\n[![Coverage Status](https://coveralls.io/repos/github/GlitchCorp/fastapi-another-jwt-auth/badge.svg?branch=master)](https://coveralls.io/github/GlitchCorp/fastapi-another-jwt-auth?branch=master)\n[![PyPI version](https://badge.fury.io/py/fastapi-another-jwt-auth.svg)](https://badge.fury.io/py/fastapi-another-jwt-auth)\n[![Downloads](https://static.pepy.tech/personalized-badge/fastapi-another-jwt-auth?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/fastapi-another-jwt-auth)\n\n---\n\n**Documentation**: <a href="https://GlitchCorp.github.io/fastapi-another-jwt-auth" target="_blank">https://GlitchCorp.github.io/fastapi-another-jwt-auth</a>\n\n**Source Code**: <a href="https://github.com/GlitchCorp/fastapi-another-jwt-auth" target="_blank">https://github.com/GlitchCorp/fastapi-another-jwt-auth</a>\n\n---\n\n## Features\nFastAPI extension that provides JWT Auth support (secure, easy to use and lightweight), if you were familiar with flask-jwt-extended this extension suitable for you, cause this extension inspired by flask-jwt-extended 😀\n\n- Access tokens and refresh tokens\n- Freshness Tokens\n- Revoking Tokens\n- Support for WebSocket authorization\n- Support for adding custom claims to JSON Web Tokens\n- Storing tokens in cookies and CSRF protection\n\n## Installation\nThe easiest way to start working with this extension with pip\n\n```bash\npip install fastapi-another-jwt-auth\n```\n\nIf you want to use asymmetric (public/private) key signing algorithms, include the <b>asymmetric</b> extra requirements.\n```bash\npip install \'fastapi-another-jwt-auth[asymmetric]\'\n```\n\n## License\nThis project is licensed under the terms of the MIT license.\n',
    'author': 'Mariusz Masztalerczuk',
    'author_email': 'mariusz@masztalerczuk.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/GlitchCorp/fastapi-another-jwt-auth',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
