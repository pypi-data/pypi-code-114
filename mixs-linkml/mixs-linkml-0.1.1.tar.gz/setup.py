# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['release']

package_data = \
{'': ['*'],
 'release': ['graphql/*',
             'jsonld/*',
             'jsonschema/*',
             'owl/*',
             'prefixmap/*',
             'protobuf/*',
             'shacl/*',
             'shex/*',
             'sqlschema/*']}

install_requires = \
['linkml>=1.1.13', 'mkdocs', 'pandas']

setup_kwargs = {
    'name': 'mixs-linkml',
    'version': '0.1.1',
    'description': 'A LinkML (https://linkml.io/) model of the MIxS standard (https://gensc.org/mixs/)',
    'long_description': None,
    'author': 'GSC',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
