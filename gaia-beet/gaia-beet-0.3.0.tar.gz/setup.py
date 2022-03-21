# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gaia_beet']

package_data = \
{'': ['*']}

install_requires = \
['beet>=0.45.3']

setup_kwargs = {
    'name': 'gaia-beet',
    'version': '0.3.0',
    'description': 'Beet plugin to generate Minecraft worldgen files',
    'long_description': '# gaia-beet\n\n[![GitHub Actions](https://github.com/misode/gaia/workflows/CI/badge.svg)](https://github.com/misode/gaia-beet/actions)\n[![PyPI](https://img.shields.io/pypi/v/gaia-beet.svg)](https://pypi.org/project/gaia-beet/)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/gaia-beet.svg)](https://pypi.org/project/gaia-beet/)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)\n[![Discord](https://img.shields.io/discord/900530660677156924?color=7289DA&label=discord&logo=discord&logoColor=fff)](https://discord.gg/98MdSGMm8j)\n\n> Beet plugin to generate Minecraft worldgen files\n\n## Introduction\n\nWriting density functions in JSON by hand can be tiring and confusing. This package allows you to write them as natural looking expressions.\n\n```py\ngaia.df("basic:foo", abs(const(4) ** 3) + ref("basic:bar"))\n```\n\n## Installation\n\nThe package can be installed with `pip`.\n\n```bash\n$ pip install gaia-beet\n```\n\n## Getting started\n\nWhen using with [`beet`](https://github.com/mcbeet/beet), a simple `beet.yml` is enough:\n```yml\npipeline:\n  - main\n```\n\nThis references a `main.py` plugin file where the density functions will be defined:\n```py\nfrom beet import Context\nfrom gaia_beet import Gaia\nfrom gaia_beet.density_functions import *\n\ndef beet_default(ctx: Context):\n    gaia = ctx.inject(Gaia)\n\n    blah = slide(const(2))\n\n    foo = gaia.df("basic:foo", abs(const(4) ** 3) + blah)\n\n    gaia.df("basic:bar", blah * foo)\n```\n\n## Contributing\n\nContributions are welcome. Make sure to first open an issue discussing the problem or the new feature before creating a pull request. The project uses [`poetry`](https://python-poetry.org).\n\n```bash\n$ poetry install\n```\n\nYou can run the tests with `poetry run pytest`.\n\n```bash\n$ poetry run pytest\n```\n\nThe project must type-check with [`pyright`](https://github.com/microsoft/pyright). If you\'re using VSCode the [`pylance`](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) extension should report diagnostics automatically. You can also install the type-checker locally with `npm install` and run it from the command-line.\n\n```bash\n$ npm run watch\n$ npm run check\n```\n\nThe code follows the [`black`](https://github.com/psf/black) code style. Import statements are sorted with [`isort`](https://pycqa.github.io/isort/).\n\n```bash\n$ poetry run isort gaia_beet examples tests\n$ poetry run black gaia_beet examples tests\n$ poetry run black --check gaia_beet examples tests\n```\n\n---\n\nLicense - [MIT](https://github.com/misode/gaia-beet/blob/main/LICENSE)\n',
    'author': 'Misode',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/misode/gaia-beet',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
