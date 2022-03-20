# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poetry_pyinvoke_plugin']

package_data = \
{'': ['*']}

install_requires = \
['invoke>=1.6.0,<2.0.0',
 'poetry>=1.2.0.a2,<2.0.0',
 'simple-chalk>=0.1.0,<0.2.0',
 'toml>=0.10.2,<0.11.0']

entry_points = \
{'poetry.application.plugin': ['inv = poetry_pyinvoke_plugin.plugin:InvPlugin',
                               'invoke = '
                               'poetry_pyinvoke_plugin.plugin:InvokePlugin']}

setup_kwargs = {
    'name': 'poetry-pyinvoke-plugin',
    'version': '0.1.2',
    'description': 'A plugin for poetry that allows you to execute scripts defined in your tasks.py using pyinvoke. Inspired by poetry-exec-plugin.',
    'long_description': '# poetry-pyinvoke-plugin\n\nA plugin for poetry that allows you to invoke commands in your `tasks.py` file delegating to `pyinvoke`.\n\nHeavily inspired by the work from `keattang` on the [poetry-exec-plugin](https://github.com/keattang/poetry-exec-plugin) project.\n\n## Installation\n\nInstallation requires poetry 1.2.0+. To install this plugin run:\n\n```sh\npip install poetry-pyinvoke-plugin\n# OR\npoetry add -D poetry-pyinvoke-plugin\n```\n\nFor other methods of installing plugins see the [poetry documentation](https://python-poetry.org/docs/master/plugins/#the-plugin-add-command).\n\n## Usage\n\n`tasks.py`\n```python\nfrom invoke import task\n\n@task\ndef lint(c):\n  c.run("flake8")\n  c.run("black --check .")\n```\n\nThen:\n```sh\npoetry invoke lint\n# OR\npoetry inv lint\n```\n\n## Publishing\n\nTo publish a new version,first bump the package version in `pyproject.toml` and commit your changes to the `main` branch (via pull request). Then in GitHub create a new release with the new version as the tag and name. You can use the handy auto release notes feature to populate the release description.\n',
    'author': 'neozenith',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/neozenith/poetry-pyinvoke-plugin',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
