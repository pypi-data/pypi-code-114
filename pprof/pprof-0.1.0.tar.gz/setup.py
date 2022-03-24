# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pprof']

package_data = \
{'': ['*']}

install_requires = \
['line-profiler>=3.4.0,<4.0.0']

setup_kwargs = {
    'name': 'pprof',
    'version': '0.1.0',
    'description': 'Python profiling tool',
    'long_description': '## Installing\n\n```sh\npip install pprof\n```\n\nor\n\n```sh\npoetry add pprof\n```\n\n## A Simple Example\n\n```python\nfrom typing import List\nfrom pprof import cpu\n\ncpu.auto_report()\n\n@cpu\ndef run(arr: List) -> float:\n    tmp = []\n    for row in arr:\n        if row % 3 == 0:\n            tmp.append(row)\n    result = (sum(tmp*100) + len(arr)) / len(tmp)\n    return result\n\nrun(list(range(100000)))\n```\n\n```sh\n(venv) python run.py\n```\n\n## Links\n\n+ **line_profiler** (<https://github.com/pyutils/line_profiler>)\n',
    'author': 'mirecl',
    'author_email': 'grazhdankov@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0',
}


setup(**setup_kwargs)
