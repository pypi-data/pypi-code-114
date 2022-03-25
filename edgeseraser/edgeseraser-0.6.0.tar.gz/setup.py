# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['edgeseraser', 'edgeseraser.misc', 'edgeseraser.polya_tools']

package_data = \
{'': ['*']}

install_requires = \
['igraph',
 'llvmlite>=0.37.0',
 'networkx',
 'numba',
 'numpy',
 'scipy',
 'typing_extensions']

setup_kwargs = {
    'name': 'edgeseraser',
    'version': '0.6.0',
    'description': 'A short description of the project',
    'long_description': '# Edges Eraser\n\n[![PyPI](https://img.shields.io/pypi/v/edgeseraser?style=flat-square)](https://pypi.python.org/pypi/edgeseraser/)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/edgeseraser?style=flat-square)](https://pypi.python.org/pypi/edgeseraser/)\n[![PyPI - License](https://img.shields.io/pypi/l/edgeseraser?style=flat-square)](https://pypi.python.org/pypi/edgeseraser/)\n\n[![Coookiecutter - Wolt](https://img.shields.io/badge/cookiecutter-Wolt-00c2e8?style=flat-square&logo=cookiecutter&logoColor=D4AA00&link=https://github.com/woltapp/wolt-python-package-cookiecutter)](https://github.com/woltapp/wolt-python-package-cookiecutter)\n\n\n---\n\n**Documentation**: [https://devmessias.github.io/edgeseraser](https://devmessias.github.io/edgeseraser)\n\n**Source Code**: [https://github.com/devmessias/edgeseraser](https://github.com/devmessias/edgeseraser)\n\n**PyPI**: [https://pypi.org/project/edgeseraser/](https://pypi.org/project/edgeseraser/)\n\n---\n\n## What is Edges Eraser?\nThis pkg aims to implement serveral filtering methods for (un)directed graphs.\n\nEdge filtering methods allows to extract the backbone of a graph or sampling the most important edges. You can use edge filtering methods as a preprocessing step aiming to improve the performance/results of graph algorithms or to turn a graph visualtzation more asthetic.\n\n\n## Example\n```python\nimport networkx as nx\nimport edgeseraser as ee\n\ng = nx.erdos_renyi_graph(100, 0.1)\nee.noise_score.filter_nx_graph(g)\n\ng # filtered graph\n```\n\n## Available methods and details\n\n| Method | Description | suitable for | limitations/restrictions/details |\n| --- | --- |--- | --- |\n| [Noise Score] | Filters edges with high noise score. Paper:[1]|Directed, Undirected, Weighted | Very good and fast! [4] |\n| [Disparity] | Dirichlet process filter (stick-breaking) Paper:[2] |  Directed, Undirected, Weighted |There are some criticism regarding the use in undirected graphs[3]|\n| [Pólya-Urn]| Filters edges with Pólya-Urn method. Paper:[5]| Directed, Undirected, Integer Weighted||\n\n[1]: https://arxiv.org/abs/1701.07336\n[2]: https://arxiv.org/abs/0904.\n[3]: https://arxiv.org/abs/2101.00863\n[4]: https://www.michelecoscia.com/?p=1236\n[5]: https://www.nature.com/articles/s41467-019-08667-3\n[Noise Score]: /api_docs/#edgeseraser.noise_score\n[Disparity]: /api_docs/#edgeseraser.disparity\n\n\n## Installation\n\n```sh\npip install edgeseraser\n```\n\n## Development\n\n* Clone/Fork this repository\n\n```sh\ngit clone https://github.com/devmessias/edgeseraser\n```\n\n* Requirements:\n  * [Poetry](https://python-poetry.org/)\n  * Python 3.7+\n\n```sh\nmake install\nmake init\n```\n\n### Testing\n\n```sh\nmake test\n```\n\nTo run the static analysis, use the following command:\n```sh\nmake mypy\n```\n\n### Documentation\n\nThe documentation is automatically generated from the content of the [docs directory](./docs) and from the docstrings\n of the public signatures of the source code. The documentation is updated and published as a [Github project page\n ](https://pages.github.com/) automatically as part each release.\n\nTo see the current state of the documentation in your browser, use the following command:\n```sh\nmake docs-serve\n```\nThe above command will start a local server on port 8000. Any changes to\nthe documentation and docstrings will be automatically reflected in your browser.\n\n### Pre-commit\n\nPre-commit hooks run all the auto-formatters (e.g. `black`, `isort`), linters (e.g. `mypy`, `flake8`), and other quality\n checks to make sure the changeset is in good shape before a commit/push happens.\n\n\nIf you want e.g. want to run all checks manually for all files:\n\n```sh\nmake pre-commit\n```\n',
    'author': 'Bruno Messias',
    'author_email': 'devmessias@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://devmessias.github.io/edgeseraser',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<3.11',
}


setup(**setup_kwargs)
