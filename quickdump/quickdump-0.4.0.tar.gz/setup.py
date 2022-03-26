# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['quickdump']

package_data = \
{'': ['*']}

install_requires = \
['cloudpickle>=2.0.0,<3.0.0',
 'lz4>=4.0.0,<5.0.0',
 'multidict>=6.0.2,<7.0.0',
 'starlette[server]>=0.19.0,<0.20.0',
 'structlog>=21.5.0,<22.0.0',
 'uvicorn[server]>=0.17.6,<0.18.0']

entry_points = \
{'console_scripts': ['quickdump_http = quickdump.server_http:main',
                     'quickdump_tcp = quickdump.server_tcp:main']}

setup_kwargs = {
    'name': 'quickdump',
    'version': '0.4.0',
    'description': 'Quickly store arbitrary Python objects in unique files.',
    'long_description': '# quickdump\n\nQuickly store arbitrary Python objects in unique files.\n\n*Library status - this is an experimental work in progress that hasn\'t been\nbattle-tested at all. The API may change often between versions, and you may\nlose all your data.*\n\n---\n\n### Features\n\n- Store arbitrary objects with `cloudpickle` locally\n- No config or boilerplate required\n- Dump from TCP server\n- Dump from HTTP server\n\n### Notes\n(todo - rewrite this in a coherent manner)\n\n  - If an object from a library is dumped, the Python interpreter (or virtual\n    environment) must have the library installed.\n  - Currently, compression is applied per call to `dump`. This isn\'t very efficient.\n  - Labels are slugified to prevent errors from invalid characters in the filename.\n\n---\n```python\nfrom quickdump import QuickDumper, iter_dumps\n\nif __name__ == "__main__":\n    qd = QuickDumper("some_label")\n    test_size = 1000\n    qd(*[("one", "two", i) for i in range(test_size)])\n\n    # In a separate run...\n    \n    for obj in iter_dumps("some_label"):\n        print(obj)\n    # or:\n    for obj in qd.iter_dumps():\n        print(obj)\n```\n',
    'author': 'Pedro Batista',
    'author_email': 'pedrovhb@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pedrovhb/quickdump',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
