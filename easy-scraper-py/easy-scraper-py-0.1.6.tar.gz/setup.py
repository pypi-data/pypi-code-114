# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['easy_scraper', 'easy_scraper.entity']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'easy-scraper-py',
    'version': '0.1.6',
    'description': 'An Easy Scraper for HTML',
    'long_description': '# easy-scraper-py\n\n![](https://img.shields.io/static/v1?label=+&message=Python%203.9%2B&color=lightblue&logo=Python)\n![](https://img.shields.io/static/v1?label=status&message=Work%20In%20Progress&color=red)\n[![PyPI](https://img.shields.io/pypi/v/easy-scraper-py.svg)](https://pypi.python.org/pypi/easy-scraper-py)\n\nAn easy scraping tool for HTML\n\n## Goal\n\nRe-implementation of [tanakh/easy-scraper](https://github.com/tanakh/easy-scraper) in Python.\n\n## Install from PyPI\n\n```bash\n   pip install easy-scraper-py\n```\n\n## Usage Example\n\n### Scraping texts\n\n```html\n<!-- Target: full or partial HTML code -->\n<body>\n    <b>NotMe</b>\n    <a class=here>Here</a>\n    <a class=nothere>NotHere</a>\n</body>\n\n<!-- Pattern: partial HTML with variables ({{ name }}) -->\n<a class=here>{{ text }}</a>\n```\n\n```python\nimport easy_scraper\n\ntarget = r"""<body>\n    <b>NotMe</b>\n    <a class=here>Here</a>\n    <a class=nothere>NotHere</a>\n</body>\n"""  # newlines and spaces are all ignored.\n\n# Matching innerText under a-tag with class="here"\npattern = "<a class=here>{{ text }}</a>"\n\neasy_scraper.match(target, pattern)  # [{\'text\': \'Here\'}]\n```\n\n### Scraping links\n\n```python\ntarget = r"""\n<div>\n    <div class=here>\n        <a href="link1">foo</a>\n        <a href="link2">bar</a>\n        <a>This is not a link.</a>\n        <div>\n            <a href="link3">baz</a>\n        </div>\n    </div>\n    <div class=nothere>\n        <a href="link4">bazzz</a>\n    </div>\n</div>\n"""\n\n# Marching links (href and innerText) under div-tag with class="here"\npattern = r"""\n    <div class=here>\n        <a href="{{ link }}">{{ text }}</a>\n    </div>\n"""\n\nassert easy_scraper.match(target, pattern) == [\n    {"link": "link1", "text": "foo"},\n    {"link": "link2", "text": "bar"},\n    {"link": "link3", "text": "baz"},\n]\n```\n\n### Scraping RSS (XML)\n\n`easy-scraper-py` just uses [html.parser](https://docs.python.org/ja/3/library/html.parser.html) for parsing, also can parse almost XML.\n\n```python\nimport easy_scraper\nimport urllib.request\n\nbody = urllib.request.urlopen("https://kuragebunch.com/rss/series/10834108156628842505").read().decode()\nres = easy_scraper.match(body, "<item><title>{{ title }}</title><link>{{ link }}</link></item>")\nfor item in res[:5]:\n    print(item)\n```\n\n### Scraping Images\n\n```python\nimport easy_scraper\nimport urllib.request\n\nurl = "https://unsplash.com/s/photos/sample"\nbody = urllib.request.urlopen(url).read().decode()\n\n# Matching all images\nres = easy_scraper.match(body, r"<img src=\'{{ im }}\' />")\nprint(res)\n\n# Matching linked (under a-tag) images\nres = easy_scraper.match(body, r"<a href=\'{{ link }}\'><img src=\'{{ im }}\' /></a>")\nprint(res)\n```\n',
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
