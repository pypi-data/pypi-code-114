# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['linkml_solr', 'linkml_solr.utils']

package_data = \
{'': ['*']}

install_requires = \
['SPARQLWrapper>=1.8.5,<2.0.0',
 'flatten-dict>=0.4.2,<0.5.0',
 'json-flattener>=0.1.9,<0.2.0',
 'linkml-runtime>=1.1.12,<2.0.0',
 'linkml>=1.1.15,<2.0.0',
 'pyparsing==2.4',
 'pysolr>=3.9.0,<4.0.0']

entry_points = \
{'console_scripts': ['lsolr = linkml_solr.cli:main']}

setup_kwargs = {
    'name': 'linkml-solr',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Chris Mungall',
    'author_email': 'cjm@berkeleybop.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.4,<4.0.0',
}


setup(**setup_kwargs)
