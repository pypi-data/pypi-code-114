# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['combpyter', 'combpyter.lattice_paths']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib[plot]>=3.5.1,<4.0.0', 'numpy>=1.22.3,<2.0.0']

setup_kwargs = {
    'name': 'combpyter',
    'version': '0.0.3',
    'description': 'A lightweight Python library for generating and analyzing combinatorial objects.',
    'long_description': '# combpyter\n\nA lightweight Python library for generating and analyzing combinatorial objects.\n\n\n## Installation\n\nThe latest release is simply pip-installable via PyPI. Simply run\n```sh\npip install combpyter\n```\nto install the library.\n\n\n## Features\n\nPlease note that this is a personal and mostly research-driven project.\nAs such, the implemented combinatorial structures span, for the time being,\na narrow scope.\n\nCurrently, `combpyter` supports the following combinatorial objects:\n\n- Dyck paths (elements: `DyckPath`, generator: `DyckPaths`)\n\n\n## Example usage\n\nThis snippet iterates over all Dyck paths of semi-length 8 and computes\nthe distribution of the number of peaks (which is a statistic described\nby [Narayana numbers](https://en.wikipedia.org/wiki/Narayana_number)).\n\n```python\n>>> from combpyter import DyckPaths\n>>> from collections import defaultdict\n>>> peak_distribution = defaultdict(int)\n>>> for path in DyckPaths(8):\n...     num_peaks = len(path.peaks())\n...     peak_distribution[num_peaks] += 1\n...\n>>> for num_peaks, num_paths in peak_distribution.items():\n...     print(f"There are {num_paths} Dyck paths with {num_peaks} peaks.")\n...\nThere are 1 Dyck paths with 1 peaks.\nThere are 28 Dyck paths with 2 peaks.\nThere are 196 Dyck paths with 3 peaks.\nThere are 490 Dyck paths with 4 peaks.\nThere are 490 Dyck paths with 5 peaks.\nThere are 196 Dyck paths with 6 peaks.\nThere are 28 Dyck paths with 7 peaks.\nThere are 1 Dyck paths with 8 peaks.\n```\n',
    'author': 'Benjamin Hackl',
    'author_email': 'devel@benjamin-hackl.at',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/behackl/combpyter',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
