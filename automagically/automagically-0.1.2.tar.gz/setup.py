# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['automagically',
 'automagically.services',
 'automagically.services.emails',
 'automagically.services.emails.helpers',
 'automagically.services.sms',
 'automagically.services.sms.helpers',
 'tests']

package_data = \
{'': ['*']}

install_requires = \
['fire==0.4.0', 'loguru>=0.6.0,<0.7.0', 'python-dotenv>=0.20.0,<0.21.0']

extras_require = \
{'dev': ['tox>=3.20.1,<4.0.0',
         'virtualenv>=20.2.2,<21.0.0',
         'pip>=20.3.1,<21.0.0',
         'twine>=3.3.0,<4.0.0',
         'pre-commit>=2.12.0,<3.0.0',
         'toml>=0.10.2,<0.11.0'],
 'doc': ['mkdocs>=1.1.2,<2.0.0',
         'mkdocs-include-markdown-plugin>=1.0.0,<2.0.0',
         'mkdocs-material>=6.1.7,<7.0.0',
         'mkdocstrings>=0.13.6,<0.14.0',
         'mkdocs-autorefs==0.1.1'],
 'test': ['black==20.8b1',
          'isort==5.6.4',
          'flake8==3.8.4',
          'flake8-docstrings>=1.6.0,<2.0.0',
          'pytest==6.1.2',
          'pytest-cov==2.10.1']}

entry_points = \
{'console_scripts': ['automagically = automagically.cli:main']}

setup_kwargs = {
    'name': 'automagically',
    'version': '0.1.2',
    'description': 'Python SDK für Automagically.',
    'long_description': '# 🔥  Automagically  Python Client\n\n[![PyPi](https://img.shields.io/pypi/v/automagically.svg)](https://pypi.python.org/pypi/automagically)\n[![PyPi](https://img.shields.io/pypi/pyversions/automagically)](https://pypi.python.org/pypi/automagically)\n[![ReadTheDocs](https://readthedocs.org/projects/automagically/badge/?version=latest)](https://automagically.readthedocs.io/en/latest/?version=latest)\n[![Gitter](https://badges.gitter.im/binaryai/community.svg)](https://gitter.im/automagically-hq/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)\n\n## Introduction\n\nAutomagically is Foundation as a Service. We work at your finger tips to provide you with the management tools, APIs and SDKs to build software.\n\n## Get started\n\n### Installation\n\n```shell\npip install automagically\n\nexport AUTOMAGICALLY_API_KEY=....\n```\n\n### Code\n\n```python\nfrom automagically import Client\n\nAUTOMAGICALLY_API_KEY = os.getenv("AUTOMAGICALLY_API_KEY")\n\nclient = Client(AUTOMAGICALLY_API_KEY)\n\n```\n\nYou find more examples in the `/examples` folder.\n\n## Documentation\n\nWIP\n\n## Get your API key\n\nApply for early access at <https://automagically.cloud>.\n',
    'author': 'Jens Neuhaus',
    'author_email': 'hey@automagically.cloud',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/automagically-cloud/automagically',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0',
}


setup(**setup_kwargs)
