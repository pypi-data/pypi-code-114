# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['convmoji']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.8.2,<2.0.0', 'questionary>=1.10.0,<2.0.0', 'typer>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['convmoji = convmoji.commit:app']}

setup_kwargs = {
    'name': 'convmoji',
    'version': '0.1.7a0',
    'description': 'A simple cli tool to commit Conventional Commits with emojis.',
    'long_description': '\n[![Test](https://github.com/KnowKit/convmoji/actions/workflows/test.yaml/badge.svg)](https://github.com/KnowKit/convmoji/actions/workflows/test.yaml)\n[![Codecov](https://codecov.io/gh/KnowKit/convmoji/branch/main/graph/badge.svg?token=84LAM4S1RD)](https://codecov.io/gh/KnowKit/convmoji)\n![PyPI](https://img.shields.io/pypi/v/convmoji?color=%234c1&label=convmoji)\n\n# convmoji\n\nA simple cli tool to commit Conventional Commits.\n\n### Requirements\n\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/convmoji)\n\n### Install\n\n```bash\npip install convmoji\nconvmoji --help\n```\n\n## Commit types\n\nFor details on commit types see [conventional commits spec](https://www.conventionalcommits.org/en/v1.0.0/#specification).\n\n* `feat`: ✨\n* `fix`: 🐛\n* `docs`: 📚\n* `style`: 💎\n* `refactor`: 🔨\n* `perf`: 🚀\n* `test`: 🚨\n* `build`: 📦\n* `ci`: 👷\n* `chore`: 🔧\n\n## Interactive Mode\n\nUse the interactive mode and be asked for different parameters. If you don\'t need them just skip with `Enter`.\nConvmojis interactive mode does not work with `--debug` but prompts for whether or not to execute the commit \n(equivalent to `--print`).\n````\nconvmoji -i\n? Your commit message (required) epic feature added\n? Choose a type (default is \'✨:feat\') (Use arrow keys)\n   ✨:feat\n   🐛:fix\n   📚:docs\n   💎:style\n   🔨:refactor\n   🚀:perf\n » 🚨:test\n   📦:build\n   👷:ci\n   🔧:chore\n...\n````\n\n## Classic Mode\n\nA conventianal commit\n````bash\nconvmoji "epic feature added" feat\n````\n\nOne with a scope\n````bash\nconvmoji "epic feature added" feat --scope somescope\n# ✨: epic feature added\n````\n\nWith options\n````bash\nconvmoji "epic feature added" feat --scope somescope --amend --no-verify\n# ✨(somescope): epic feature added --amend --no-verify\n````\n\nWith more informative text\n````bash\nconvmoji "epic feature added" feat --scope somescope \\\n  --body "more body information" --foot "more footer information"\n# ✨(somescope): epic feature added\n# \n# more body information\n# \n# more footer information\n````\n\nInform people about breaking changes\n````bash\nconvmoji "epic feature added" feat --scope somescope \\\n  --body "more body information" --footer "more footer information" \\\n  --breaking-changes "breaks somthing"\n# ✨‼️(somescope): epic feature added\n# \n# more body information\n# \n# BREAKING CHANGE: breaks somthing\n# more footer information\n````\n\nLost track of what scope string to use? Run the following to view all scopes used in \nthe mentioned **conventional commits spec** format.\n````bash\nconvmoji --show-scopes\n# README\n# action\n# actions\n# cli-options\n# coverage\n# documentation\n# error-handling\n# pipy\n# readme\n# trynerror\n````\n\n> If you want to see what to does without performing the action, run it with `--debug`.\n> This will prompt the commit command.\n\n> If you want to work with some sort of paste tool or other workflow, for example to pipe results \n> back to ide and commit stuff there, run command with `--print`. \n> This will only prompt the commit message.\n\n## convmoji --help\n\n**Usage**:\n\n```console\n$ convmoji [OPTIONS] DESCRIPTION [COMMIT_TYPE]\n```\n\n**Arguments**:\n\n* `DESCRIPTION`: Commit message, as in \'git commit -m "..."\'  [required]\n* `[COMMIT_TYPE]`: Either of [feat, fix, docs, style, refactor, perf, test, build, ci, chore]  [default: feat]\n\n**Options**:\n\n* `-s, --scope TEXT`: Scope for commit (any string)  [default: ]\n* `-b, --body TEXT`: Body message for commit  [default: ]\n* `-f, --foot TEXT`: Footer message (formatted two blank lines below body)  [default: ]\n* `--breaking-changes, --bc TEXT`: Specially formatted message to show changes might break         previous versions  [default: ]\n* `--amend`: Execute commit with --amend  [default: False]\n* `--no-verify`: Execute commit with --no-verify  [default: False]\n* `--co-authored_by, --co TEXT`: A string of authors formatted like: _`--co-authored-by \'<User user@no-reply> \'        --co-authored-by \'<User2 user2@no-reply>\'`_\n* `--debug`: Debug mode (does not execute commit)  [default: False]\n* `--show-scopes`: A helper that shows scopes used with convmoji. (does not execute commit)\n* `--info`: Prompt convmoji info (does not execute commit)\n* `--version`: Prompt convmoji version (does not execute commit)\n* `--install-completion`: Install completion for the current shell.\n* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.\n* `--help`: Show this message and exit.\n',
    'author': 'arrrrrmin',
    'author_email': 'info@dotarmin.info',
    'maintainer': 'arrrrrmin',
    'maintainer_email': 'info@dotarmin.info',
    'url': 'https://github.com/KnowKit/convmoji',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
