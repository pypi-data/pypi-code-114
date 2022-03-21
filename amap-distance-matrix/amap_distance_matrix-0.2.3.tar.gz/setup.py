# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['amap_distance_matrix',
 'amap_distance_matrix.schemas',
 'amap_distance_matrix.services']

package_data = \
{'': ['*']}

install_requires = \
['PyMySQL>=1.0.2,<2.0.0',
 'aiohttp>=3.8.1,<4.0.0',
 'polyline>=1.4.0,<2.0.0',
 'pydantic==1.8.2',
 'python-geohash>=0.8.5,<0.9.0',
 'redis>=4.1.4,<5.0.0',
 'sqlalchemy-pydantic-orm>=0.1.0,<0.2.0']

setup_kwargs = {
    'name': 'amap-distance-matrix',
    'version': '0.2.3',
    'description': 'amap distance matrix service based on Redis and MySQL',
    'long_description': '### distance_matrix \n- name = "amap_distance_matrix"\n- version = "0.2.3"\n- description = "amap distance matrix service based on Redis and MySQL"\n- authors = ["Euraxluo <euraxluo@outlook.com>"]\n- license = "The MIT LICENSE"\n- readme = "README.md"\n- homepage = "https://github.com/Euraxluo/distance_matrix"\n- repository = "https://github.com/Euraxluo/distance_matrix"\n\n#### install\n`pip install amap-distance-matrix`\n\n![](https://gitee.com/Euraxluo/images/raw/master/pycharm/MIK-RHfzjB.png)\n',
    'author': 'Euraxluo',
    'author_email': 'euraxluo@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Euraxluo/distance_matrix',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
