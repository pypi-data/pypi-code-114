# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pluginmgr']

package_data = \
{'': ['*']}

install_requires = \
['munge>=1.0.0,<2.0.0']

setup_kwargs = {
    'name': 'pluginmgr',
    'version': '1.1.0',
    'description': 'lightweight python plugin system supporting config inheritance',
    'long_description': "\n# pluginmgr\n\n\n[![PyPI](https://img.shields.io/pypi/v/pluginmgr.svg?maxAge=3600)](https://pypi.python.org/pypi/pluginmgr)\n[![PyPI](https://img.shields.io/pypi/pyversions/pluginmgr.svg?maxAge=3600)](https://pypi.python.org/pypi/pluginmgr)\n[![Tests](https://github.com/20c/pluginmgr/workflows/tests/badge.svg)](https://github.com/20c/pluginmgr)\n[![Codecov](https://img.shields.io/codecov/c/github/20c/pluginmgr/master.svg?maxAge=3600)](https://codecov.io/github/20c/pluginmgr)\n[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/20c/pluginmgr.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/20c/pluginmgr/context:python)\n\n\n\nlightweight python plugin system supporting config inheritance\n\n\n## To use\n\nThere is a full example at <https://github.com/20c/pluginmgr/tree/master/tests/pluginmgr_test>\n\nCreate the manager, for example in a module `__init__.py` file\n\n```python\nimport pluginmgr\n\n# this is the namespace string that import uses\nnamespace = 'pluginmgr_test.plugins'\n\n# directories to look in, string or list of strings\nsearchpath = 'path/to/search/in'\n\n# determines if this should create a blank loader to import through. This\n# should be enabled if there isn't a real module path for the namespace and\n# disabled for sharing the namespace with static modules\n# default is False\ncreate_loader = False\n\nplugin = pluginmgr.PluginManager(namespace, searchpath, create_loader)\n```\n\nCreate and register a plugin, note the filename needs to be the same as registered name\n\n```python\nfrom pluginmgr_test import plugin\n\n\n# register a plugin named mod0\n@plugin.register('mod0')\nclass Mod0(pluginmgr.PluginBase):\n    pass\n```\n\nSee the dict containing all registered plugins\n\n```python\nfrom pluginmgr_test import plugin\n\n# dict of all registered plugins\nprint(plugin.registry)\n```\n\n",
    'author': '20C',
    'author_email': 'code@20c.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/20c/pluginmgr',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
