# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['marquedown']

package_data = \
{'': ['*']}

install_requires = \
['Markdown>=3.3.6,<4.0.0']

setup_kwargs = {
    'name': 'marquedown',
    'version': '0.3.0',
    'description': 'Extending Markdown further by adding a few more useful notations.',
    'long_description': '# Marquedown\n\nExtending Markdown further by adding a few more useful notations.\nIt can be used in place of `markdown` as it also uses and applies it.\n\n## Examples\n\n### Blockquote with citation\n\nThis is currently limited to the top scope with no indentation.\nSurrounding dotted lines are optional.\n\n```md\n......................................................\n> You have enemies? Good. That means you\'ve stood up\n> for something, sometime in your life.\n-- Winston Churchill\n\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\n```\n\n```html\n<blockquote>\n    <p>\n        You have enemies? Good. That means you\'ve stood up\n        for something, sometime in your life.\n    </p>\n    <cite>Winston Churchill</cite>\n</blockquote>\n```\n\n### Embed video\n\n#### YouTube\n\n```md\n![dimweb](https://youtu.be/VmAEkV5AYSQ "An embedded YouTube video")\n```\n\n```html\n<iframe\n    src="https://www.youtube.com/embed/VmAEkV5AYSQ"\n    title="An embedded YouTube video" frameborder="0"\n    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"\n    allowfullscreen>\n</iframe>\n```',
    'author': 'Maximillian Strand',
    'author_email': 'maximillian.strand@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/deepadmax/marquedown',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
