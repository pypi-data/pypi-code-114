# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['parserkiosk', 'parserkiosk.templates']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.0.3,<4.0.0', 'PyYAML>=6.0,<7.0', 'python-box>=5.4.1,<6.0.0']

entry_points = \
{'console_scripts': ['parserkiosk = parserkiosk:main']}

setup_kwargs = {
    'name': 'parserkiosk',
    'version': '0.1.0',
    'description': 'A Proof of Concept multi-lingual test generation suite intended for parsers.',
    'long_description': '## ParserKiosk: A Proof of Concept multi-lingual test generation suite intended for parsers\n\n### Motivation\nAfter reading this [article](https://seriot.ch/projects/parsing_json.html) and [this one](https://bishopfox.com/blog/json-interoperability-vulnerabilities), I am now paranoid and under the assumption that implementations of data serialization and deserialization have a lot of quirks that differ from language to language, and implementation to implementation.\n\nThis _could_ lead to serious security issues as applications, especially web applicatons _usually_ utilize multiple services, written in multiple languages that use the same format to communicate. \n\nReference implementations usually provide tests, but translating them from language to language is tiresome and tedious. I wanted to compose a library to generate **simple**, functional tests for multiple languages with minimal repitition. \n\n### How does it work?\nParserkiosk uses ``jinja2`` templates to generate test cases from ``yaml`` file(s). You can either expect something to fail(raise an "exception" or "error") or use a function that you define in a special file called ```commons``` to assert if the parsed data matches the expected internal representation. \n\nLet\'s say you\'ve written a reference implementation of your data de/serialization format in ``Go`` and I wanted to implement it in ``Python``.  \nAll I would need to do to implement your test-suite is:\n1. Write a ```commons.py``` file implementing the same assertion functions that you\'ve written in your ``commons.go`` file\n2. Run ```$ parserkiosk folder_with_yaml_test_files/ --builtin python``` and _voila_ I have your entire test suite implemented!\n\nFor more on this, see ```examples/json/```\n\n### Languages supported\n- [x] Python / pytest / ``python``\n- [x] NodeJS / jest (sync) / ``node_js``\n- [ ] NodeJS / jest (async)\n- [ ] Go\n- [ ] Java\n- [ ] PHP\n- [ ] Perl\n- [ ] Ruby\n- [ ] ...\n\n### How do I use it?\nSee [HOWTO](HOWTO.md)\n\n### License\nAll work is licensed under ```GPL-3.0``` excluding the example JSON test-suite which is licensed under ```MIT```\n\n### Contributing\nIssues, feedback and pull requests are welcome. I have tried _my best_ to keep the code simple. Please keep in mind that I wish to limit features that we accomodate to keep it simple. Tests should be simple and readable.\n\n### Thanks\nSpecial thanks to [nst](https://github.com/nst/) for inspiring Parserkiosk. All test cases in ``examples/json`` come from his [incredible work](https://github.com/nst/JSONTestSuite)\n',
    'author': 'aarnav',
    'author_email': 'aarnavbos@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/R9295/parser-kiosk',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
