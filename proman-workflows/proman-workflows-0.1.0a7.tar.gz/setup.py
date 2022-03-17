# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['proman_workflows',
 'proman_workflows.container',
 'proman_workflows.docs',
 'proman_workflows.executable',
 'proman_workflows.formatter',
 'proman_workflows.git',
 'proman_workflows.package',
 'proman_workflows.pki',
 'proman_workflows.qa',
 'proman_workflows.sca',
 'proman_workflows.sca.security',
 'proman_workflows.system',
 'proman_workflows.templates',
 'proman_workflows.web']

package_data = \
{'': ['*'],
 'proman_workflows': ['_vendor/gitignore/*',
                      '_vendor/gitignore/.github/*',
                      '_vendor/gitignore/Global/*',
                      '_vendor/gitignore/community/*',
                      '_vendor/gitignore/community/AWS/*',
                      '_vendor/gitignore/community/DotNet/*',
                      '_vendor/gitignore/community/Elixir/*',
                      '_vendor/gitignore/community/GNOME/*',
                      '_vendor/gitignore/community/Golang/*',
                      '_vendor/gitignore/community/Java/*',
                      '_vendor/gitignore/community/JavaScript/*',
                      '_vendor/gitignore/community/Linux/*',
                      '_vendor/gitignore/community/PHP/*',
                      '_vendor/gitignore/community/Python/*',
                      '_vendor/gitignore/community/embedded/*']}

install_requires = \
['PyInputPlus>=0.2.12,<0.3.0',
 'compendium>=0.1.1-alpha.0,<0.2.0',
 'invoke>=1.5.0,<2.0.0',
 'keyring>=23.2.1,<24.0.0',
 'proman-common>=0.1.1-alpha.1,<0.2.0',
 'pygit2>=1.7,<2.0',
 'python-gnupg>=0.4.7,<0.5.0',
 'stevedore>=3.4.0,<4.0.0']

extras_require = \
{':python_version >= "3.7" and python_version < "3.8"': ['cached-property>=1.5.2,<2.0.0'],
 ':sys_platform == "linux"': ['SecretStorage>=3.3.1,<4.0.0']}

entry_points = \
{'console_scripts': ['workflow = proman_workflows:workflow.run',
                     'workflow-setup = proman_workflows.setup:setup.run',
                     'workflow-tools = proman_workflows:workflow_tools.run'],
 'proman.workflows.container.compose': ['docker_compose = '
                                        'proman_workflows.container.docker:namespace',
                                        'podman_compose = '
                                        'proman_workflows.container.podman:namespace'],
 'proman.workflows.docs': ['mkdocs = proman_workflows.docs.mkdocs:namespace'],
 'proman.workflows.formatter': ['autopep8 = '
                                'proman_workflows.formatter.autopep8:namespace',
                                'black = '
                                'proman_workflows.formatter.black:namespace',
                                'isort = '
                                'proman_workflows.formatter.isort:namespace'],
 'proman.workflows.mock': ['original = mock_workflow.mock.original:namespace',
                           'update = mock_workflow.mock.update:namespace'],
 'proman.workflows.package': ['flit = proman_workflows.package.flit:namespace',
                              'poetry = '
                              'proman_workflows.package.poetry:namespace',
                              'setuptools = '
                              'proman_workflows.package.setuptools:namespace',
                              'twine = '
                              'proman_workflows.package.twine:namespace'],
 'proman.workflows.pki': ['gpg = proman_workflows.pki.gpg:namespace',
                          'tls = proman_workflows.pki.tls:namespace'],
 'proman.workflows.qa': ['behave = proman_workflows.qa.behave:namespace',
                         'pytest = proman_workflows.qa.pytest:namespace'],
 'proman.workflows.sca': ['bandit = '
                          'proman_workflows.sca.security.bandit:namespace',
                          'flake8 = proman_workflows.sca.flake8:namespace',
                          'mypy = proman_workflows.sca.mypy:namespace',
                          'safety = '
                          'proman_workflows.sca.security.safety:namespace'],
 'proman.workflows.system': ['test-infra = '
                             'proman_workflows.system.test_infra:namespace'],
 'proman.workflows.vcs': ['git = proman_workflows.git:namespace']}

setup_kwargs = {
    'name': 'proman-workflows',
    'version': '0.1.0a7',
    'description': 'Task-runner to automate projects.',
    'long_description': '# proman-workflows\n\n[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://spdx.org/licenses/MPL-2.0)\n[![Build Status](https://travis-ci.org/python-proman/proman-workflows.svg?branch=master)](https://travis-ci.org/python-proman/proman-workflows)\n[![codecov](https://codecov.io/gh/python-proman/proman-workflows/branch/master/graph/badge.svg)](https://codecov.io/gh/python-proman/proman-workflows)\n\n## Overview\n\nThis project is a task runner to help automate common development tasks for\nprojects using Python.\n\nThe goal of this effort is help implement DevSecOps practices consistly with\nthe Software Development Lifecycle (SDLC) without burdening developers.\n\nThe objectives for achieving this goal are:\n- Enforce use of commit signing\n- Introduce QA tools early in development\n- SAST, SCA, and DAST integration\n- Encapulate processes for seamless integration with CI/CD systems\n- Make TUF compliant packages for PyPI\n\n## Install\n\nThe project can be installed using the following command:\n\n```\npip install proman-workflows\n```\n\nThe above will only install the workflows but not all dependencies. The\nadditional dependencies can be install with:\n\n```\npip install proman-workflow[all]\n```\n\n### Usage\n\nCurrently, there are three command line utilities included with this install.\nThis is due to the primary CLI tool being under heavy development.\n\nThe `workflow-tools` command provides direct access to each of integrations\nprovided by the task runner. It can either be used directory or extended as\na library for additional workflows.\n\nThe `workflow-setup` command\n\nThe `workflow` command is the intended CLI for the task runner but is still\nunder development. It will allow control of integrated tools through abstracted\nphases accessible to a developer. The functionality is still imited at this time.\n\n### Setup\n\nSetup a signing key for development:\n\n```\nworkflow-tools setup\n```\n\n## FAQ\n\nQ: Why should developers use this?\nA: Coodinating procedures and setup for multiple team members and projects is difficult and error\nprone. Task runners are purpose built to solve this problem.\n\nQ: Why not include this using project templates?\nA: Since this is distributed as a library updates and changes can be much more easilly distributed.\n\nQ: Why not use Invocations\nA: While this project is inspired by Invocations, it does not support a pluggable architecture.\n\n## Refereces\n\n- https://theupdateframework.io/\n- https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.04232020.pdf\n',
    'author': 'Jesse P. Johnson',
    'author_email': 'jpj6652@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/python-protools/proman-workflows',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
