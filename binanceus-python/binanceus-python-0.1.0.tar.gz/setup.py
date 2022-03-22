# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['rest_bs', 'websocket_bs']

package_data = \
{'': ['*']}

install_requires = \
['binance-connector>=1.11.0,<2.0.0',
 'requests>=2.27.1,<3.0.0',
 'websocket-client>=1.3.1,<2.0.0']

setup_kwargs = {
    'name': 'binanceus-python',
    'version': '0.1.0',
    'description': 'A lightweight Python wrapper for the binance.us public API.',
    'long_description': '# binanceus-python\nA lightweight Python wrapper for the binance.us public API. \n\nUses [binance-connector-python](https://github.com/binance/binance-connector-python) for API connectivity.\n\nI am in no way affiliated with Binance or Binance US. Use this at your own risk.\n\n## Quick Start\nInstall binanceus-python: `pip install binanceus-python` \n\nHere\'s some example code to get started with:\n\n```python\nfrom websocket_bs.client import BsWebsocketClient\nimport time\n\n# start real-time ticker stream for symbol BTCUSD\nsymbol = \'BTCUSD\'\n\nws = BsWebsocketClient()\nws.subscribe(symbol)\nws.start()\n\n\n# print live ticker feed\ntry:\n    while True:\n        book_top = ws.get_book_top(symbol)\n        bid = book_top[0]\n        bid_qty = book_top[1]\n        ask = book_top[2]\n        ask_qty = book_top[3]\n        print(f\'{symbol} SPOT orderbook_top: ({bid:0.4f}, {bid_qty})  ({ask:0.4f}, {ask_qty})\')\n        time.sleep(1)\nexcept KeyboardInterrupt as e:\n    print("Program finished.")\n    ws.stop()\n```\n\n## Contributing \nContributions, fixes, recommendations, and all other feedback is welcome. If you are fixing a bug, please open an issue first with all relevant details, and mention the issue number in the pull request.\n\n### Contact \nI can be reached on discord at Nenye#5335, or through email at nenye@ndili.net. Otherwise, feel free to open a PR or Issue here.\n',
    'author': 'Nenye Ndili',
    'author_email': 'nenye@ndili.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/nenyehub/binanceus-python',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
