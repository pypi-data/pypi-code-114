# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['celery_typed_tasks']

package_data = \
{'': ['*']}

install_requires = \
['celery>5']

extras_require = \
{'docs': ['mkdocs', 'mkdocs-material', 'mkautodoc']}

setup_kwargs = {
    'name': 'celery-typed-tasks',
    'version': '0.1.25',
    'description': '',
    'long_description': None,
    'author': 'massover',
    'author_email': 'joshm@simplebet.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
