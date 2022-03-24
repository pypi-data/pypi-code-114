# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['captif_db',
 'captif_db.db',
 'captif_db.db.models',
 'captif_db.db.models.continuous',
 'captif_db.db.models.interval',
 'captif_db.helpers',
 'captif_db.loaders']

package_data = \
{'': ['*']}

install_requires = \
['captif-data-structures>=0.11,<0.12',
 'captif-db-config==0.10',
 'captif-slp>=0.7,<0.8',
 'mysqlclient>=2.0.3,<3.0.0',
 'numpy>=1.19.1,<2.0.0',
 'pandas>=1.1.0,<2.0.0',
 'schema>=0.7.2,<0.8.0',
 'toml>=0.10.1,<0.11.0']

setup_kwargs = {
    'name': 'captif-db',
    'version': '0.11',
    'description': '',
    'long_description': '\n# captif-db\n\nObject relational mapping for the CAPTIF database.\n\nThese are low-level methods.\n\n### Initialise database and generate a session object:\n\n```\nfrom captif_db.db import DbSession\nDbSession.global_init()\nsession = DbSession.factory()\n```\n\n### Import and use models:\n\n```\nfrom captif_db.db.models import Project\nprojects = session.query(Project).all()\n```\n',
    'author': 'John Bull',
    'author_email': 'john.bull@nzta.govt.nz',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
