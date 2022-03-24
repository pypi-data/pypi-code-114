# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dgraph_orm',
 'dgraph_orm.ACL',
 'dgraph_orm.strawberry_helpers',
 'dgraph_orm.utils',
 'dgraph_orm.vendors.edgedb',
 'dgraph_orm.vendors.edgedb.gen']

package_data = \
{'': ['*']}

install_requires = \
['PyJWT',
 'black>=21.9b0,<22.0',
 'devtools>=0.8,<0.9',
 'fastapi',
 'gql[all]>=3.0.0b0,<4.0.0',
 'httpx>=0.19.0,<0.20.0',
 'orjson>=3.6.7,<4.0.0',
 'pydantic[email]>=1.9.0,<2.0.0',
 'requests>=2.26,<3.0',
 'retry>=0.9.2,<0.10.0']

setup_kwargs = {
    'name': 'dgraph-orm',
    'version': '0.2.8',
    'description': '',
    'long_description': None,
    'author': 'Jeremy Berman',
    'author_email': 'jerber@sas.upenn.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
