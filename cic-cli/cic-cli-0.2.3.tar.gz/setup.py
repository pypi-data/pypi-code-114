# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cic',
 'cic.cmd',
 'cic.contract',
 'cic.contract.components',
 'cic.ext.eth',
 'cic.runnable',
 'cmd',
 'eth']

package_data = \
{'': ['*'],
 'cic': ['configs/docker/*',
         'configs/local/*',
         'configs/mainnet/*',
         'configs/testnet/*',
         'data/*',
         'data/config/*',
         'schema/*']}

modules = \
['cic_cmd']
install_requires = \
['cbor2==5.4.1',
 'chainlib>=0.0.17,<0.1.0',
 'cic-types>=0.2.1a8,<0.3.0',
 'confini>=0.5.3,<0.6.0',
 'funga-eth>=0.5.5,<0.6.0']

extras_require = \
{'eth': ['chainlib-eth>=0.0.25,<0.1.0',
         'eth-token-index>=0.2.4,<0.3.0',
         'eth-address-index>=0.2.4,<0.3.0',
         'okota>=0.2.5,<0.3.0',
         'cic_eth_registry>=0.6.6,<0.7.0',
         'cic_contracts>=0.0.5,<0.1.0']}

entry_points = \
{'console_scripts': ['cic = cic.runnable.cic_cmd:main']}

setup_kwargs = {
    'name': 'cic-cli',
    'version': '0.2.3',
    'description': 'Generic cli tooling for the CIC token network',
    'long_description': '# CIC Token Deployment Tool\n[![Status](https://ci.grassecon.net/api/badges/cicnet/cic-cli/status.svg)](https://ci.grassecon.net/grassrootseconomics/cic)\n[![Version](https://img.shields.io/pypi/v/cic-cli?color=green)](https://pypi.org/project/cic/)\n\nCIC-CLI provides tooling to generate and publish metadata in relation to\ntoken deployments.\n\n```shell\npip install cic-cli[eth]\n```\n## Usage\n### Using the wizard  \nFirst make sure that you edit the configs below to add your paths for `[auth]keyfile_path` and `[wallet]keyfile`\nThe configs are located in `~/.config/cic/cli/config/`\n```\n# Local\ncic wizard ./somewhere -c ~/.config/cic/cli/config/docker\n\n# Test Net\ncic wizard ./somewhere -c ~/.config/cic/cli/config/testnet\n```\n### Modular\nSome of the concepts described below assume familiarity with base\nconcepts of the CIC architecture. Please refer to the appropriate\ndocumentation for more information.\n\nTo initialize a new token deployment for the EVM:\n\n```shell\ncic init --target eth --name <token_name> --symbol <token_symbol> --precision <token_value_precision> <settings_folder>\n```\n\nTo automatically fill in settings detected in the network for the EVM:\n\n```shell\ncic ext --registry <contract_registry_address> -d <settings_folder> -i <chain_spec> -p <rpc_endpoint> eth\n```\n\n\n## Structure of the components\n\n![image](./doc/sphinx/components.svg)\n\nCIC-CLI is designed to interface any network type backend. The current\nstate of the package contains interface to EVM only. Thus, the examples\nbelow are limited to the context of the EVM.\n\n## Development\n### Requirements\n - Install [poetry](https://python-poetry.org/docs/#installation) \n\n### Setup\n\n```\n poetry install -E eth\n```\n\n### Running the CLI\n\n```bash\n poetry run cic -h\n```\n\n```bash\n poetry run cic wizard ./somewhere -c ./config/docker\n```\n### Importing a wallet from metamask\n- Export the accounts private key [Instructions](https://metamask.zendesk.com/hc/en-us/articles/360015289632-How-to-Export-an-Account-Private-Key)\n- Save the private key to a file\n- Run `eth-keyfile -k <file> > ~/.config/cic/keystore/keyfile.json`\n\n###  Port Forwarding\n<details>\n<summary>Install Kubectl</summary>\n\n```bash\nsudo apt-get update\nsudo apt-get install -y apt-transport-https ca-certificates curl\nsudo curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg\necho "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list\nsudo apt-get update\nsudo apt-get install -y kubectl\n```\n</details>\n\n- Download testnet cluster config from https://cloud.digitalocean.com/kubernetes/clusters\n- Move the config to `$HOME/.kube/`\n- Run `kubectl -n grassroots --kubeconfig=$HOME/.kube/<config_file_name>.yaml get pods`  \n- Copy the name of the meta pod (e.g `cic-meta-server-67dc7c6468-8rhdq`)\n- Port foward the meta pod to the local machine using `kubectl port-forward pods/<name_of_meta_pod> 6700:8000 -n grassroots --kubeconfig=$HOME/.kube/<config_file_name>.yaml`\n- Clone this repository to your local machine\n- Run `poetry install -E eth` in the repo root\n- Open `./cic/config/testnet/config.ini` and change\n  - [auth]keyfile_path \n  - [wallet]key_file\n- Open a new terminal and run `poetry run cic wizard -c ./cic/config/testnet ./somewhere` \n### Tests\n\n```\npoetry run pytest\n```\n',
    'author': 'Louis Holbrook',
    'author_email': 'dev@holbrook.no',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://git.grassecon.net/cicnet/cic-cli',
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
