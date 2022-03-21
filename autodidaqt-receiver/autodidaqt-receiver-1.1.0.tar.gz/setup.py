# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['autodidaqt_receiver']

package_data = \
{'': ['*'],
 'autodidaqt_receiver': ['fixtures/nano_xps/*',
                         'fixtures/nano_xps/__xarray_dataarray_variable__/*',
                         'fixtures/nano_xps/alpha/*',
                         'fixtures/nano_xps/beta/*',
                         'fixtures/nano_xps/chi/*',
                         'fixtures/nano_xps/eV/*',
                         'fixtures/nano_xps/hv/*',
                         'fixtures/nano_xps/psi/*',
                         'fixtures/nano_xps/theta/*',
                         'fixtures/nano_xps/x/*',
                         'fixtures/nano_xps/y/*',
                         'fixtures/nano_xps/z/*']}

install_requires = \
['autodidaqt-common>=0.1.0,<0.2.0',
 'matplotlib>=3.1.1,<4.0.0',
 'numpy>=1.20,<2.0',
 'pandas>=1.2.4,<2.0.0',
 'ptpython>=3.0.19,<4.0.0',
 'pynng>=0.7.1,<0.8.0',
 'scipy>=1.7.1,<2.0.0',
 'xarray>=0.18.2,<0.19.0',
 'zarr>=2.8.3,<3.0.0']

setup_kwargs = {
    'name': 'autodidaqt-receiver',
    'version': '1.1.0',
    'description': 'Analyis-side bridge for autodiDAQt.',
    'long_description': '# autodidaqt-receiver\n\n<div align="center">\n\n[![Build status](https://github.com/chstan/autodidaqt-receiver/workflows/build/badge.svg?branch=master&event=push)](https://github.com/chstan/autodidaqt-receiver/actions?query=workflow%3Abuild)\n[![Python Version](https://img.shields.io/pypi/pyversions/autodidaqt-receiver.svg)](https://pypi.org/project/autodidaqt-receiver/)\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![License](https://img.shields.io/github/license/chstan/autodidaqt-receiver)](https://github.com/chstan/autodidaqt-receiver/blob/master/LICENSE)\n\nAnalysis-side bridge for AutodiDAQt.\n\n</div>\n\n## Installation\n\n```bash\npip install -U autodidaqt-receiver\n```\n\nor install with `Poetry`\n\n```bash\npoetry add autodidaqt-receiver\n```\n\n## Installation from Source\n\n1. Clone this repository\n2. Install `make` if you are on a Windows system\n3. Install `poetry` (the alternative Python package manager)\n4. Run `make install` from the directory containing this README\n\n## Building and releasing\n\nBuilding a new version of the application contains steps:\n\n- Bump the version of your package `poetry version <version>`. You can pass the new version explicitly, or a rule such as `major`, `minor`, or `patch`. For more details, refer to the [Semantic Versions](https://semver.org/) standard.\n- Make a commit to `GitHub`.\n- Create a `GitHub release`.\n- Publish `poetry publish --build`\n',
    'author': 'chstan',
    'author_email': 'chstansbury@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/chstan/autodidaqt-receiver',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
