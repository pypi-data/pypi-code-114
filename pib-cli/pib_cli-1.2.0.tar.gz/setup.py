# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pib_cli',
 'pib_cli.cli',
 'pib_cli.cli.commands',
 'pib_cli.cli.commands.bases',
 'pib_cli.cli.commands.bases.fixtures',
 'pib_cli.cli.interface',
 'pib_cli.cli.interface.builtins',
 'pib_cli.cli.interface.custom',
 'pib_cli.config',
 'pib_cli.config.locale',
 'pib_cli.support',
 'pib_cli.support.container',
 'pib_cli.support.container.bases',
 'pib_cli.support.iterators',
 'pib_cli.support.iterators.bases',
 'pib_cli.support.iterators.bases.fixtures',
 'pib_cli.support.mixins',
 'pib_cli.support.user_configuration',
 'pib_cli.support.user_configuration.bases',
 'pib_cli.support.user_configuration.bases.fixtures',
 'pib_cli.support.user_configuration.selectors']

package_data = \
{'': ['*'],
 'pib_cli': ['bash/*'],
 'pib_cli.config': ['schemas/*'],
 'pib_cli.config.locale': ['en/LC_MESSAGES/*']}

install_requires = \
['GitPython>=3.1.26,<4.0.0',
 'PyYAML>=5.4.1,<7.0.0',
 'bandit>=1.7.0,<2.0.0',
 'click>=8.0.1,<9.0.0',
 'commitizen>=2.20.0,<3.0.0',
 'isort>=5.10.0,<6.0.0',
 'jinja2>=2.11.3,<4.0.0',
 'jsonschema>=4.4.0,<5.0.0',
 'pre-commit>=2.17.0,<3.0.0',
 'pylint>=2.8.3,<3.0.0',
 'pytest-cov>=3.0.0,<4.0.0',
 'pytest-pylint>=0.18.0,<0.19.0',
 'pytest>=7.0.1,<8.0.0',
 'safety>=1.10.3,<2.0.0',
 'wheel>=0.37.1,<0.38.0',
 'yamllint>=1.26.3,<2.0.0',
 'yapf>=0.32.0,<0.33.0']

extras_require = \
{'docs': ['darglint>=1.8.1,<2.0.0',
          'sphinx>=4.4.0,<5.0.0',
          'sphinx-autopackagesummary>=1.3,<2.0',
          'sphinx_rtd_theme>=1.0.0,<2.0.0'],
 'docstrings': ['pydocstyle>=6.1.1,<7.0.0'],
 'pib_docs': ['sphinx>=4.4.0,<5.0.0',
              'sphinx-autopackagesummary>=1.3,<2.0',
              'sphinx-click>=3.1.0,<4.0.0',
              'sphinx-intl>=2.0.1,<3.0.0',
              'sphinx-jsonschema>=1.17.2,<2.0.0',
              'sphinx_rtd_theme>=1.0.0,<2.0.0'],
 'types': ['mypy']}

entry_points = \
{'console_scripts': ['dev = pib_cli.main:main', 'pib_cli = pib_cli.main:main']}

setup_kwargs = {
    'name': 'pib-cli',
    'version': '1.2.0',
    'description': 'Python Development CLI',
    'long_description': '# PIB CLI\n\nA batteries included [make](https://www.gnu.org/software/make/) style CLI for [python](https://python.org) projects in [git](https://git-scm.com/) repositories.\n\n[Project Documentation](https://pib_cli.readthedocs.io/en/latest/)\n\n## Master Branch\n\n[![pib_cli-automation](https://github.com/niall-byrne/pib_cli/workflows/pib_cli%20Automation/badge.svg?branch=master)](https://github.com/niall-byrne/pib_cli/actions)\n\n## Production Branch\n\n[![pib_cli-automation](https://github.com/niall-byrne/pib_cli/workflows/pib_cli%20Automation/badge.svg?branch=production)](https://github.com/niall-byrne/pib_cli/actions)\n\n## Documentation Builds\n\n[![Documentation Status](https://readthedocs.org/projects/pib-cli/badge/?version=latest)](https://pib-cli.readthedocs.io/en/latest/?badge=latest)\n\n## Supported Python Versions\n\nTested to work with the following Python versions:\n\n  - Python 3.7\n  - Python 3.8\n  - Python 3.9\n  - Python 3.10\n\n## Installation\n\nTo install, simply use: \n\n  - `pip install pib_cli`\n  - `pip install pib_cli[docs]` (Adds [Sphinx](https://www.sphinx-doc.org/en/master/) support.)\n  - `pip install pib_cli[docstrings]` (Adds [pydocstyle](http://www.pydocstyle.org/en/stable/) support.)\n  - `pip install pib_cli[types]` (Adds [mypy](http://mypy-lang.org/) support.)\n\n## Usage\n\n- The CLI itself is launched with the `dev` command.\n- Try `dev --help` for details.\n\n## With Cookiecutter\n\n`pib_cli` is also baked into this [Cookie Cutter](https://github.com/cookiecutter/cookiecutter) template:\n\n  - [Python In A Box](https://github.com/niall-byrne/python-in-a-box)\n\n## License\n\n[MPL-2](https://github.com/niall-byrne/pib_cli/blob/master/LICENSE)\n\n## Included Packages\n\nAs it\'s batteries included, `pib_cli` ships with a slightly opinionated list of popular development packages.  You can customize the exact mix by specifying one or more [extras](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/?highlight=extras#installing-extras) when installing the package. \n\n### Core installed packages\n| package       | Description                       |\n| ------------- | --------------------------------- |\n| bandit        | Finds common security issues      |\n| commitizen    | Standardizes commit messages      |\n| isort         | Sorts imports                     |\n| pre-commit    | Pre-commit hook manager           |\n| pylint        | Static code analysis              |\n| pytest        | Testing with Python               |\n| pytest-cov    | Coverage support for pytest       |\n| pytest-pylint | Pylint support for pytest         |\n| safety        | Dependency vulnerability scanning |\n| wheel         | Package distribution tools        |\n| yamllint      | Lint YAML configuration files     |\n| yapf          | Customizable code formatting      |\n\n### Installed and required by pib_cli\n| package       | Description                        |\n| ------------- | ---------------------------------- |\n| click         | Command line interface toolkit     |\n| jsonschema    | JSON Schema validation for Python  |\n| GitPython     | Interact with Git repositories     |\n| PyYAML        | YAML parser and emitter for Python |\n\n  - `pip install pib_cli` to install only these dependencies.\n  - These become indirect **development** dependencies of **YOUR** project, so it\'s good to keep that in mind.\n\n### \'docs\' extras\n| package                   | Description                                                |\n| ------------------------- | ---------------------------------------------------------- |\n| darglint                  | Sphinx style guide enforcement                             |\n| sphinx                    | Python documentation generator                             |\n| sphinx-autopackagesummary | Template nested module content                             |\n| sphinx_rtd_theme          | The [Read the Docs](https://readthedocs.org/) Sphinx theme | \n\n  - `pip install pib_cli[docs]` to add these dependencies to the core installation.\n\n### \'docstrings\' extras\n| package    | Description                       |\n| ---------- | --------------------------------- |\n| pydocstyle | PEP 257 enforcement               |\n\n  - `pip install[docstrings]` to add these dependencies to the core installation.\n\n### \'types\' extras\n| package    | Description                       |\n| ---------- | --------------------------------- |\n| mypy       | Static type checker               |\n\n  - `pip install pib_cli[types]` to add these dependencies to the core installation.\n\n### \'pib_docs\' extras\n| package                   | Description                                                |\n| ------------------------- | ---------------------------------------------------------- |\n| sphinx                    | Python documentation generator                             |\n| sphinx-autopackagesummary | Templates nested module content                            |\n| sphinx-click              | Generates CLI documentation                                |\n| sphinx-intl               | Generates documentation translations                       |\n| sphinx-jsonschema         | Generates JSON schema documentation                        |\n| sphinx_rtd_theme          | The [Read the Docs](https://readthedocs.org/) Sphinx theme | \n\n  - `pip install pib_cli[pib_docs]` to add these dependencies to the core installation.\n  - These extras exist only to support building `pib_cli` documentation- they aren\'t meant to be consumed by user projects.\n\n### Installing multiple extras\n\nThis is straightforward to do:\n\n  - `pip install pib_cli[docs,docstrings,types]`\n\n## Customizing the Command Line Interface\n\nThe most powerful feature of `pib_cli` is its ability to customize how it interacts with the packages it brings to your project.  In this way it\'s very similar to the standard Linux [make](https://www.gnu.org/software/make/) command- with the notable difference being that `pib_cli` is packaged with a suite of Python libraries.\n\n**The CLI configuration file is in YAML format, and conforms to [this](https://github.com/niall-byrne/pib_cli/blob/master/pib_cli/config/schemas) set of JSON schemas.**\n\n  - pib_cli v1.0.0 introduces a [new JSON schema version](https://github.com/niall-byrne/pib_cli/blob/master/pib_cli/config/schemas/cli_base_schema_v2.0.0.json).\n  - pib_cli v1.2.0 introduces [further refinements to the JSON schema](https://github.com/niall-byrne/pib_cli/blob/master/pib_cli/config/schemas/cli_base_schema_v2.1.0.json) but is fully backwards compatible with v1.0.0, and **ALL** legacy configuration files.\n\n### Creating a \'.pib.yml\' file\n\nThe `.pib.yml` file is where you can take control, and customize `pib_cli` behaviour to suit your particular needs.  This file should adhere to the specification detailed above- read on for further detail.\n\nThe top level of your `.pib.yml` file should include metadata information.  This metadata is used to tell `pib_cli` where to find your project\'s codebase and any documentation (Sphinx) definitions.\n\n```yaml\nmetadata:\n  project_name: "Tell pib_cli the folder your codebase is in."\n  documentation_root: "Tell pib_cli where to find your documentation definitions."\ncli_definition:\n  - [A YAML array of cli command definitions, which are detailed in the next section].\n```\n\n  - The `cli_definition` section is mandatory, and `pib_cli` will throw an error if it\'s missing.\n  - The metadata itself though is actually optional, and can also be declared using environment variables.\n\n**Understanding pib_cli metadata**\n\nMetadata tells `pib_cli` where to find your project\'s files, so it\'s important to set these values appropriately:\n\n  - `project_name` is your project\'s name from a Python perspective.  It\'s the top level folder (inside your git repository) that houses your codebase, such that `from <project_name> import *` would be accessing your codebase.\n  - `documentation_root` is a relative path from your repository\'s root to a folder containing a Sphinx Makefile.  This is purely a convenience definition for any documentation related commands.\n\n**Environment variables and pib_cli**\n\nYou may also define your project\'s metadata by setting environment variables.  This would allow you to reuse the same CLI configuration for multiple projects:\n\n  - `project_name` can also be defined by `PIB_PROJECT_NAME` environment variable\n  - `documentation_root` can also be defined by the `PIB_DOCUMENTATION_ROOT` environment variable\n\nWhen configuration AND environment variables exist, `pib_cli` will **prefer to use environment variable values**.\n\n**Environment variables and pib_cli commands**\n\nRegardless of whether you have used configuration or environment variables, when your CLI commands are executed, the environment variables will be available in the shell:\n\n  - `PIB_PROJECT_NAME` will always be defined and accessible from inside the shell\n  - `PIB_DOCUMENTATION_ROOT` will always be defined and accessible from inside the shell\n\n\n### Adding a CLI definition to a \'.pib.yml\' file\n\nThe `cli_definition` YAML key, should contain a list of definitions for CLI commands you wish to use.\n\nEach command should adhere to this format (and you can have many commands for whatever tasks you need to perform):\n\n```yaml\n    - name: "command-name"\n      description: "A description of the command."\n      container_only: false # Optional restriction of the command to a PIB container\n      path: "repo_root"\n      commands:\n        - "one or more"\n        - "shell commands"\n        - "each run in a discrete environment"\n        - "The ${PIB_DOCUMENTATION_ROOT} environment variable is also available if you need to navigate to that folder."\n        - "The ${PIB_PROJECT_NAME} environment variable is available if you need to navigate to that folder."\n        - "Any extra arguments passed are stored in the ${PIB_OVERLOAD_ARGUMENTS} environment variable."\n      success: "Success Message"\n      failure: "Failure Message"\n```\n\nNotes on this configuration format: \n\n  - `container_only` restricts the command to working only inside a [Python-in-a-Box](https://github.com/niall-byrne/python-in-a-box) container environment.  (Completely optional key to include, defaults to `false`.)\n  - `path` must be one of:\n    - `repo_root` (The root folder of your code repository.)\n    - `documentation_root` (Defaults to the folder `documentation`, can be customized with metadata or environment variables.)\n    - `project_root` (The `project_name` folder as defined with metadata or environment variables.)\n\n### Validating a \'.pib.yml\' file\n\nUse `pib_cli` to validate new configuration files before activating them:\n\n  - `dev @pib config -c <path to your file> validate`\n\n### Activating a \'.pib.yml\' file\n\nTo `activate` your configuration, use one of the following methods:\n\n   1. You can set the environment variable `PIB_CONFIG_FILE_LOCATION` to the absolute path where the file is located.\n   2. Or just move your new `.pib.yml` file to the top level folder (the repository root) of your project.\n\nUse the command `dev @pib config where` to confirm it\'s been activated.\n\nIf a `.pib.yml` file cannot be found with either of these methods, then the [default config](https://github.com/niall-byrne/pib_cli/blob/master/pib_cli/config/default_cli_config.yml) will be used.\n\n## Development Guide for `pib_cli`\n\nPlease see the documentation [here](https://github.com/niall-byrne/pib_cli/blob/master/CONTRIBUTING.md).\n\n## Environment Variable Summary\n\nThis table summarizes the environment variables that can be used with `pib_cli`:\n\n| Name                      | Purpose                                                                   |\n| ------------------------- | ------------------------------------------------------------------------- |\n| PIB_CONFIG_FILE_LOCATION  | The absolute path to the configuration file that should be used.          | \n| PIB_DOCUMENTATION_ROOT    | A relative path from the repository root where a Sphinx Makefile lives.   |\n| PIB_OVERLOAD_ARGUMENTS    | Reserved to pass arguments to customized CLI commands.                    |\n| PIB_PROJECT_NAME          | The top level folder in the repository where the codebase is found.       |\n',
    'author': 'Niall Byrne',
    'author_email': 'niall@niallbyrne.ca',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/niall-byrne/pib_cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7.0,<3.11.0',
}


setup(**setup_kwargs)
