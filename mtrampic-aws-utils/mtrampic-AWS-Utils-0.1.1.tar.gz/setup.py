# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mtrampic_aws_utils']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.21.22,<2.0.0',
 'pydantic>=1.5.1,<2.0.0',
 'requests>=2.27.1,<3.0.0',
 'typer-cli==0.0.12']

entry_points = \
{'console_scripts': ['aws-utils-cli = mtrampic_aws_utils.main:app']}

setup_kwargs = {
    'name': 'mtrampic-aws-utils',
    'version': '0.1.1',
    'description': 'Mini CLI to help work with AWS in Cross-Account setup.',
    'long_description': '# AWS-Utils\n\n<p align="center">\n    <em>A summary phrase to catch attention!</em>\n</p>\n\n<p align="center">\n<a href="https://github.com/mtrampic/AWS-Utils/actions?query=workflow%3ATest" target="_blank">\n    <img src="https://github.com/mtrampic/AWS-Utils/workflows/Test/badge.svg" alt="Test">\n</a>\n<a href="https://github.com/mtrampic/AWS-Utils/actions?query=workflow%3APublish" target="_blank">\n    <img src="https://github.com/mtrampic/AWS-Utils/workflows/Publish/badge.svg" alt="Publish">\n</a>\n<a href="https://dependabot.com/" target="_blank">\n    <img src="https://flat.badgen.net/dependabot/mtrampic/AWS-Utils?icon=dependabot" alt="Dependabot Enabled">\n</a>\n<a href="https://codecov.io/gh/mtrampic/AWS-Utils" target="_blank">\n    <img src="https://img.shields.io/codecov/c/github/mtrampic/AWS-Utils?color=%2334D058" alt="Coverage">\n</a>\n<a href="https://pypi.org/project/AWS-Utils" target="_blank">\n    <img src="https://img.shields.io/pypi/v/AWS-Utils?color=%2334D058&label=pypi%20package" alt="Package version">\n</a>\n<a href="https://pypi.org/project/AWS-Utils/" target="_blank">\n    <img src="https://img.shields.io/pypi/pyversions/AWS-Utils.svg" alt="Python Versions">\n</a>\n\n## The Basic Idea\n\nThis is a template module collecting many utilities I have liked from other projects, to serve as a personal reference.\n\n- [https://github.com/tiangolo/pydantic-sqlalchemy/](https://github.com/tiangolo/pydantic-sqlalchemy/)\n- [https://github.com/cookiecutter/cookiecutter](https://github.com/cookiecutter/cookiecutter)\n\n## Features\n\n- Poetry (virtual environment and publish to PyPi, all with one tool)\n- black (linting/formatter)\n- autoflake (removing unused packages)\n- isort (dependency organization)\n- mypy (static type checking)\n- pytest (including test coverage)\n- [pre-commit](https://pre-commit.com/) (hooks on commit)\n- GitHub Actions for CI/CD\n- mkdocs for documentation (with material theme)\n\n## Installing AWS-Utils\n\nInstall the latest release:\n\n```bash\npip install AWS-Utils\n```\n\nOr you can clone `AWS-Utils` and get started locally\n\n```bash\n\n# ensure you have Poetry installed\npip install --user poetry\n\n# install all dependencies (including dev)\npoetry install\n\n# develop!\n\n```\n\n## Example Usage\n\n```python\nimport AWS-Utils\n\n# do stuff\n```\n\nOnly **Python 3.6+** is supported as required by the black, pydantic packages\n\n## Publishing to Pypi\n\n### Poetry\'s documentation\n\nNote that it is recommended to use [API tokens](https://pypi.org/help/#apitoken) when uploading packages to PyPI.\n\n>Once you have created a new token, you can tell Poetry to use it:\n\n<https://python-poetry.org/docs/repositories/#configuring-credentials>\n\nWe do this using GitHub Actions\' Workflows and Repository Secrets!\n\n### Repo Secrets\n\nGo to your repo settings and add a `PYPI_TOKEN` environment variable:\n\n![Github Actions setup of Poetry token environment variable](images/Github-Secrets-PYPI_TOKEN-Setup.png)\n\n### Inspect the GitHub Actions Publish Workflows\n\n```yml\nname: Publish\n\non:\n  release:\n    types:\n      - created\n\njobs:\n  publish:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v2\n      ...\n      ...\n      ...\n      - name: Publish\n        env:\n          PYPI_TOKEN: ${{ secrets.PYPI_TOKEN }}\n        run: |\n          poetry config pypi-token.pypi $PYPI_TOKEN\n          bash scripts/publish.sh\n```\n\n> That\'s it!\n\nWhen you make a release on GitHub, the publish workflow will run and deploy to PyPi! 🚀🎉😎\n\n## Contributing Guide\n\nWelcome! 😊👋\n\n> Please see the [Contributing Guide](CONTRIBUTING.md).\n',
    'author': 'Mladen Trampic',
    'author_email': 'mladen@trampic.info',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
