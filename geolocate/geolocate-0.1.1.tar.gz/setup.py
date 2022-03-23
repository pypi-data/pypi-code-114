# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['geolocate']

package_data = \
{'': ['*']}

install_requires = \
['p-tqdm>=1.3.3,<2.0.0', 'requests>=2.27.1,<3.0.0']

setup_kwargs = {
    'name': 'geolocate',
    'version': '0.1.1',
    'description': 'Georeferencing large amounts of data for free.',
    'long_description': '# Geolocate\n\nGeoreferencing large amounts of data for free.\n\n## How?\n\nIt\'s using the very same API that Waze uses to georeference addresses before\nit finds the best route to that destination. It requires no API keys, works\nreally well and has fairly high throughput.\n\nIn order to make this package extensible, there\'s an abstract class\n`GeolocateEngine` that defines the interface for the engines. This allows\nfor the addition of new engines without having to modify the code.\n\n## How do I use it?\n\nFirst you have to install the `geolocate` package for Python 3.7+:\n\n```\npip3 install geolocate\n```\n\nThen, for a single address:\n\n```py\n>>> from geolocate import geolocate\n>>> geolocate("1 Infinite Loop, Cupertino, CA 95014")\n{\'latitude\': 37.3311841, \'longitude\': -122.0287127}\n```\n\nOr, if you want to run things in parallel:\n\n```py\n>>> from geolocate import geolocate_batch\n>>> geolocate_batch(["1 Infinite Loop, Cupertino, CA 95014", "Eiffel Tower"])\n100%|███████| 2/2 [00:01<00:00,  1.66it/s]\n[{\'latitude\': 37.3311841, \'longitude\': -122.0287127}, {\'latitude\': 48.8560934, \'longitude\': 2.2930458}]\n```\n\n### Advanced usage\n\nBoth `geolocate` and `geolocate_batch` accept the following keyword arguments:\n\n- engine (`geolocate.engines.GeolocateEngine`): Engine to use for\n  geolocating the address. Defaults to `geolocate.engines.WazeEngine`\n- timeout (int): The timeout in seconds.\n- tries (int): The number of attempts to geolocate the address.\n- backoff_factor (float): The backoff factor. Delay will grow by\n  `{backoff factor} * (2 ** ({number of total retries} - 1))`.\n- on_not_found (str or callable): A callback function for when the\n  address is not found. The signature of the callback function\n  should be:\n  ```py\n  def callback(address: str):\n      ...\n  ```\n  where `address` is the address that was not found. The return\n  value of the callback function is returned by the geolocate\n  function.\n- on_error (str or callable): A callback function for when an error\n  occurs. The signature of the callback function should be:\n  ```py\n  def callback(address: str, error: Exception):\n      ...\n  ```\n  where `address` is the address that caused the error and\n  `error` is the exception that occurred. The return value of\n  the callback function is returned by the geolocate function.\n\nIn addition, the `geolocate_batch` function accepts the following\nkeyword arguments:\n\n- num_cpus (int): The number of CPUs to use. If None, the number of\n  CPUs will be determined automatically.\n',
    'author': 'Gabriel Gazola Milan',
    'author_email': 'gabriel.gazola@poli.ufrj.br',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/gabriel-milan/geolocate',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
