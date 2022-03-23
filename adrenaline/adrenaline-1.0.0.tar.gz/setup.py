# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['adrenaline', 'adrenaline._impl']

package_data = \
{'': ['*']}

extras_require = \
{':sys_platform == "darwin"': ['pyobjc-core>=8.0,<9.0',
                               'pyobjc-framework-Cocoa>=8.0,<9.0'],
 ':sys_platform == "linux"': ['jeepney>=0.6.0,<0.7.0']}

entry_points = \
{'console_scripts': ['adrenaline = adrenaline.__main__:main']}

setup_kwargs = {
    'name': 'adrenaline',
    'version': '1.0.0',
    'description': 'Keep your OS from sleeping (supports Windows and macOS)',
    'long_description': '`adrenaline`\n============\n\nSimple Python module to prevent your computer from going to sleep. Supports\nWindows and macOS at the moment; Linux support is coming soon (hopefully).\n\nUsage\n-----\n\nThe module provides a context manager named `prevent_sleep()`. The computer\nwill not go to sleep while the execution is in this context:\n\n```python\nfrom adrenaline import prevent_sleep\n\n\nwith prevent_sleep():\n    # do something important here\n    ...\n```\n\nOptionally, you can also prevent the screen from turning off:\n\n```python\nwith prevent_sleep(display=True):\n    # do something important here\n    ...\n```\n\nCommand line interface\n----------------------\n\nYou can also use this module from the command line as follows:\n\n```sh\n$ python -m adrenaline\n```\n\nThe command line interface will prevent sleep mode as long as it is running.\n\n\nAcknowledgments\n---------------\n\nThanks to [Michael Lynn](https://github.com/pudquick/pypmset) for figuring out\nhow to do this on macOS.\n\nThanks to [Niko Pasanen](https://github.com/np-8/wakepy) for the Windows\nversion.\n',
    'author': 'Tamas Nepusz',
    'author_email': 'ntamas@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ntamas/adrenaline',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
