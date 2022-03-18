# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['epcpy', 'epcpy.epc_schemes', 'epcpy.utils']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['test = scripts:test']}

setup_kwargs = {
    'name': 'epcpy',
    'version': '0.1.1',
    'description': "A Python module for creation, validation, and transformation of EPC representations as defined in GS1's EPC Tag Data Standard (https://www.gs1.org/standards/rfid/tds).",
    'long_description': "# EPCPY\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)\n[![PyPI version](https://badge.fury.io/py/epcpy.svg)](https://badge.fury.io/py/epcpy)\n\n\nA Python module for creation, validation, and transformation of EPC representations as defined in GS1's EPC Tag Data Standard (https://www.gs1.org/standards/rfid/tds).\n\n## Installation\n```python\npip install epcpy\n```\n\n## Documentation\nDocumentation can be found on [Git](https://github.com/nedap/retail-epcpy).",
    'author': 'Nedap Retail',
    'author_email': 'sander.meinderts@nedap.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/nedap/retail-epcpy',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
