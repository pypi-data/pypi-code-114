# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dbnomics_solr', 'dbnomics_solr.services']

package_data = \
{'': ['*']}

install_requires = \
['daiquiri>=3.0.1,<4.0.0',
 'dbnomics-data-model>=0.13.23,<0.14.0',
 'dirhash>=0.2.1,<0.3.0',
 'environs>=9.5.0,<10.0.0',
 'orjson>=3.6.7,<4.0.0',
 'pysolr>=3.9.0,<4.0.0',
 'python-slugify>=6.1.1,<7.0.0',
 'requests>=2.27.1,<3.0.0',
 'solrq>=1.1.1,<2.0.0',
 'tenacity>=8.0.1,<9.0.0',
 'typer>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['dbnomics-solr = dbnomics_solr.cli:app']}

setup_kwargs = {
    'name': 'dbnomics-solr',
    'version': '1.1.0',
    'description': 'Index DBnomics data with Apache Solr for full-text and faceted search',
    'long_description': None,
    'author': 'Christophe Benz',
    'author_email': 'christophe.benz@nomics.world',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://git.nomics.world/dbnomics/dbnomics-solr',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
