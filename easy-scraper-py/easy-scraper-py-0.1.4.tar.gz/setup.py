# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['easy_scraper', 'easy_scraper.entity']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'easy-scraper-py',
    'version': '0.1.4',
    'description': 'An Easy Scraper for HTML',
    'long_description': '# easy-scraper-py\n\n![](https://img.shields.io/static/v1?label=+&message=Python%203.9%2B&color=lightblue&logo=Python)\n![](https://img.shields.io/static/v1?label=status&message=Work%20In%20Progress&color=red)\n[![PyPI](https://img.shields.io/pypi/v/easy-scraper-py.svg)](https://pypi.python.org/pypi/easy-scraper-py)\n\nAn easy scraping tool for HTML\n\n## Goal\n\nRe-implementation of [tanakh/easy-scraper](https://github.com/tanakh/easy-scraper) in Python.\n\n## Install from PyPI\n\n```bash\n   pip install easy-scraper-py\n```\n\n## Usage Example\n\n```html\n<!-- Target -->\n<body>\n    <b>NotMe</b>\n    <a class=here>Here</a>\n    <a class=nothere>NotHere</a>\n</body>\n\n<!-- Pattern -->\n<a class=here>{{ text }}</a>\n```\n\n```python\nimport easy_scraper\n\ntarget = r"""<body>\n    <b>NotMe</b>\n    <a class=here>Here</a>\n    <a class=nothere>NotHere</a>\n</body>\n"""  # newlines and spaces are all ignored.\n\npattern = "<a class=here>{{ text }}</a>"\n\neasy_scraper.match(target, pattern)  # [{\'text\': \'Here\'}]\n```\n\n```python\n# XML (RSS) scraping\nimport easy_scraper\nimport urllib.request\n\nbody = urllib.request.urlopen("https://kuragebunch.com/rss/series/10834108156628842505").read().decode()\nres = easy_scraper.match(body, "<item><title>{{ title }}</title><link>{{ link }}</link></item>")\nfor item in res[:5]:\n    print(item)\n```\n',
    'author': 'cympfh',
    'author_email': 'cympfh@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/cympfh/easy-scraper-py/',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
