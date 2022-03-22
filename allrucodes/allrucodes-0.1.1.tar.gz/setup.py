# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['allrucodes']

package_data = \
{'': ['*'], 'allrucodes': ['data/*']}

install_requires = \
['fuzzywuzzy>=0.18.0,<0.19.0', 'numpy>=1.22.3,<2.0.0']

setup_kwargs = {
    'name': 'allrucodes',
    'version': '0.1.1',
    'description': 'Python package with a collection of official all-russian codes catalogs.',
    'long_description': '# allrudirectory\n\n\n[![pypi](https://img.shields.io/pypi/v/allrucodes.svg)](https://pypi.org/project/allrucodes/)\n[![python](https://img.shields.io/pypi/pyversions/allrucodes.svg)](https://pypi.org/project/allrucodes/)\n[![Build Status](https://github.com/naydyonov/allrucodes/actions/workflows/dev.yml/badge.svg)](https://github.com/naydyonov/allrucodes/actions/workflows/dev.yml)\n[![codecov](https://codecov.io/gh/naydyonov/allrucodes/branch/main/graphs/badge.svg)](https://codecov.io/github/naydyonov/allrucodes)\n\n\n\nPython package with a collection of official all-russian code catalogs\n\n\n* Documentation: <https://naydyonov.github.io/allrucodes>\n* GitHub: <https://github.com/naydyonov/allrucodes>\n* PyPI: <https://pypi.org/project/allrucodes/>\n* Free software: MIT\n\n\n## Features\n\nFor now it contains few of all-russian classifiers:\n* OKSM (ОКСМ) - All-russian classifier of world countries (Общероссийский классификатор стран мира)\n* OKOPF (ОКОПФ) - All-russian classifier of organizational and legal forms (Общероссийский классификатор организационно-правовых форм)\n\n## Credits\n\nThis package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage) project template.\n',
    'author': 'Alexey Naydyonov',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/naydyonov/allrucodes',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
