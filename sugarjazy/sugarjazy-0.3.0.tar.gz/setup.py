# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sugarjazy']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['sugarjazy = sugarjazy.cli:main']}

setup_kwargs = {
    'name': 'sugarjazy',
    'version': '0.3.0',
    'description': 'Parse json logs output from uber-go/zap library nicely',
    'long_description': '# sugarjazy - parse json logs nicely\n\nsugarjazy is a simple tool to parse json logs and output them in a nice format with nice colors.\n\nUsually play nicely with <https://github.com/uber-go/zap> when using the ["Sugar"](https://pkg.go.dev/go.uber.org/zap#Logger.Sugar) log.\n\n## Installation\n\nThere is not many dependencies on this package but [`python-dateutil`](https://dateutil.readthedocs.io/en/stable/) is an optional dependency, if the package is not installed you will not be be able to show the log timestamps.\n\n### Arch\n\nYou can install it [from aur](https://aur.archlinux.org/packages/sugarjazy) with your aurhelper, like yay :\n\n```\nyay -S sugarjazy\n```\n\n### pip\n\nWith pip from pypi - <https://pypi.org/project/sugarjaz/>\n\n```\npip install --user sugarjazy\n```\n\n(make sure $HOME/.local/bin is in your PATH)\n\n## Screenshot\n\n![screenshot](./.github/screenshot.png)\n\n## Usage\n\nYou can simply pipe your logs vai `kubectl logs podname|sugarjazy` or specify a log file.\n\n```shell\n% poetry run sugarjazy --help\nusage: sugarjazy [-h] [--timeformat TIMEFORMAT] [--regexp-highlight REGEXP_HIGHLIGHT] [--disable-event-colouring] [--regexp-color REGEXP_COLOR] [--hide-timestamp] [files ...]\n\npositional arguments:\n  files\n\noptions:\n  -h, --help            show this help message and exit\n  --timeformat TIMEFORMAT\n                        timeformat default only to the hour minute. Use "%Y-%m-%d %H:%M:%S" if you want to add the year\n  --regexp-highlight REGEXP_HIGHLIGHT, -r REGEXP_HIGHLIGHT\n                        Highlight a regexp in message, for example: \\"Failed:\\s*\\d+, Cancelled\\s*\\d+\\"\n  --disable-event-colouring\n                        Add a \uf054 with a color to the eventid to easily identify which event belongs to which\n  --regexp-color REGEXP_COLOR\n                        Regexp highlight color\n  --hide-timestamp, -H  don\'t show timestamp\n  ```\n\nSugarjazy try to identify the same event and add all events on the same colors to the chevron character (\uf054).\n\n## Copyright\n\n[Apache-2.0](./LICENSE)\n\n## Authors\n\nChmouel Boudjnah <[@chmouel](https://twitter.com/chmouel)>\n',
    'author': 'Chmouel Boudjnah',
    'author_email': 'chmouel@chmouel.com',
    'maintainer': 'Chmouel Boudjnah',
    'maintainer_email': 'chmouel@chmouel.com',
    'url': 'https://github.com/chmouel/sugarjazy',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
