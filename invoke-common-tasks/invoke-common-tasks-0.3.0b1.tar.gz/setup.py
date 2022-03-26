# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['invoke_common_tasks', 'invoke_common_tasks.utils']

package_data = \
{'': ['*']}

install_requires = \
['invoke>=1.6.0,<2.0.0',
 'poetry-core>=1.0.8,<2.0.0',
 'types-invoke>=1.6.2,<2.0.0']

extras_require = \
{'all': ['black>=22.1.0,<23.0.0',
         'isort>=5.10.1,<6.0.0',
         'flake8>=4.0.1,<5.0.0',
         'flake8-docstrings>=1.6.0,<2.0.0',
         'mypy>=0.942,<0.943',
         'pytest>=7.1.1,<8.0.0',
         'pytest-cov>=3.0.0,<4.0.0',
         'coverage[toml]>=6.3.2,<7.0.0'],
 'format': ['black>=22.1.0,<23.0.0', 'isort>=5.10.1,<6.0.0'],
 'lint': ['flake8>=4.0.1,<5.0.0', 'flake8-docstrings>=1.6.0,<2.0.0'],
 'test': ['pytest>=7.1.1,<8.0.0',
          'pytest-cov>=3.0.0,<4.0.0',
          'coverage[toml]>=6.3.2,<7.0.0'],
 'typecheck': ['mypy>=0.942,<0.943']}

setup_kwargs = {
    'name': 'invoke-common-tasks',
    'version': '0.3.0b1',
    'description': 'Some common tasks for PyInvoke to bootstrap your code quality and testing workflows.',
    'long_description': '# Invoke Common Tasks\n\nSome common tasks for PyInvoke to bootstrap your code quality and testing workflows.\n\n\n## Getting Started\n\n```sh\npip install invoke-common-tasks\n# Or\npoetry add -D invoke-common-tasks\n\n# With Extras\npip install invoke-common-tasks[all]\n# Or\npoetry add -D invoke-common-tasks[all]\n```\n\n`invoke-common-tasks` defines a few _extras_, where you can also install the tooling to go with each task.\nBy default we **do not** install the tools that these tasks call, since you could have different pinned versions than what we specify.\n\nHowever, you can install `all` of them or distinct subsets:\n\n - **format** -> `black`, `isort`\n - **lint** -> `flake8`, `flake8-docstrings`\n - **typecheck** -> `mypy`\n - **test** -> `pytest`, `pytest-cov`, `coverage[toml]`\n\nSo you can specify the following if you only want `format` and `test`:\n\n```sh\npip install invoke-common-tasks[format,test]\n```\n\nAll _tasks_ will still be available but we won\'t install associated tooling.\n\n### Invoke Setup\n\n`tasks.py`\n\n```python\nfrom invoke_common_tasks import * # noqa\n```\n\nOnce your `tasks.py` is setup like this `invoke` will have the extra commands:\n\n```sh\nλ invoke --list\nAvailable tasks:\n\n  build         Build wheel.\n  ci            Run linting and test suite for Continuous Integration.\n  format        Autoformat code for code style.\n  init-config   Setup default configuration for development tooling.\n  lint          Linting and style checking.\n  test          Run test suite.\n  typecheck     Run typechecking tooling.\n```\n\nYou can also initialise default configuration for each tool by running the following:\n\n```sh\ninvoke init-config --all\n```\n\nMore details in the [init-config](#init-config) section.\n\n## The Tasks\n\n### build\n\nAssuming you are using `poetry` this will build a wheel (and only a wheel).\n\n### format\n\nThis will apply code formatting tools `black` and `isort`.\n\nThese are only triggers for these commands, the specifics of configuration are up to you.\n\nRecommended configuration in your `pyproject.toml`:\n\n```toml\n[tool.black]\nline-length = 120\n\n[tool.isort]\nprofile = "black"\nmulti_line_output = 3\nimport_heading_stdlib = "Standard Library"\nimport_heading_firstparty = "Our Libraries"\nimport_heading_thirdparty = "Third Party"\n```\n\n### lint\n\nThis will run checks for `black`, `isort` and `flake8`.\n\nUp to you to specify your preferences of plugins for `flake8` and its configuration.\n\nRecommended configuration in `.flake8`:\n\n```ini\n[flake8]\nexclude = \n    venv,\n    dist,\n    .venv\nselect = ANN,B,B9,BLK,C,D,DAR,E,F,I,S,W\nignore = E203,E501,W503,D100,D104\nper-file-ignores =\n    tests/*: D103,S101\nmax-line-length = 120\nmax-complexity = 10\nimport-order-style = google\ndocstring-convention = google\n```\n\nRecommended `flake8` plugins:\n - [`flake8-docstrings`](https://pypi.org/project/flake8-docstrings/)\n\nMore `flake8` plugins:\n\nhttps://github.com/DmytroLitvinov/awesome-flake8-extensions\n\n### typecheck\n\nSimply runs `mypy .`.\n\nRecommended configuration to add to your `pyproject.toml`\n\n```toml\n[tool.mypy]\npretty = true\nshow_error_codes = true\nshow_column_numbers = true\nshow_error_context = true\nexclude = [\n  \'tests/\',\n  \'tasks\\.py\'\n]\nfollow_imports = \'silent\'\nignore_missing_imports = true\n\n# Work your way up to these:\ndisallow_incomplete_defs = true\n# disallow_untyped_defs = true \n# disallow-untyped-calls = true\n# strict = true\n```\n\n### test (and coverage)\n\nThis will simply run `python3 -m pytest`. This is important to run as a module instead of `pytest` since it resolves\na lot of import issues.\n\nYou can simply not import this task if you prefer something else. But all config and plugins are left flexible for your own desires, this simply triggers the entrypoint.\n\nRecommended configuration in `pyproject.toml`:\n\n```toml\n[tool.pytest.ini_options]\nminversion = "6.0"\naddopts = "-s -vvv --color=yes --cov=. --no-cov-on-fail"\n\n[tool.coverage.run]\nomit = ["tests/*", "**/__init__.py", "tasks.py"]\nbranch = true\n```\n\nAssuming you also install `pytest-cov` and `coverage[toml]`.\n\nRecommended `pytest` plugins:\n - [`pytest-xdist`](https://pypi.org/project/pytest-xdist/) - Run tests in parallel using maximum cpu cores \n - [`pytest-randomly`](https://pypi.org/project/pytest-randomly/) - Run tests in random order each time to detect tests with unintentional dependencies to each other that should be isolated. Each run prints out the seed if you need to reproduce an exact seeded run.\n - [`pytest-cov`](https://pypi.org/project/pytest-cov/) - It is recommended to run coverage from the `pytest` plugin.\n \nList of other `pytest` plugins:\n\nhttps://docs.pytest.org/en/latest/reference/plugin_list.html\n\n### ci\n\nThis is a task with no commands but chains together `lint`, `typecheck` and `test`. \n\n### init-config\n\n> Experimental: This feature is still in a pre-release state.\n\nEach of the above commands came with some recommended configuration.\nThis command attempts to automate setting up even that part in your `pyproject.toml` and `.flake8` files.\n\n```sh\nλ invoke init-config --help\nUsage: inv[oke] [--core-opts] init-config [--options] [other tasks here ...]\n\nDocstring:\n  Setup default configuration for development tooling.\n\nOptions:\n  -a, --all\n  -f, --format\n  -l, --lint\n  -t, --test\n  -y, --typecheck\n```\n## TODO\n\n - Auto-initialisations of some default config. \n    - eg `invoke format --init` should set config if not present\n\n\n## Roadmap\n\nThis project will get marked as a stable v1.0 once the above TODO features are ticked off and this has seen at least 6 months in the wild in production.\n\n\n## All Together\n\nOnce all the tasks are imported, you can create a custom task as your default task with runs a few tasks chained together.\n\n```python\nfrom invoke import task\nfrom invoke_common_tasks import *\n\n@task(pre=[format, lint, typecheck, test], default=True)\ndef all(c):\n  """Default development loop."""\n  ...\n```\n\nYou will notice a few things here:\n\n1. The method has no implementation `...`\n1. We are chaining a series of `@task`s in the `pre=[...]` argument\n1. The `default=True` on this root tasks means we could run either `invoke all` or simply `invoke`.\n\nHow cool is that?\n\n# Contributing\n\nAt all times, you have the power to fork this project, make changes as you see fit and then:\n\n```sh\npip install https://github.com/user/repository/archive/branch.zip\n```\n[Stackoverflow: pip install from github branch](https://stackoverflow.com/a/24811490/622276)\n\nThat way you can run from your own custom fork in the interim or even in-house your work and simply use this project as a starting point. That is totally ok.\n\nHowever if you would like to contribute your changes back, then open a Pull Request "across forks".\n\nOnce your changes are merged and published you can revert to the canonical version of `pip install`ing this package.\n\nIf you\'re not sure how to make changes or if you should sink the time and effort, then open an Issue instead and we can have a chat to triage the issue.\n\n\n# Resources\n\n - [`pyinvoke`](https://pyinvoke.org)\n\n# Prior Art\n\n - https://github.com/Smile-SA/invoke-sphinx\n - https://github.com/Dashlane/dbt-invoke\n - https://invocations.readthedocs.io/en/latest/index.html\n\n',
    'author': 'Josh Peak',
    'author_email': 'neozenith.dev@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/neozenith/invoke-common-tasks',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
