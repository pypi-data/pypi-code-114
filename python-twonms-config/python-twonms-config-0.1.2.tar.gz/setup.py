# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'python_twonms_config'}

packages = \
['tests', 'twonms', 'twonms.config']

package_data = \
{'': ['*']}

install_requires = \
['fire==0.4.0',
 'livereload>=2.6.3,<3.0.0',
 'loguru>=0.6.0,<0.7.0',
 'omegaconf>=2.1.1,<3.0.0',
 'python-dotenv>=0.19.2,<0.20.0']

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

setup_kwargs = {
    'name': 'python-twonms-config',
    'version': '0.1.2',
    'description': 'Python package to manage configs based on OmegaConf.',
    'long_description': '# Python 2NMS config manager\n\n<p align="center">\n<a href="https://pypi.python.org/pypi/python_twonms_config">\n    <img src="https://img.shields.io/pypi/v/python_twonms_config.svg"\n        alt = "Release Status">\n</a>\n\n<a href="https://github.com/mwallraf/python_twonms_config/actions">\n    <img src="https://github.com/mwallraf/python_twonms_config/actions/workflows/release.yml/badge.svg?branch=release" alt="CI Status">\n</a>\n\n<a href="https://mwallraf.github.io/python_twonms_config/">\n    <img src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" alt="Documentation Status">\n</a>\n\n</p>\n\nPython package to manage application configurations. This is a wrapper around the OmegaConf create function.\n\nThis package makes it easy to define parameters for your application. It\'s possible to define parameters in different ways (in order of precedence):\n\n-   programmatically defined default values\n-   environment variables/dotenv files\n-   configuration files in YAML format\n-   cli arguments\n\n## Documentation\n\nCheck out the [Github Docs](https://mwallraf.github.io/python_twonms_config/)\n\n## Features\n\n-   generates an [OmegaConf](https://omegaconf.readthedocs.io) dictionary object\n-   supports environment variables\n-   supports dotenv\n-   reads yaml config files\n-   supports cli parameters\n-   allows programmatic initialization of parameters\n\n## Credits\n\nThis package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [zillionare/cookiecutter-pypackage](https://github.com/zillionare/cookiecutter-pypackage) project template.\n',
    'author': 'Maarten Wallraf',
    'author_email': 'mwallraf@2nms.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mwallraf/python_twonms_config',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6.1,<4.0',
}


setup(**setup_kwargs)
