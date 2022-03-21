# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simple_poetry']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['docs = simple_poetry:__docs',
                     'serve = simple_poetry:__serve',
                     'test = simple_poetry:__test']}

setup_kwargs = {
    'name': 'simple-poetry',
    'version': '0.1.0',
    'description': 'A clean, automated setup for publishing simple Python packages to PyPI and Anaconda.',
    'long_description': '# Simple Poetry\n\n**A clean, automated setup for publishing simple Python packages to PyPI using Poetry and GitHub Actions.**\n\n![action](https://img.shields.io/github/workflow/status/ppeetteerrs/simple-poetry/build?logo=githubactions&logoColor=white)\n[![pypi](https://img.shields.io/pypi/v/simple-poetry.svg)](https://pypi.python.org/pypi/simple-poetry)\n[![codecov](https://img.shields.io/codecov/c/github/ppeetteerrs/simple-poetry?label=codecov&logo=codecov)](https://app.codecov.io/gh/ppeetteerrs/simple-poetry)\n[![docs](https://img.shields.io/github/deployments/ppeetteerrs/simple-poetry/github-pages?label=docs&logo=readthedocs)](https://ppeetteerrs.github.io/simple-poetry)\n\n## Setup\n\n1. Prepare GitHub repo\n\t- Create new GitHub repository / fork this repository\n\t- Setup PyPI Credentials in repository secrets\n\t\t- `PYPI_TOKEN`: PyPI API token\n\n2. Replace text in files\n\t- Rename `simple_poetry` folder to `<package_name>`\n\t- Replace all `simple_poetry` instance in files to `<package_name>`\n\t- Replace all `simple-poetry` instance in files to `<package-name>`\n\t- Replace all `3.8` instance in files to `<target-python-version>`\n\t- Replace `ppeetteerrs` with `<github_user_name`>\n\n3. Enter Package Information\n\t- `pyproject.toml`: Project description, authors\n\t- `<package_name>/__init__.py`: Author and email\n\t- `README.md`: Customize it, change the name and description especially\n\n4. Further Customizations\n\t- `mkdocs.yaml`: Edit theme and `mkdocstrings` preferences (Can also add sub-pages to API Reference etc.)\n\t- `.devcontainer.json`: Add preferred extensions / build configurations (e.g. use GPUs)\n\t- `Dockerfile`: Install necessary formatters / linters / packages for local testing\n\t- `docs/`: Write your documentation\n\t- `.github/workflows/push.yaml`: Remove the `tests::Run Tests` step if you need to run tests locally (e.g. if your tests require GPU). Keep the rest to upload Codecov.\n\n5. Publish and Setup GitHub Pages\n\t- `commit` and `push` your changes\n\t- Create first release\n\t- Go to `Settings` and activate your GitHub Pages using the `gh-pages` branch',
    'author': 'Peter Yuen',
    'author_email': 'ppeetteerrsx@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ppeetteerrs/simple-poetry',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
