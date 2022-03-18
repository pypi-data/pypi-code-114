# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['orm_alchemy']

package_data = \
{'': ['*']}

install_requires = \
['arrow>=1.2.2,<2.0.0',
 'inflection>=0.5.1,<0.6.0',
 'pymysql>=1.0.2,<2.0.0',
 'sqlalchemy>=1.4.31,<2.0.0',
 'sqlalchemy_utils>=0.38.2,<0.39.0']

setup_kwargs = {
    'name': 'orm-alchemy',
    'version': '0.1.11',
    'description': '',
    'long_description': None,
    'author': 'NamTH',
    'author_email': 'namth2302@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
