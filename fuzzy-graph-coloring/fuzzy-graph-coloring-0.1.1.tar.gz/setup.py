# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['fuzzy_graph_coloring']
install_requires = \
['matplotlib>=3.5.1,<4.0.0',
 'networkx>=2.6.3,<3.0.0',
 'numpy>=1.22.2,<2.0.0',
 'pygad>=2.16.3,<3.0.0']

setup_kwargs = {
    'name': 'fuzzy-graph-coloring',
    'version': '0.1.1',
    'description': 'fuzzy-graph-coloring is a Python package for calculating the fuzzy chromatic number and coloring of a graph with fuzzy edges.',
    'long_description': 'fuzzy-graph-coloring\n********************\n\nfuzzy-graph-coloring is a Python package for calculating\nthe fuzzy chromatic number and coloring of a graph with fuzzy edges.\nIt will create a coloring with a minimal amount of incompatible edges\nusing a genetic algorithm (:code:`genetic_fuzzy_color`) or a greedy-k-coloring (:code:`greedy_k_color`)\ncombined with a binary search (:code:`alpha_fuzzy_color`).\n\nIf you don\'t know which one to use, we recommend :code:`alpha_fuzzy_color`.\nIf you are looking for a networkX coloring but with a given k, use :code:`greedy_k_color`.\n\nSee repository https://github.com/ferdinand-dhbw/fuzzy-graph-coloring\n\nQuick-Start\n===========\nInstall package: :code:`pip install fuzzy-graph-coloring`\n\nTry simple code:\n\n.. code-block::\n\n   import fuzzy-graph-coloring as fgc\n\n   TG1 = nx.Graph()\n   TG1.add_edge(1, 2, weight=0.7)\n   TG1.add_edge(1, 3, weight=0.8)\n   TG1.add_edge(1, 4, weight=0.5)\n   TG1.add_edge(2, 3, weight=0.3)\n   TG1.add_edge(2, 4, weight=0.4)\n   TG1.add_edge(3, 4, weight=1.0)\n\n   print(fgc.alpha_fuzzy_color(TG1, 3, return_alpha=True, fair=True))\n\nResult: :code:`({1: 0, 4: 1, 2: 2, 3: 2}, 0.918918918918919, 0.4)`\n\n(Tuple of coloring, score [(1-DTI)], and alpha [of alpha-cut])\n\nBibliography\n============\nThe project uses a lot of the by Keshavarz created basics:\nE. Keshavarz, "Vertex-coloring of fuzzy graphs: A new approach," Journal of Intelligent & Fuzzy Systems, vol. 30, pp. 883-893, 2016, issn: 1875-8967. https://doi.org/10.3233/IFS-151810\n\nLicense\n=======\nThis project is licensed under GNU General Public License v3.0 (GNU GPLv3). See :code:`LICENSE` in the code repository.\n\n\nSetup development environment\n=============================\n1. Get poetry https://python-poetry.org/docs/\n2. Make sure, Python 3.8 is being used\n3. :code:`poetry install` in your system shell\n4. :code:`poetry run pre-commit install`\n\nRun pre-commit\n--------------\n:code:`poetry run pre-commit run --all-files`\n\nRun pytest\n----------\n:code:`poetry run pytest .\\tests`\n\nCreate documentation\n--------------------\n:code:`.\\docs\\make html`\n',
    'author': 'Ferdinand Koenig and Jonas Rheiner',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ferdinand-dhbw/fuzzy-graph-coloring',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
