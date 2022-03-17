# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['etch', 'etch.instructions', 'etch.mixins', 'etch.parser', 'etch.stdlib']

package_data = \
{'': ['*']}

install_requires = \
['sly>=0.4,<0.5']

extras_require = \
{'repl': ['etchrepl>=0.1.3']}

setup_kwargs = {
    'name': 'etchlang',
    'version': '0.2.3',
    'description': 'Etch, an easy-to use, high-level, interpreted lang based on Python.',
    'long_description': "# Etch\n\nTo install, run the command `pip3 install --user etchlang[repl]` or the equivalent for your package manager (This will also bundle the repl). Once you've installed Etch, just type `etch` at the command line to be dropped into the REPL.\n",
    'author': 'Ginger Industries',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/GingerIndustries/Etch',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
