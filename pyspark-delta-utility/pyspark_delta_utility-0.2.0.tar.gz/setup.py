# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pyspark_delta_utility']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyspark-delta-utility',
    'version': '0.2.0',
    'description': 'A useful python package that consists of pyspark and delta utilities',
    'long_description': '# pyspark_delta_utility\n\nA useful python package that consists of pyspark and delta utilities\n\n## Installation\n\n```bash\n$ pip install pyspark_delta_utility\n```\n\n## Usage\n\n- TODO\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n## License\n\n`pyspark_delta_utility` was created by Kyle Ahn. It is licensed under the terms of the MIT license.\n\n## Credits\n\n`pyspark_delta_utility` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n',
    'author': 'Kyle Ahn',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<3.10',
}


setup(**setup_kwargs)
