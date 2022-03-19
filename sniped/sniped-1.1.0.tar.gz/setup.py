# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sniped']

package_data = \
{'': ['*']}

install_requires = \
['rich>=12.0.0,<13.0.0', 'typer[all]>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['sniped = sniped.__main__:app']}

setup_kwargs = {
    'name': 'sniped',
    'version': '1.1.0',
    'description': 'Turn snippets of code into beautiful images.',
    'long_description': '# sniped\n\n`sniped` is a CLI tool that helps you turn code snippets into beautiful images.\n\n## Example\n\n```pwsh\nsniped create snappify "print(\'Hello, world!\')" --language Python --key snappify.key --out imgs/hello_world.png\n```\n\n![](imgs/hello_world.png)\n\n## Usage\n\n```console\n$ sniped [OPTIONS] COMMAND [ARGS]...\n```\n\n**Options**:\n\n* `--install-completion`: Install completion for the current shell.\n* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.\n* `--help`: Show this message and exit.\n\n**Commands**:\n\n* `config`: Manage the configuration for the services.\n* `create`: Create a beautiful image from a snippet of code.\n\n### `sniped config`\n\nManage the configuration for the services.\n\n**Usage**:\n\n```console\n$ sniped config [options] SERVICE:[carbon|snappify]\n```\n\n**Arguments**:\n\n* `SERVICE:[carbon|snappify]`: [required]\n\n**Options**:\n\n* `--show / --no-show`: Print the configuration to stdout.  [default: False]\n* `--pretty / --no-pretty`: Whether to use pretty printing or show plain output.  [default: True]\n* `--write WRITE_PATH`: File to write default config to.\n* `--help`: Show this message and exit.\n\n### `sniped create`\n\nCreate a beautiful image from a snippet of code.\n\n**Usage**:\n\n```console\n$ sniped create [options] SERVICE:[carbon|snappify] CODE_OR_PATH\n```\n\n**Arguments**:\n\n* `SERVICE:[carbon|snappify]`: [required]\n* `CODE_OR_PATH`: Code to include in the image or path to code file. Use \'-\' to read from stdin.  [required]\n\n**Options**:\n\n* `--language LANG`: Language for syntax highlighting; \'auto\' only works for carbon.  [default: auto]\n* `--key KEY_OR_PATH`: (Path to file with) API key for Snappify.\n* `--out PATH`: Write to given file instead of stdout.\n* `--help`: Show this message and exit.\n\n\n## Changelog\n\nSee the file [CHANGELOG.md](CHANGELOG.md).\n',
    'author': 'Rodrigo Girão Serrão',
    'author_email': '5621605+RodrigoGiraoSerrao@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
