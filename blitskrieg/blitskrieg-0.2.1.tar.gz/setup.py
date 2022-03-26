# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['blitskrieg', 'blitskrieg.utils']

package_data = \
{'': ['*'], 'blitskrieg': ['share/*']}

install_requires = \
['PyYAML>=5.4.1,<6.0.0',
 'boltlight-proto>=2.0.0,<3.0.0',
 'click>=8.0.4,<9.0.0',
 'docker-compose>=1.28.5,<2.0.0',
 'docker>=5.0.3,<6.0.0',
 'googleapis-common-protos>=1.53.0,<2.0.0',
 'grpcio>=1.43.0,<2.0.0',
 'protobuf>=3.19.1,<4.0.0',
 'requests>=2.25.1,<3.0.0']

entry_points = \
{'console_scripts': ['bli = blitskrieg.bli:entrypoint',
                     'blitskrieg = blitskrieg.blitskrieg:start']}

setup_kwargs = {
    'name': 'blitskrieg',
    'version': '0.2.1',
    'description': 'The Bitcoin Lightning Integration Test Service',
    'long_description': "# BLITSkrieg: Bitcoin Lightning Integration Test Service\n\nBLITSkrieg is a gRPC server in Python that aims to provide a set of utilities\nto test Bitcoin and Lightning Network services.\n\nIt uses [boltlight](https://gitlab.com/hashbeam/boltlight) in order to hide\nthe differences between the different LN node implementations.\n\nCurrently the available services are:\n* `bitcoind` <sup>[1]</sup>\n* `boltlight` <sup>[2]</sup>\n* `c-lightning`\n* `eclair`\n* `electrs` <sup>[3]</sup>\n* `electrum`\n* `lnd`\n\n#### Notes\n\n1. docker image always necessary\n2. docker image necessary to call LN-related commands\n3. docker image necessary to run `electrum`\n\n## System dependencies\n\n- Linux or macOS (_Windows may work, but is not supported_)\n- Python 3.9+\n- poetry\n- docker\n\n## Build\n\nIn order to build the docker image for BLITSkrieg, run:\n```bash\n# production mode\n$ ./unix_helper build\n\n# development mode\n$ ./unix_helper build-dev\n```\n\nProduction mode does not include the package dev dependencies.\n\nPre-built (production mode) images for the latest versions can be downloaded\nfrom GitLab's [container\nregistry](https://gitlab.com/hashbeam/blitskrieg/container_registry).\n\n## Run\n\nIn order to launch the docker image of BLITSkrieg, run:\n```bash\n# production mode\n$ ./unix_helper run\n\n# development mode\n$ ./unix_helper run-dev\n```\n\n## CLI\n\nBLITSkrieg features a Command Line Interface, named `bli`. It can be installed\nand called from the project directory.\n\nIn order to install the project, run:\n```bash\n$ poetry install\n```\n\nIn order to run `bli`, call it via poetry:\n```bash\n$ poetry run bli\n```\n\n`bli` supports shell completion for bash and zsh (the shell needs to have\ncompletion support enabled). It can be enabled sourcing the appropriate file\nfor the running shell, from the project directory:\n```bash\n$ . ./blitskrieg/share/complete-bli.bash\n$ . ./blitskrieg/share/complete-bli.zsh\n```\n\n## Use\n\nIn order to run a command on BLITSkrieg, you can directly call it by making\na gRPC call to it, or you can use its CLI.\n\nTo get a list of available CLI commands, run:\n```bash\n$ poetry run bli --help\n```\n\nIn order to perform any action in BLITSkrieg, you first need to create a LN\nstack. To do so, call:\n```bash\n$ poetry run bli createstack [--<implementation>=<number_of_nodes>]\n```\n\nIf you do not specify any LN node, this will run a single `bitcoind` instance\nand only Bitcoin-related commands will be available.\n\nVisit our [docker repository](https://gitlab.com/hashbeam/docker) in\norder to build the required services.\nOtherwise, if the needed docker images are not available, they will be pulled\nfrom hashbeam's GitLab container registry.\n",
    'author': 'Hashbeam',
    'author_email': 'hashbeam@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/hashbeam/blitskrieg',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9.0,<4.0.0',
}


setup(**setup_kwargs)
