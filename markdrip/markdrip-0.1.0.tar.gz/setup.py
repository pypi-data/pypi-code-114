# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['markdrip', 'markdrip.mods']

package_data = \
{'': ['*'], 'markdrip': ['css/*', 'templete/*']}

install_requires = \
['Jinja2>=3.1.1,<4.0.0', 'click>=8.0.4,<9.0.0', 'mistletoe>=0.8.2,<0.9.0']

entry_points = \
{'console_scripts': ['markdrip = markdrip.main:main']}

setup_kwargs = {
    'name': 'markdrip',
    'version': '0.1.0',
    'description': 'Simple MarkDown renderer',
    'long_description': '# Markdrip\n\nMarkDrip is a simple HTML generator.\nMistletoe is used for rendering.\n\nThe site is [here](https://comamoca.github.io/markdrip.github.io/) even in the rendered result.\n\n## How to use\n\n`markdrip filename`\n\n### Options\n\nRun `markdrip --help`.\n\n```\nUsage: main.py [OPTIONS] TARGET\n\nOptions:\n  --output TEXT  Output destination file path\n  --theme TEXT   Applicable CSS file name. Does not include extension.\n  --help         Show this message and exit.\n\n```\n\n## Custom CSS\n\nCSS is stored under `~ / .markdrip`.\nNote that when writing CSS, specify the tag name directly in the selector.\n\nEx.)\n```\nh1, h2, h3, h4, h5 {\n\tcolor: black\n}\n```\n',
    'author': 'Comamoca',
    'author_email': 'comamoca.dev@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
