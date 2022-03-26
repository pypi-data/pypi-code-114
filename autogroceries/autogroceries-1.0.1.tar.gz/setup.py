# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['autogroceries', 'autogroceries.shopper', 'autogroceries.utils']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.4.1,<2.0.0',
 'selenium>=3.141.0,<4.0.0',
 'webdriver-manager>=3.4.2,<4.0.0']

setup_kwargs = {
    'name': 'autogroceries',
    'version': '1.0.1',
    'description': 'Automate your grocery shop',
    'long_description': '## autogroceries\n\n<!-- badges: start -->\n\n[![Lifecycle:\nexperimental](https://img.shields.io/badge/lifecycle-experimental-orange.svg)](https://lifecycle.r-lib.org/articles/stages.html#experimental)\n[![ci](https://github.com/dzhang32/autogroceries/workflows/test-deploy-package/badge.svg)](https://github.com/dzhang32/autogroceries/actions)\n[![Codecov test\ncoverage](https://codecov.io/gh/dzhang32/autogroceries/branch/master/graph/badge.svg)](https://codecov.io/gh/dzhang32/autogroceries?branch=master)\n[![PyPI version](https://badge.fury.io/py/autogroceries.svg)](https://badge.fury.io/py/autogroceries)\n<!-- badges: end -->\n\nThe goal of `autogroceries` is to automate your weekly grocery shop (from Sainsbury\'s).\n\n## Installation\n\n `autogroceries` was developed for for personal use and is no longer under active development. You can install the development version from `pypi`:\n\n```bash\npip install autogroceries\n```\n\n## Usage\n\n`autogroceries` uses [Selenium](https://selenium-python.readthedocs.io) to interface with the Sainsbury\'s website, automatically filling your cart with an inputted list of ingredients.\n\nThe below illustrates the minimal config required to run `autogroceries`.\n\n```python\nfrom autogroceries.shopper import SainsburysShopper\n\ningreds = ["tomatoes", "lemon"]\nn_ingreds = [1, 2]\nsb = SainsburysShopper(ingreds, n_ingreds)\n\n# SainsburysShopper needs Sainsbury\'s grocery account username/email and password\n# for security, it\'s recommended to load these from a file\n# rather than inputting your credentials directly\nshopping_list = sb.shop("UN", "PW")\n```\n\nAn example of `autogroceries` in action:\n\nhttps://user-images.githubusercontent.com/32676710/159334670-9df6cbb5-c547-426b-a42b-64b312463e56.mov\n\n## Credits\n\n`autogroceries` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n',
    'author': 'David Zhang',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
