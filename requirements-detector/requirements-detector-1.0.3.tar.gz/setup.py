# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['requirements_detector']

package_data = \
{'': ['*']}

install_requires = \
['astroid>=2.0,<3.0',
 'packaging>=21.3,<22.0',
 'poetry-semver==0.1.0',
 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['detect-requirements = requirements_detector.run:run']}

setup_kwargs = {
    'name': 'requirements-detector',
    'version': '1.0.3',
    'description': 'Python tool to find and list requirements of a Python project',
    'long_description': '# Requirements Detector\n\n## Status\n\n[![Latest Version](https://img.shields.io/pypi/v/requirements-detector.svg?label=version&style=flat)](https://pypi.python.org/pypi/requirements-detector)\n[![Build Satus](https://github.com/PyCQA/prospector/actions/workflows/ci.yaml/badge.svg)](https://github.com/PyCQA/prospector/actions/workflows/ci.yaml)\n[![Health](https://landscape.io/github/landscapeio/requirements-detector/master/landscape.svg?style=flat)](https://landscape.io/github/landscapeio/requirements-detector/master)\n[![Coverage Status](https://img.shields.io/coveralls/landscapeio/requirements-detector.svg?style=flat)](https://coveralls.io/r/landscapeio/requirements-detector)\n[![Documentation](https://readthedocs.org/projects/requirements-detector/badge/?version=master)](https://readthedocs.org/projects/requirements-detector/)\n\n## About\n\n`requirements-detector` is a simple Python tool which attempts to find and list the requirements of a Python project.\n\nWhen run from the root of a Python project, it will try to ascertain which libraries and the versions of those libraries that the project depends on.\n\nIt uses the following methods in order, in the root of the project:\n\n1. Parse `setup.py` (if this is successful, the remaining steps are skipped)\n2. Parse `pyproject.yoml` (if a `tool.poetry.dependencies` section is found, the remaining steps are skipped)\n3. Parse `requirements.txt` or `requirements.pip`\n4. Parse all `*.txt` and `*.pip` files inside a folder called `requirements`\n5. Parse all files in the root folder matching `*requirements*.txt` or `reqs.txt` (so for example, `pip_requirements.txt` would match, as would `requirements_common.txt`)\n\n### Usage\n\n```\ndetect-requirements [path]\n```\nIf `path` is not specified, the current working directory will be used.\n\n### Output\n\nThe output will be plaintext, and match that of a [pip requirements file](http://www.pip-installer.org/en/latest/logic.html), for example:\n\n```\nDjango==1.5.2\nSouth>=0.8\nanyjson\ncelery>=2.2,<3\n```\n\n### Usage From Python\n\n```\n>>> import os\n>>> from requirements_detector import find_requirements\n>>> find_requirements(os.getcwd())\n[DetectedRequirement:Django==1.5.2, DetectedRequirement:South>=0.8, ...]\n```\n\n\nIf you know the relevant file or directory,  you can use `from_requirements_txt`, `from_setup_py` or `from_requirements_dir` directly.\n\n```\n>>> from requirements_detector import from_requirements_txt\n>>> from_requirements_txt("/path/to/requirements.txt")\n[DetectedRequirement:Django==1.5.2, DetectedRequirement:South>=0.8, ...]\n```\n',
    'author': 'Landscape.io',
    'author_email': 'code@landscape.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/landscapeio/requirements-detector',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2,<4.0',
}


setup(**setup_kwargs)
