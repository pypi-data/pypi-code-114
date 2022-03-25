# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hydrus', 'hydrus_api']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.26.0,<3.0.0']

setup_kwargs = {
    'name': 'hydrus-api',
    'version': '3.22.7',
    'description': 'Python module implementing the Hydrus API',
    'long_description': '# Hydrus API\nPython module implementing the Hydrus API.\n\n# Requirements\n- Python >= 3.9 (I think; Let me know if you can use this with an older Python version)\n- requests library (`pip install requests`)\n\n# Installation\n`$ pip install hydrus-api`\n\nIf you want to use the package in your own (installable) Python project, specify it in your `setup.py` using:\n`install_requires=[\'hydrus-api\']`.\n\n# Contributing\nPlease feel free to contribute in the form of a pull request when the API changes (keep close to the existing code style\nor you\'ll create more work than help); I\'ve been bad about merging these until now, I\'ll try to be more conscientious of\nthem.\n\nTry to avoid checking in your modifications to `.vscode/settings.json` and `.env` please.\n\nI can\'t guarantee any fixed timespan in which I\'ll update this module myself when the API changes -- the only reason it\nwas updated now is because prkc kept bugging me; So if you desperately need this module to be updated, please create a\npull request.\n\n# Description\nRead the (latest) official documentation [here](https://hydrusnetwork.github.io/hydrus/help/client_api.html).\n\nWhen instantiating `hydrus_api.Client` the `acccess_key` is optional, allowing you to initially manually request\npermissions using `request_new_permissions()`. Alternatively there is `hydrus_api.utils.request_api_key()` to make this\neasier. You can instantiate a new `Client` with the returned access key after that.\n\nIf the API version the module is developed against and the API version of the Hydrus client differ, there is a chance\nthat using this API module might have unintended consequences -- be careful.\n\nIf something with the API goes wrong, a subclass of `APIError` (`MissingParameter`, `InsufficientAccess`,\n`DatabaseLocked`, `ServerError`) or `APIError` itself will be raised with the\n[`requests.Response`](http://docs.python-requests.org/en/master/api/#requests.Response) object that caused the error.\n`APIError` will only be raised directly, if the returned status code is unrecognized.\n\nThe module provides `Permission`, `URLType`, `ImportStatus`, `TagAction`, `TagStatus`, `PageType` and `FileSortType`\nEnums for your convenience. Due to a limitation of JSON, all dictionary keys that are returned by the client will be\nstrings, so when using Enum members to index a dictionary that was returned by the client, make sure to use the string\nrepresentation of its value. Usually you would have to do this: `str(Enum.member.value)`, but the listed Enums allow you\nto just do `str(Enum.member)` instead to get the string representation of the member\'s value directly.\n\nThe client provides convenience methods that are not strictly part of the API: `add_and_tag_files()` and\n`get_page_list()`; read their docstrings to figure out what they do. Some more utility functions besides\n`request_api_key()` are also available in `hydrus_api.utils`.\n\nIn places where the API returns a dictionary with a single, useless top-level key, the key\'s value will be returned\ndirectly instead (e.g. "access_key" for `/request_new_permissions` or "cookies" for `/manage_cookies/get_cookies`).\n\nThe client methods `add_file()` and `add_and_tag_files()` accept `str`, `pathlib.Path` and objects that implement the\ninternal `BinaryFileLike` protocol (i.e. all objects that provide a `read()`-method that returns `bytes`).\n\nThe function `hydrus_api.utils.parse_hydrus_metadata_file` behaves similarly, except that it accepts objects that\nimplement the internal `TextFileLike` protocol (i.e. its `read()`-method returns a string).\n\nCheck out `examples/` for some example applications. Some of them might be outdated, but they should be good enough to\ngive you an idea how to use the module.\n',
    'author': 'cryzed',
    'author_email': 'cryzed@googlemail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/cryzed/hydrus-api',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
