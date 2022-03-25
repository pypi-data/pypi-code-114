# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cpstl',
 'cpstl.algorithm',
 'cpstl.algorithm.sort',
 'cpstl.datatype',
 'cpstl.datatype.graph',
 'cpstl.datatype.heap']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'cpstl',
    'version': '0.0.2',
    'description': 'Copy and Paste standard library (CPSTL) is a repository with a collection of data structure and algorithms in many different languages',
    'long_description': '# Python Copy and Paste standard Library\n\nPython Copy and Paste standard library (CPSTL) is a repository with a collection of data structure and algorithms.\n\n## TODO\nAdd more content\n\n\n## License\n\n<div align="center">\n  <img src="https://opensource.org/files/osi_keyhole_300X300_90ppi_0.png" width="150" height="150"/>\n</div>\n\n    Collection of algorithm\'s and data struct developer in different language\n    and with the Code Style guide line, to resolve Competitive Programming problem.\n    Copyright (C) 2020-2021 Vincenzo Palazzo vincenzopalazzodev@gmail.com\n\n    This program is free software; you can redistribute it and/or modify\n    it under the terms of the GNU General Public License as published by\n    the Free Software Foundation; either version 2 of the License, or\n    (at your option) any later version.\n\n    This program is distributed in the hope that it will be useful,\n    but WITHOUT ANY WARRANTY; without even the implied warranty of\n    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n    GNU General Public License for more details.\n\n    You should have received a copy of the GNU General Public License along\n    with this program; if not, write to the Free Software Foundation, Inc.,\n    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.',
    'author': 'Vincenzo Palazzo',
    'author_email': 'vincenzopalazzodev@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://vincenzopalazzo.github.io/cpstl',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
