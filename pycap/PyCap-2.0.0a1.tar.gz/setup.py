# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['redcap', 'redcap.methods']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.20,<3.0', 'semantic-version>=2.8.5,<3.0.0']

extras_require = \
{'data_science': ['pandas>=1.3.4,<2.0.0']}

setup_kwargs = {
    'name': 'pycap',
    'version': '2.0.0a1',
    'description': 'PyCap: Python interface to REDCap',
    'long_description': '# PyCap\n\n[![CI](https://github.com/redcap-tools/PyCap/actions/workflows/ci.yml/badge.svg)](https://github.com/redcap-tools/PyCap/actions/workflows/ci.yml)\n[![Codecov](https://codecov.io/gh/redcap-tools/PyCap/branch/master/graph/badge.svg?token=IRgcPzANxU)](https://codecov.io/gh/redcap-tools/PyCap)\n[![PyPI](https://badge.fury.io/py/PyCap.svg)](https://badge.fury.io/py/PyCap)\n[![black](https://img.shields.io/badge/code%20style-black-black)](https://pypi.org/project/black/)\n\n## Intro\n\n`PyCap` is a python module exposing the REDCap API through some helpful abstractions. Information about the REDCap project can be found at http://project-redcap.org/.\n\nAvailable under the MIT license.\n\n## Installation\n\nInstall the latest version with [`pip`](https://pypi.python.org/pypi/pip)\n\n```sh\n$ pip install PyCap\n```\n\nIf you want to load REDCap data into [`pandas`](https://pandas.pydata.org/) dataframes, this will make sure you have `pandas` installed\n\n```sh\n$ pip install PyCap[pandas]\n```\n\nTo install the bleeding edge version from the github repo, use the following\n\n```sh\n$ pip install -e git+https://github.com/redcap-tools/PyCap.git#egg=PyCap\n```\n\n## Documentation\n\nCanonical documentation and usage examples can be found [here](http://redcap-tools.github.io/PyCap/).\n\n## Features\n\nCurrently, these API calls are available:\n\n### Export\n\n* Field names\n* Instrument-event mapping\n* File\n* Metadata\n* Project Info\n* Records\n* Report\n* Survey participant list\n* Users\n* Version\n\n### Import\n\n* File\n* Metadata\n* Records\n\n### Delete\n\n* File\n* Records\n\n### Other\n\n* Generate next record name\n\n## Citing\n\nIf you use PyCap in your research, please consider citing the software:\n\n>    Burns, S. S., Browne, A., Davis, G. N., Rimrodt, S. L., & Cutting, L. E. PyCap (Version 1.0) [Computer Software].\n>    Nashville, TN: Vanderbilt University and Philadelphia, PA: Childrens Hospital of Philadelphia.\n>    Available from https://github.com/redcap-tools/PyCap. doi:10.5281/zenodo.9917\n',
    'author': 'Scott Burns',
    'author_email': 'scott.s.burns@gmail.com',
    'maintainer': 'Paul Wildenhain',
    'maintainer_email': 'pwildenhain@gmail.com',
    'url': 'https://github.com/redcap-tools/PyCap',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
