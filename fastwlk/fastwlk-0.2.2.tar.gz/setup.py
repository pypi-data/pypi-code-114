# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastwlk', 'fastwlk.utils']

package_data = \
{'': ['*']}

install_requires = \
['networkx>=2.6.3,<3.0.0',
 'numpy>=1.22.1,<2.0.0',
 'pandas>=1.4.0,<2.0.0',
 'tqdm>=4.62.3,<5.0.0']

setup_kwargs = {
    'name': 'fastwlk',
    'version': '0.2.2',
    'description': 'fastwlk is a Python package that implements a fast version of the Weisfeiler-Lehman kernel.',
    'long_description': "=============================\nFastWLK\n=============================\n\n.. image:: https://github.com/pjhartout/fastwlk/actions/workflows/main.yml/badge.svg\n        :target: https://github.com/pjhartout/fastwlk/\n\n\n.. image:: https://img.shields.io/pypi/v/fastwlk.svg\n        :target: https://pypi.python.org/pypi/fastwlk\n\n\n.. image:: https://codecov.io/gh/pjhartout/fastwlk/branch/main/graph/badge.svg?token=U054MJONED\n      :target: https://codecov.io/gh/pjhartout/fastwlk\n\n`Documentation`_.\n\n\nWhat does ``fastwlk`` do?\n-------------------------\n\n\n``fastwlk`` is a Python package that implements a fast version of the\nWeisfeiler-Lehman kernel. It manages to outperform current state-of-the-art\nimplementations on sparse graphs by implementing a number of improvements\ncompared to vanilla implementations:\n\n1. It parallelizes the execution of Weisfeiler-Lehman hash computations since\n   each graph's hash can be computed independently prior to computing the\n   kernel.\n\n2. It parallelizes the computation of similarity of graphs in RKHS by computing\n   batches of the inner products independently.\n\n3. On sparse graphs, lots of computations are spent processing positions/hashes\n   that do not actually overlap between graph representations. As such, we\n   manually loop over the overlapping keys, outperforming numpy dot\n   product-based implementations.\n\nThis implementation works best when graphs have relatively few connections and\nare reasonably dissimilar from one another. If you are not sure the graphs you\nare using are either sparse or dissimilar enough, try to benchmark this package\nwith others out there.\n\nHow fast is ``fastwlk``?\n-------------------------\n\nRunning the benchmark script in ``examples/benchmark.py`` shows that for the\ngraphs in ``data/graphs.pkl``, we get an approximately 80% speed improvement\nover other implementations like `grakel`_.\n\nTo see how much faster this implementation is for your use case:\n\n.. code-block:: console\n\n   $ git clone git://github.com/pjhartout/fastwlk\n   $ poetry install\n   $ poetry run python examples/benchmark.py\n\n\n.. _Documentation: https://pjhartout.github.io/fastwlk/\n.. _grakel: https://github.com/ysig/GraKeL\n",
    'author': 'Philip Hartout',
    'author_email': 'philip.hartout@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
