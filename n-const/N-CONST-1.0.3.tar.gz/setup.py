# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['n_const']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.19,<2.0', 'tomlkit>=0.10,<0.11']

extras_require = \
{':python_version < "3.8"': ['astropy>=3.0,<4.0'],
 ':python_version < "3.9"': ['typing-extensions>=3.0,<5.0'],
 ':python_version >= "3.6" and python_version < "3.7"': ['dataclasses>=0.8,<0.9'],
 ':python_version >= "3.8"': ['astropy>=5.0.3,<6.0.0']}

setup_kwargs = {
    'name': 'n-const',
    'version': '1.0.3',
    'description': 'Necst Constants and ObservatioN Specification Translator.',
    'long_description': '# N-CONST\n\n[![PyPI](https://img.shields.io/pypi/v/n-const.svg?label=PyPI&style=flat-square)](https://pypi.org/pypi/n-const/)\n[![Python](https://img.shields.io/pypi/pyversions/n-const.svg?label=Python&color=yellow&style=flat-square)](https://pypi.org/pypi/n-const/)\n[![Test](https://img.shields.io/github/workflow/status/nanten2/N-const/Test?logo=github&label=Test&style=flat-square)](https://github.com/nanten2/NASCO-tools/actions)\n[![License](https://img.shields.io/badge/license-MIT-blue.svg?label=License&style=flat-square)](LICENSE)\n\nNecst Constants and ObservatioN Specification Translator.\n\n## Features\n\nThis library provides:\n\n- constants of the telescope system as useful python objects\n- parsers for parameter files unique to NECST\n\n## Installation\n\n```shell\npip install n-const\n```\n\n## Usage\n\nBe careful of the package name! Use underscore instead of hyphen.\n\n### Constants\n\nSolid constants such as location of the telescope are declared in `constants` module. To use the constants:\n\n```python\n>>> import n_const\n>>> n_const.LOC_NANTEN2\nEarthLocation(2230866.39573496, -5440247.68222275, -2475554.41874542) m\n>>> n_const.XFFTS.ch_num\n32768\n```\n\n`Constants` objects support both keys and dot notations to access its components. So you can write:\n\n```python\n>>> n_const.XFFTS[\'ch_num\']\n32768\n```\n\nYou now can get all the parameters packed in the `Constants` using `dict` method:\n\n```python\n>>> n_const.XFFTS.keys()\ndict_keys([\'ch_num\', \'bandwidth\'])\n>>> n_const.REST_FREQ.values()\ndict_values([<Quantity 115.27 GHz>, <Quantity 110.20 GHz>, ..., <Quantity 219.56 GHz>])\n>>> n_const.XFFTS.items()\ndict_items([(\'ch_num\', 32768), (\'bandwidth\', <Quantity 2. GHz>)])\n```\n\n### Parameters\n\nPointing error parameter (parameters to correct pointing error) and observation parameters are extracted via `pointing` and `obsparam` modules respectively.\n\nTo get the pointing error parameters:\n\n```python\n>>> from n_const.pointing import PointingError\n>>> params = PointingError.from_file("path/to/param_file")\n>>> params.dAz\nQuantity 5314.24667547 arcsec\n\n# This module also supports keys to access the components:\n\n>>> params[\'dAz\']\nQuantity 5314.24667547 arcsec\n```\n\nTo get the observation parameters:\n\n```python\n>>> from n_const import obsparams\n>>> params = obsparams.OTFParams.from_file("path/to/obs_file")\n>>> params.Beta_on\n<Angle 15.51638889 deg>\n>>> params[\'Beta_on\']\n<Angle 15.51638889 deg>\n```\n\nFor conventional style obsfiles, this module provides a parser. This is a conventional one, so it provides very limited functionality;\n\n- Dot notation is not supported, keys only.\n- Return values are not combined with units.\n\n```python\n>>> params = obsparams.obsfile_parser("path/to/obs_file")\n>>> params[\'offset_Az\']\n0\n```\n\n---\n\nThis library is using [Semantic Versioning](https://semver.org).\n',
    'author': 'KaoruNishikawa',
    'author_email': 'k.nishikawa@a.phys.nagoya-u.ac.jp',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://nanten2.github.io/N-CONST',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
