# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['arcdico']

package_data = \
{'': ['*']}

install_requires = \
['pyserial>=3.0,<4.0']

setup_kwargs = {
    'name': 'arcdico',
    'version': '1.0.0',
    'description': 'Python module to interact with the ArC Instruments Digital Control Module',
    'long_description': "# ArC Digital Control Module\n\nThis is a Python wrapper for the ArC Digital Control (ArC DiCo) serial protocol.\n\n## Usage\n\nUsage of the library is fairly straightforward. You only to know the serial\nport where the DiCo is connected to.\n\n```python\nfrom arcdico import DiCo\n\ndico = DiCo('/dev/ttyUSB0')\n\n# The DiCo will disable all outputs when initially\n# powered on but you can do that programmatically by\n# using the `reset` function.\ndico.reset()\n\n# connect specified pins to the DAC output\ndico.set_state(pins=[1, 8, 22])\n\n# set output voltage at 3.50 V\ndico.set_state(voltage=3.50)\n\n# or do both\ndico.set_state(pins=[1, 8], voltage=2.25)\n```\n",
    'author': 'Spyros Stathopoulos',
    'author_email': 'spyros@arc-instruments.co.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'http://www.arc-instruments.co.uk/products/arc-one/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
