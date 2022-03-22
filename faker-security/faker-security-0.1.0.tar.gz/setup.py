# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['faker_security']

package_data = \
{'': ['*']}

install_requires = \
['faker>=8.2.1']

setup_kwargs = {
    'name': 'faker-security',
    'version': '0.1.0',
    'description': 'Faker provider for security related data',
    'long_description': '# Faker-Security\n\nProvider for [Faker](https://github.com/joke2k/faker)\nto generate random/fake data related to security.\n\n## Requirements\n\n- Faker\n- Python 3.9+\n\n## Installation and Usage\n\n- Add `faker-security` to your requirements\n- Install `faker-security` using `pip` or whatever package manager you use\n- Add the `SecurityProvider` during tests or wherever you use Faker\n\n```python\nfrom faker import Faker\nfrom faker_security.providers import SecurityProvider\n\nfake = Faker()\nfake.add_provider(SecurityProvider)\n\n# generate a CVSSv3 vector\nfake.cvss3()\n```\n\n## Provider Features\n\n- `cvss3`: generates a CVSS v3 vector\n- `cvss2`: generates a CVSS v2 vector\n- `version`: generates a [semver version number](https://semver.org/)\n- `npm_semver_range`: generates a [npm compatible semver version range](https://docs.npmjs.com/about-semantic-versioning)\n- `cwe`: generates a CWE identifier\n- `cve`: generates a CVE identifier\n\n## Developing\n\n- Install `poetry` and run `poetry install`\n- Install `pre-commit` and run `pre-commit install --install-hooks`\n\n## Testing\n\n`poetry run pytest` to run tests.\n',
    'author': 'Snyk Security R&D',
    'author_email': 'security-engineering@snyk.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/snyk/faker-security',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
