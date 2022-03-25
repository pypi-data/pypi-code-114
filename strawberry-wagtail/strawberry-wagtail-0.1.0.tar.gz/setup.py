# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['strawberry_wagtail']

package_data = \
{'': ['*']}

install_requires = \
['strawberry-graphql-django>=0.2.5,<0.3.0',
 'strawberry-graphql>=0.103.1,<0.104.0']

setup_kwargs = {
    'name': 'strawberry-wagtail',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Patrick Arminio',
    'author_email': 'patrick.arminio@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
