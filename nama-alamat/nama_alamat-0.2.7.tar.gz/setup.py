# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nama_alamat',
 'nama_alamat.preprocessing',
 'nama_alamat.preprocessing.dict_files',
 'tests']

package_data = \
{'': ['*']}

install_requires = \
['roman>=3.3,<4.0']

extras_require = \
{'dev': ['tox>=3.20.1,<4.0.0',
         'virtualenv>=20.2.2,<21.0.0',
         'pip>=20.3.1,<21.0.0',
         'twine>=3.3.0,<4.0.0',
         'pre-commit>=2.12.0,<3.0.0',
         'toml>=0.10.2,<0.11.0',
         'bump2version>=1.0.1,<2.0.0'],
 'doc': ['mkdocs>=1.1.2,<2.0.0',
         'mkdocs-include-markdown-plugin>=1.0.0,<2.0.0',
         'mkdocs-material>=6.1.7,<7.0.0',
         'mkdocstrings>=0.15.2,<0.16.0',
         'mkdocs-autorefs>=0.2.1,<0.3.0'],
 'test': ['black>=21.5b2,<22.0',
          'isort>=5.8.0,<6.0.0',
          'flake8>=3.9.2,<4.0.0',
          'flake8-docstrings>=1.6.0,<2.0.0',
          'mypy>=0.900,<0.901',
          'pytest>=6.2.4,<7.0.0',
          'pytest-cov>=2.12.0,<3.0.0']}

setup_kwargs = {
    'name': 'nama-alamat',
    'version': '0.2.7',
    'description': 'Indonesia Name and Address Preprocessor.',
    'long_description': "# Indonesia Name and Address Preprocessor\n\n[![pypi](https://img.shields.io/pypi/v/nama_alamat.svg)](https://pypi.org/project/nama_alamat/)\n[![python](https://img.shields.io/pypi/pyversions/nama_alamat.svg)](https://pypi.org/project/nama_alamat/)\n[![Build Status](https://github.com/kloworizer/nama_alamat/actions/workflows/dev.yml/badge.svg)](https://github.com/kloworizer/nama_alamat/actions/workflows/dev.yml)\n[![codecov](https://codecov.io/gh/kloworizer/nama_alamat/branch/main/graphs/badge.svg)](https://codecov.io/github/kloworizer/nama_alamat)\n\nIndonesia Name and Address Preprocessor\n\n-   Documentation: <https://kloworizer.github.io/nama_alamat>\n-   GitHub: <https://github.com/kloworizer/nama_alamat>\n-   PyPI: <https://pypi.org/project/nama_alamat/>\n-   Free software: MIT\n\n## Features\n\n-   Preprocessing Indonesia name and address.\n\n## Instalation\n\n```\npip install nama-alamat\n```\n\n## Usage\n\nexample of name preproccesing:\n```\nfrom nama_alamat.preprocessing import Preprocessing\npreprocessing_nama = Preprocessing(tipe='nama')\nstrings = 'IR SULAEMAN'\nprint(preprocessing_nama.preprocessing(strings))\n```\n\naddress preproccesing:\n```\nfrom nama_alamat.preprocessing import Preprocessing\npreprocessing_alamat = Preprocessing(tipe='alamat')\nstrings = 'JALAN GARUDA IX BLOK C/3 RT 003 RW 002, JAKARTA UTARA, DKI JAKARTA 12110'\nprint(preprocessing_alamat.preprocessing(strings))\n```\n\n## Credits\n\nThis package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage) project template.\n",
    'author': 'Esha Indra',
    'author_email': 'esha.indra@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/kloworizer/nama_alamat',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6.2,<4.0',
}


setup(**setup_kwargs)
