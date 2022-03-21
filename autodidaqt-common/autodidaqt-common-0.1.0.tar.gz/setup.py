# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['autodidaqt_common', 'autodidaqt_common.remote']

package_data = \
{'': ['*']}

install_requires = \
['dataclasses_json>=0.5.0,<0.6.0',
 'loguru>=0.3.2,<0.4.0',
 'numpy>=1.20,<2.0',
 'pynng>=0.7.1,<0.8.0',
 'xarray>=0.18.2']

setup_kwargs = {
    'name': 'autodidaqt-common',
    'version': '0.1.0',
    'description': 'Common code for autodiDAQt and autodiDAQt-receiver.',
    'long_description': '# autodidaqt-common\n\n<div align="center">\n\n[![Build status](https://github.com/chstan/autodidaqt-common/workflows/build/badge.svg?branch=master&event=push)](https://github.com/chstan/autodidaqt-common/actions?query=workflow%3Abuild)\n[![Python Version](https://img.shields.io/pypi/pyversions/autodidaqt-common.svg)](https://pypi.org/project/autodidaqt-common/)\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![License](https://img.shields.io/github/license/chstan/autodidaqt-common)](https://github.com/chstan/autodidaqt-common/blob/master/LICENSE)\n\nAnalyis-side bridge for autodiDAQt.\n\n</div>\n\n## Installation\n\n```bash\npip install -U autodidaqt-common\n```\n\nor install with `Poetry`\n\n```bash\npoetry add autodidaqt-common\n```\n\n## Building and releasing\n\nBuilding a new version of the application contains steps:\n\n- Bump the version of your package `poetry version <version>`. You can pass the new version explicitly, or a rule such as `major`, `minor`, or `patch`. For more details, refer to the [Semantic Versions](https://semver.org/) standard.\n- Make a commit to `GitHub`.\n- Create a `GitHub release`.\n- Publish `poetry publish --build`\n',
    'author': 'chstan',
    'author_email': 'chstansbury@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/chstan/autodidaqt-common',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
