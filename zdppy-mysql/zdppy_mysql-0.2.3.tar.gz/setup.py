# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zdppy_mysql',
 'zdppy_mysql.libs',
 'zdppy_mysql.libs.aiomysql',
 'zdppy_mysql.libs.pymysql',
 'zdppy_mysql.libs.pymysql.constants']

package_data = \
{'': ['*']}

install_requires = \
['zdppy-log>=0.1.5,<0.2.0']

setup_kwargs = {
    'name': 'zdppy-mysql',
    'version': '0.2.3',
    'description': '使用python操作MySQL,同时支持同步版本和异步版本,支持事务',
    'long_description': None,
    'author': 'zhangdapeng',
    'author_email': 'pygosuperman@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
