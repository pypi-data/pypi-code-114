# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['altb']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'blessed>=1.19.0,<2.0.0',
 'getch>=1.0,<2.0',
 'natsort>=8.0.1,<9.0.0',
 'pydantic>=1.8.2,<2.0.0',
 'rich>=10.15.2,<11.0.0',
 'typer>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['altb = altb.main:main']}

setup_kwargs = {
    'name': 'altb',
    'version': '0.3.0',
    'description': 'Cli tool for tracking over binaries and easily swapping between them',
    'long_description': '# altb\naltb is a cli utility influenced by `update-alternatives` of ubuntu.  \nLinked paths are added to `$HOME/.local/bin` according to [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html).  \nConfig file is located at `$HOME/.config/altb/config.yaml`.\n\n### How to start?\nexecute:\n```bash\npipx install altb\n```\n\nto track new binary use:\n```bash\naltb track path <app_name>@<app_tag> /path/to/binary\n```\nfor example:\n```bash\naltb track path python@2.7 /bin/python2.7\naltb track path python@3.8 /bin/python3.8\n# altb track python ~/Downloads/python # will also work and generate a new hash for it\n```\n\nList all tracked versions:\n```bash\n$ altb list -a\npython\n|----   2.7 - /bin/python2.7\n|----   3.8 - /bin/python3.8\n```\n\nUse specific version:\n```bash\naltb use <app_name>[@<app_tag>]\n```\n\nexample:\n```bash\naltb use python@2.7\n```\nthis will link the tracked path to `~/.local/bin/<app_name>` in this case - `~/.local/bin/python`\n\nCopy specific standalone binary automatically to `~/.local/altb/versions/<app_name>/<app_name>_<tag>`\n```bash\naltb track path helm@3 ~/Downloads/helm --copy\n```\n\nYou can run custom commands using:\n```bash\naltb track command special_command@latest "echo This is a command"\n```\nthis especially useful for latest developments, example:\n```bash\naltb track command special_command@latest "go run ./cmd/special_command" --working-directory "$HOME/special_command"\n```\n',
    'author': 'Elran Shefer',
    'author_email': 'elran777@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/IamShobe/altb',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
