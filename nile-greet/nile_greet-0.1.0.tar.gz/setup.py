# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nile_greet']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.4,<9.0.0']

entry_points = \
{'nile_plugins': ['greet = nile_greet.main.greet']}

setup_kwargs = {
    'name': 'nile-greet',
    'version': '0.1.0',
    'description': 'Nile plugin for greeting',
    'long_description': '# Nile plugin example :boat:\n\nThis project is an example plugin for extending functionality in Nile.\n\n## Installation\n\n`pip install nile-greet`\n\n## Usage\n\nAfter installing you should already have the command available for usage. Run `nile --help` for checking the `nile greet` availability.\n\n## Development\n\nFor creating new plugins follow this instructions below.\n\n1. Install Poetry:\n\n`curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`\n\n2. Install dependencies:\n\n`poetry install`\n\nAfter having the environment setted up we can start developing. We will use `click` for extending Nile commands. All new commands must be implemented as `click.commands`. Find below an implementation design template:\n\n```python\n# First, import click dependency\nimport click\n\n# Decorate the method that will be the command name with `click.command` \n@click.command()\n# You can define custom parameters as defined in `click`: https://click.palletsprojects.com/en/7.x/options/\ndef my_command():\n    # Help message to show with the command\n    """\n    Subcommand plugin that does something.\n    """\n    # Done! Now implement your custom functionality in the command\n    click.echo("I\'m a plugin overiding a command!")\n```\n\nGreat! Now our new Nile command is ready to be used. For Nile to detect it make sure at least version `0.6.0` is installed. Then modify the `pyproject.toml` file as follows:\n\n```\n# We need to specify that click commands are Poetry entrypoints of type `nile_plugins`. Do not modify this\n[tool.poetry.plugins."nile_plugins"]\n# Here you specify you command name and location <command_name> = <package_method_location>\n"greet" = "nile_greet.main.greet"\n```\n\n## Testing\n\n`poetry run pytest tests`',
    'author': 'Fran Algaba',
    'author_email': 'f.algaba.work@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.11,<4.0.0',
}


setup(**setup_kwargs)
