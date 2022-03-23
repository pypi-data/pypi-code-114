# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['suricataparser']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'suricataparser',
    'version': '0.0.8',
    'description': 'Package for parsing and generating Snort/Suricata rules.',
    'long_description': 'suricataparser |build-status| |py-versions| |pypi-version| |license|\n======================================================================\nPure python package for parsing and generating Snort/Suricata rules.\n\nInstall\n---------\nRequires Python >= 3.6.\n\n    pip install suricataparser\n\nUsage\n---------\n::\n\n    >>> from suricataparser import parse_rule, parse_file, parse_rules\n\nParse rules file:\n::\n\n    >>> rules = parse_file("suricata.rules")\n\nParse rules object (for embedding into scripts):\n::\n\n    >>> rules = parse_rules(rules_object)\n\nParse raw rule:\n::\n\n    >>> rule = parse_rule(\'alert tcp any any -> any any (sid:1; gid:1;)\')\n    >>> print(rule)\n    alert tcp any any -> any any (msg:"Msg"; sid:1; gid:1;)\n\nView rule properties:\n::\n\n    >>> rule.sid\n    1\n\n    >>> rule.action\n    alert\n\n    >>> rule.header\n    tcp any any -> any any\n\n    >>> rule.msg\n    \'"Msg"\'\n\nTurn on/off rule:\n::\n\n    >>> rule.enabled\n    True\n\n    >>> rule.enabled = False\n    >>> print(rule)\n    # alert tcp any any -> any any (msg:"Msg"; sid:1; gid:1;)\n\nModify options:\n::\n\n    >>> rule.add_option("http_uri")\n    >>> rule.add_option("key", "value")\n    >>> print(rule)\n    alert tcp any any -> any any (msg: "Msg"; sid: 1; gid: 1; http_uri; key: value;)\n\n    >>> rule.pop_option("key")\n    >>> print(rule)\n    alert tcp any any -> any any (msg: "Msg"; sid: 1; gid: 1; http_uri;)\n\n.. |build-status| image:: https://travis-ci.org/m-chrome/py-suricataparser.png?branch=master\n   :target: https://travis-ci.org/m-chrome/py-suricataparser\n.. |pypi-version| image:: https://badge.fury.io/py/suricataparser.svg\n   :target: https://pypi.org/project/suricataparser\n.. |license| image:: https://img.shields.io/pypi/l/suricataparser.svg\n   :target: https://github.com/m-chrome/py-suricataparser/blob/master/LICENSE\n.. |py-versions| image:: https://img.shields.io/pypi/pyversions/suricataparser.svg\n   :target: https://pypi.org/project/suricataparser\n',
    'author': 'Mikhail Tsyganov',
    'author_email': 'tsyganov.michail@yandex.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
