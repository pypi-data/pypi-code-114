# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['conf_diff']
install_requires = \
['colorama>=0.4.4,<0.5.0']

setup_kwargs = {
    'name': 'conf-diff',
    'version': '0.2.0',
    'description': 'compare configuration files',
    'long_description': '[![license](https://img.shields.io/github/license/abatilo/actions-poetry.svg)](https://github.com/muhammad-rafi/conf_diff/blob/main/LICENSE)\n[![Pypi](https://img.shields.io/pypi/v/conf_diff.svg)](https://pypi.org/project/conf-diff/) \n[![Build Status](https://github.com/muhammad-rafi/conf_diff/actions/workflows/main.yml/badge.svg)](https://github.com/muhammad-rafi/conf_diff/actions)\n\n# Introduction\n\nThis module is built to provide you the configuration comparison between two configuration files and generates configuration differences either on the terminal or create a HTML output file based on the parameter provided to the module.\n\nNote: This module is built on the top of the Python built-in difflib module but modified to show you the colourful output and customised HTML template.\n\n## Features\n\n* Shows the configuration differences on the terminal window with colourful output.\n* Generate a HTML output file as a comparison report.\n\n## Installation\n\nInstall this module from PyPI:\n\n```sh\npip install conf_diff\n```\n\n## Usage:\n\n### Prerequisite\nAs this module compares the configuration difference between two config file, so we need to have two configuration files should be present in the same directory where you are running the script from or specify the absolute path for the configuration files. e.g. `"/Users/rafi/sandbox-nxos-1.cisco.com_before_config.cfg"` and `"/Users/rafi/sandbox-nxos-1.cisco.com_after_config.cfg"\n`\n\nYou may use either .cfg or .txt file extensions.\n\nIn the below example, I am using two running configuration files from the Cisco always-on NXOS Sandbox, assuming that, `sandbox-nxos-1.cisco.com_before_config.cfg` was taken before the change and ` sandbox-nxos-1.cisco.com_after_config.cfg` after the change, and we want to see the configuration diffrence between them. You may name the filenames as you like or add the timestamps.\n\nImport the module on your python script and instantiate a class object \'delta\'\n\n```python\nimport conf_diff\n\n# Instantiate a class object \'delta\'\ndelta = conf_diff.ConfDiff("sandbox-nxos-1.cisco.com_before_config.cfg", "sandbox-nxos-1.cisco.com_after_config.cfg")\n\n# Display the output of the diff on the terminal \nprint(delta.diff())\n```\nAbove will generate a configuration difference on the terminal. \n\n![App Screenshot](https://github.com/muhammad-rafi/conf_diff/blob/main/images/cli_output.png)\n\nTo generate a html output file, add third parameter as the expected output file name. e.g. `"html_diff_output.html"`\n\n```python\n # Instantiate a class object \'delta\'\ndelta = conf_diff.ConfDiff("sandbox-nxos-1.cisco.com_before_config.cfg", "sandbox-nxos-1.cisco.com_after_config.cfg", "html_diff_output.html")\n\n# Generates a `html_diff_output.html` in your current directory unless expected full path is specified.\ndelta.diff()\n```\nSee the screenshot below for the `html_diff_output.html`\n![App Screenshot](https://github.com/muhammad-rafi/conf_diff/blob/main/images/html_output_file.png)\n\n## Issues\nPlease raise any issue or pull request if you find something wrong with this module.\n\n## Authors\n[Muhammad Rafi](https://github.com/muhammad-rafi)\n\n## License\nThe source code is released under the MIT License.\n',
    'author': 'Muhammad Rafi',
    'author_email': 'murafi@cisco.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/muhammad-rafi/conf_diff',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
