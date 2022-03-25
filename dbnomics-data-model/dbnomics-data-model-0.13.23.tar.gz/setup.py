# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dbnomics_data_model',
 'dbnomics_data_model.model',
 'dbnomics_data_model.scripts',
 'dbnomics_data_model.storage',
 'dbnomics_data_model.storage.adapters.filesystem',
 'dbnomics_data_model.storage.adapters.filesystem.model',
 'dbnomics_data_model.storage.adapters.filesystem.model.json_lines_variant',
 'dbnomics_data_model.storage.adapters.filesystem.model.tsv_variant']

package_data = \
{'': ['*']}

install_requires = \
['daiquiri>=3.0.1,<4.0.0',
 'dirsync>=2.2.5,<3.0.0',
 'jsonschema>=4.4.0,<5.0.0',
 'orjson>=3.6.7,<4.0.0',
 'pydantic>=1.9.0,<2.0.0',
 'pysimdjson>=4.0.3,<5.0.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'toolz>=0.11.2,<0.12.0',
 'typer>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['dbnomics-update-storage = '
                     'dbnomics_data_model.scripts.update_storage:app',
                     'dbnomics-validate-storage = '
                     'dbnomics_data_model.scripts.validate_storage:app']}

setup_kwargs = {
    'name': 'dbnomics-data-model',
    'version': '0.13.23',
    'description': 'Provide classes for DBnomics entities and a storage abstraction',
    'long_description': None,
    'author': 'DBnomics Team',
    'author_email': 'contact@nomics.world',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://git.nomics.world/dbnomics/dbnomics-data-model',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
