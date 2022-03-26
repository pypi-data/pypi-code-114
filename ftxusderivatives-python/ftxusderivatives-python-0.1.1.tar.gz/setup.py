# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['rest_lx', 'websocket_lx']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.27.1,<3.0.0', 'websocket-client>=1.3.1,<2.0.0']

setup_kwargs = {
    'name': 'ftxusderivatives-python',
    'version': '0.1.1',
    'description': 'An unofficial Python wrapper for the REST and WebSocket APIs of FTX US Derivatives, formerly known as LedgerX.',
    'long_description': '# ftxusderivatives-python\nAn unofficial Python wrapper for the [REST and WebSocket APIs](https://docs.ledgerx.com/reference/overview) of FTX US Derivatives, formerly known as LedgerX. I have no affiliation with FTX US Derivatives. Use this at your own risk.\n\n## Features\n- Implementation of all REST endpoints, detailed [here](https://docs.ledgerx.com/reference/overview)\n- WebSocket implementation: live orderbook tops, account balances, open positions info, order fills, server heartbeat, reconnect logic\n- Simple handling of authentication\n- HTTP request error handling and retry logic\n- Logging support\n\n## Quick Start\n[Register an account with FTX US Derivatives.](https://derivs.ftx.us/) *[optional]*\n\n[Generate an API key](https://docs.ledgerx.com/docs/api-key) and configure permissions. *[optional]*\n\nInstall ftxusderviatives-python: `pip install ftxusderivatives-python`\n\nHere\'s some example code to get started with. Note that API calls that require authentication will not work if you do not\nenter your API key.\n\n```python\n###############################\n# REST API Example\n###############################\nfrom rest_lx.rest import LxClient\n\napi_key = ""  # TODO: Put API key here\n\n# Init REST client\nclient = LxClient(api_key=api_key)\n\n# list active day-ahead-swap contracts\nswaps = client.list_contracts({\n    \'active\': True,\n    \'derivative_type\': \'day_ahead_swap\',\n})\n\n# grab BTC day-ahead-swap contract ID\ndata = swaps[\'data\']\ncbtc_swap = filter(lambda data: data[\'underlying_asset\'] == \'CBTC\', data)\ncontract_id = next(cbtc_swap)[\'id\']\nprint(f"BTC swap contract_id: {contract_id}")\n\n# retrieve your position for BTC day-ahead-swap contract (requires authentication)\nposition = client.retrieve_contract_position(contract_id)\nprint(f"BTC swap position: {position}")\n\n# place bid for BTC next-day swap\nlx_buy = {\n    \'order_type\': \'limit\',\n    \'contract_id\': contract_id,\n    \'is_ask\': False,\n    \'swap_purpose\': \'undisclosed\',\n    \'size\': 1,\n    \'price\': 100,  # $1 (100 cents)\n    \'volatile\': True\n}\norder = client.create_order(**lx_buy)\n\n# cancel placed order\nmessage_id = order[\'data\'][\'mid\']  # order ID\nclient.cancel_single_order(message_id=message_id, contract_id=contract_id)\n\n###############################\n# WebSocket Example\n###############################\nfrom websocket_lx.client import LxWebsocketClient\nimport time\n\n# Init WebSocket client\nws = LxWebsocketClient(api_key=api_key)\n\n# Subscribe to orderbook-top feed for BTC day-ahead-swap contract\nws.subscribe(contract_id=contract_id)\nws.connect()\n\n# Grab orderbook-top for BTC day-ahead-swap once a second\nwhile True:\n    top = ws.get_book_top(contract_id=contract_id)\n    print(top)\n    time.sleep(1)\n```\n\n## Todo\n- Repo documentation\n- [Order fills, cancels, and insertions support](https://docs.ledgerx.com/reference/market-data-feed)\n\n## Contributing \nContributions, fixes, recommendations, and all other feedback is welcome. If you are fixing a bug, please open an issue first with all relevant details, and mention the issue number in the pull request.\n\n### Contact \nI can be reached on discord at Nenye#5335, or through email at nenye@ndili.net. Otherwise, feel free to open a PR or Issue here.\n',
    'author': 'Nenye Ndili',
    'author_email': 'nenye@ndili.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/nenyehub/ftxusderivatives-python',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
