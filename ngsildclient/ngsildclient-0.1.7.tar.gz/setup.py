# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ngsildclient',
 'ngsildclient.api',
 'ngsildclient.api.helper',
 'ngsildclient.model',
 'ngsildclient.model.helper',
 'ngsildclient.utils']

package_data = \
{'': ['*']}

install_requires = \
['geojson>=2.5.0,<3.0.0', 'requests>=2.26.0,<3.0.0']

setup_kwargs = {
    'name': 'ngsildclient',
    'version': '0.1.7',
    'description': 'A Python library that helps building NGSI-LD entities and interacting with a NGSI-LD Context Broker',
    'long_description': '# The ngsildclient library\n\n[![PyPI](https://img.shields.io/pypi/v/ngsildclient.svg)](https://pypi.org/project/ngsildclient/)\n[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)\n\n## Overview\n\n **ngsildclient** is a Python library that helps building NGSI-LD entities and allows to interact with a NGSI-LD Context Broker.\n\n The library primary purpose is to **ease and speed up the development of a NGSI Agent** and is also **useful for Data Modeling in the design stage**.\n\n## Key Features\n\n### Build NGSI-LD entities\n\nThe task of building a large NGSI-LD compliant entity is tedious, error-prone and results in a significant amount of code. \n\n**ngsildclient** provides primitives to build and manipulate NGSI-LD compliant entities without effort, in respect with the [ETSI specifications](https://www.etsi.org/committee/cim).\n\n### Implement the NGSI-LD API\n\n**ngsildclient** provides a NGSI-LD API Client implementation.\n\nActing as a Context Producer/Consumer **ngsildclient** is able to send/receive NGSI-LD entities to/from the Context Broker for creation and other operations.\n\nThe library wraps a large subset of the API endpoints and supports batch operations, queries, subscriptions.\n\n## Where to get it\n\nThe source code is currently hosted on GitHub at :\nhttps://github.com/Orange-OpenSource/python-ngsild-client\n\nBinary installer for the latest released version is available at the [Python\npackage index](https://pypi.org/project/ngsildclient).\n\n```sh\npip install ngsildclient\n```\n\n## Installation\n\n**ngsildclient** requires Python 3.9+.\n\nOne should use a virtual environment. For example with pyenv.\n\n```sh\nmkdir myagent && cd myagent\npyenv virtualenv 3.10.2 myagent\npyenv local myagent\npip install ngsildclient\n```\n\n## Documentation\n\nUser guide is available on [Read the Docs](https://ngsildclient.readthedocs.io/en/latest/index.html).\n\n## License\n\n[Apache 2.0](LICENSE)\n',
    'author': 'fbattello',
    'author_email': 'fabien.battello@orange.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Orange-OpenSource/python-ngsild-client',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
