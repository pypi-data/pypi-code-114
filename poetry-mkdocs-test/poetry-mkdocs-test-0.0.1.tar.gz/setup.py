# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['plugin']
install_requires = \
['Jinja2>=3.0.3,<4.0.0', 'mkdocs>=1.2.3,<2.0.0', 'requests>=2.27.1,<3.0.0']

entry_points = \
{'console_scripts': ['mkdocs.plugins = external-markdown = '
                     'external_markdown.plugin:EmbedExternalMarkdown']}

setup_kwargs = {
    'name': 'poetry-mkdocs-test',
    'version': '0.0.1',
    'description': 'Mkdocs plugin that allow to inject external markdown or markdown section from given url',
    'long_description': None,
    'author': 'fire1ce',
    'author_email': 'dev@3os.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
