# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['vault_pki_agent', 'vault_pki_agent.watchers']

package_data = \
{'': ['*']}

install_requires = \
['cryptography>=36.0.2,<37.0.0', 'hvac>=0.11.2,<0.12.0']

entry_points = \
{'console_scripts': ['vault-pki-agent = vault_pki_agent.main:run']}

setup_kwargs = {
    'name': 'vault-pki-agent',
    'version': '0.1.0',
    'description': 'Tool for auto-renewal certificates and CRL from Vault PKI.',
    'long_description': '# Vault PKI Agent\n\nTool for auto-renewal certificates and CRL from Vault PKI.\n\n## Usage\n\nBasic usage:\n\n```shell\n  $ vault_pki_agent -c [CONFIG_PATH] -l [LOG_LEVEL]\n```\n\nLog level can be DEBUG (by default), INFO, WARNING, ERROR, CRITICAL\n\n## Configuration\n\nExample:\n\n```json\n{\n  "url": "http://111.111.111.111:8200",\n  "mount_point": "pki",\n  "auth": {\n    "method": "approle",\n    "role_id": "990ff41d-0448-f5d5-e405-22c05a23f976",\n    "secret_id": "92871b67-0ad6-a4d5-40cc-0d8fb64e2960"\n  },\n  "crl": {\n    "destination": "/etc/openvpn/keys/ca.crl"\n  },\n  "certificates": [\n    {\n      "role": "server",\n      "common_name": "server",\n      "crt_destination": "/etc/openvpn/keys/server.crt",\n      "key_destination": "/etc/openvpn/keys/server.key",\n      "hook": "systemctl restart openvpn"\n    }\n  ]\n}\n```\n\n## Release\n\n1. Bump version in `pyproject.toml` and `__init__.py` files\n2. Commit changes and create git tag with new version:\n\n```shell\n  $ git commit -am "Bump version"\n  $ git tag v0.2.0\n```\n\n3. Build and publish new library version:\n\n```shell\n  $ poetry build\n  $ poetry publish\n```\n\n4. Push:\n\n```shell\n  $ git push\n  $ git push --tags\n```\n\n## License\n\nVault PKI Agent is released under the MIT License. See the [LICENSE](LICENSE) file for more details.\n',
    'author': 'Anatoly Gusev',
    'author_email': 'a.gusev@sparklingtide.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.10,<4.0.0',
}


setup(**setup_kwargs)
