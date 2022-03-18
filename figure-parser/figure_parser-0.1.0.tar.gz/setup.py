# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['figure_parser',
 'figure_parser.alter',
 'figure_parser.gsc',
 'figure_parser.native']

package_data = \
{'': ['*'], 'figure_parser.gsc': ['locale/*']}

install_requires = \
['PyYAML>=5.2,<6.0',
 'aiohttp>=3.7.4,<4.0.0',
 'beautifulsoup4>=4.9.3',
 'feedparser>=6.0.8,<7.0.0',
 'lxml>=4.6.5',
 'pytz>=2021.1,<2022.0',
 'requests>=2.25.1',
 'toml>=0.10.2,<0.11.0']

extras_require = \
{'docs': ['Sphinx>=4.0.3,<5.0.0',
          'furo>=2021.7.5-beta.38,<2022.0.0',
          'sphinx-autodoc-typehints>=1.12.0,<2.0.0']}

setup_kwargs = {
    'name': 'figure-parser',
    'version': '0.1.0',
    'description': 'Parser for figure',
    'long_description': '[![Pypi](https://img.shields.io/pypi/pyversions/figure_parser.svg?style=flat-square)](https://pypi.org/project/figure_parser/)\n[![Pypi](https://img.shields.io/pypi/v/figure_parser.svg?style=flat-square)](https://pypi.org/project/figure_parser/)\n[![CI](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2FFigureHook%2Ffigure_parser%2Fbadge%3Fref%3Dmain&style=flat-square)](https://actions-badge.atrox.dev/FigureHook/figure_parser/goto?ref=main)\n[![Coverage](https://img.shields.io/coveralls/github/FigureHook/figure_parser?style=flat-square)](https://coveralls.io/github/FigureHook/figure_parser)\n\n## Maker List\n|                                      | Product parser | Delay parser | Shipment parser |\n| ------------------------------------ | -------------- | ------------ | --------------- |\n| [GSC](https://www.goodsmile.info/)   | V              |              | V               |\n| [Alter](https://alter-web.jp/)       | V              |              |                 |\n| [native](https://www.native-web.jp/) | V              |              |                 |\n| [F:NEX](https://fnex.jp/) |                |              |                 |\n| [SKYTUBE](https://skytube.jp/) |                |              |                 |\n| [quesQ](https://www.quesq.net/) |                |              |                 |\n| [AMAKUNI](http://amakuni.info/) |                |              |                 |\n| [alphamax](https://alphamax.jp/) |                |              |                 |\n| [ORCATORYS](http://orcatoys.com/) |                |              |                 |\n| [FLARE](https://www.flare-web.jp/) |                |              |                 |\n| [spiritale](https://spiritale.jp/) |                |              |                 |\n| [TokyoFigure](https://tokyofigure.jp/) |                |              |                 |\n| [daikikougyou](https://daikikougyou.com/) |                |              |                 |\n| [OrchidSeed](http://www.orchidseed.co.jp/) |                |              |                 |\n| [union-creative](https://union-creative.jp/) |                |              |                 |\n| [alphaomega](https://www.alphaomega-web.jp/) |                |              |                 |\n| [PLUM](https://www.pmoa.co.jp/product/fi.html) |                |              |                 |\n| [WAVE](https://www.hobby-wave.com/products-cat/figure/) |                |              |                 |\n| [KOTOBUKIYA](https://www.kotobukiya.co.jp/product-category/figure/) |                |              |                 |\n| [MegaHouse](https://www.megahouse.co.jp/products/highqualityfigure/) |                |              |                 |\n\n## Shop List\n- [ ] HobbyJapan\n- [ ] amiami\n- [ ] toranoana\n- [ ] melonbooks',
    'author': 'Elton Chou',
    'author_email': 'plscd748@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/FigureHook/figure_parser',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
