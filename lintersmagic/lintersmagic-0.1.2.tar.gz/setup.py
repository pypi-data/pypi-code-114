# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['lintersmagic']
install_requires = \
['ipython==8.1.1', 'pycodestyle==2.8.0']

setup_kwargs = {
    'name': 'lintersmagic',
    'version': '0.1.2',
    'description': 'A package to include linters in Databricks notebooks: pycodestyle',
    'long_description': "# Linters magic\nMagic function for pycodestyle module in Jupyter-Lab or Databricks notebooks.\n\nCurrent version: 0.1.2\n\nVersions of dependencies:\n- python: 3.8\n- pycodestyle: 2.8.0\n- ipython: 7.17\n\n**Note that we've tested it only on Databricks notebooks**\n\n# Installation\n\npip install lintersmagic\n\n# Usage\nEnable the magic function by using the lintersmagic module in a cell\n\n`%load_ext lintersmagic`\n\n## To check a cell once:\nuse the function as first line in your cell to check compliance with `pycodestyle` as such:\n\n`%%pycodestyle`\n\n## To auto check each cell:\nIf you want this compliance checking turned on by default for each cell then run this magic line function in an empty cell:\n\n`%pycodestyle_on`\n\nYou only need to call this once (observe the single `%`).\n\nTo turn off the auto-checking for each cell use:\n\n`%pycodestyle_off`\n\n## Config options for `%pycodestyle_on` (version >= 0.5)\n\n1. The option `--ignore` or `-i` will add the the named error(s) to the ignore list\n\nExample to ignore the errors `E225` and `E265`:\n```\n%pycodestyle_on --ignore E225,E265\n``` \nRemember to _avoid_ spaces between declaring multiple errors.\n\n2. With the option `--max_line_length` or `-m` the max-line-length can be customised.\n\nExample to set the line length to `119` characters instead of the default `79`:\n\n```\n%pycodestyle_on --max_line_length 119\n```\n\nThe options can be combined as well. \n\n\nSee notebooks in notebook directory for example use cases, as such:\n### Pycodestyle ([notebook](https://github.com/BedrockStreaming/lintersmagic/blob/main/notebook/examples.ipynb))\n![Notebook examples](img/pycodestyle.png)\n\n## Contribution\n\n### Dependencies and package\n\nHandled by Poetry ([documentation](https://python-poetry.org/))\n\nTo get a new package:\n\n```\npoetry build\n```\n\nTo install the dependencies:\n\n```\npoetry install\n```\n\n### Tests\n\n```\npoetry run ipython tests/*.py\n```\n\n### Useful links\n\n- This project adds a magic function in Ipython. Here is the documentation:\n  [Built-in magic commands](https://ipython.readthedocs.io/en/stable/interactive/magics.html)\n\n- This project uses a callback with magic functions. Here is the documentation:\n  [IPython Events](https://ipython.readthedocs.io/en/stable/config/callbacks.html)\n",
    'author': 'Bedrock streaming',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/BedrockStreaming/lintersmagic',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '==3.8.10',
}


setup(**setup_kwargs)
