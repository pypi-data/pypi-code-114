# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nndict']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'nndict',
    'version': '2.0.1',
    'description': 'A dict that does not support None entries. Silently deletes entry if updated to null and works recursively.',
    'long_description': '# NeverNoneDict\nPython Dictionary that does not have None values.\n\n### Installing\n\nYou can start using nn dict by installing it using pip.\n```bash\npip install nndict\n```\n\n\n### Using nndict\n```python\n>nndict_ = nndict({"a": 2, "b": None, "c": {"d": None}})\n>print(nndict_)\n{\'a\': 2, \'c\': {}}\n\n>nndict_ = nndict({"a": 2})\n>print(nndict_)\n{\'a\': 2}\n\n>nndict_["a"] = None\n>print(nndict_)\n{}\n```\n\n## Running the tests\nMake sure you have the python versions listed in tox.ini installed. Then run tox:\n```bash\ntox\n```\n\n## Authors\n\n* **Tiago Santos** - *Initial work* - tiago.santos@vizidox.com\n\n',
    'author': 'Tiago Santos',
    'author_email': 'tiago.santos@vizidox.com',
    'maintainer': 'Joana Teixeira',
    'maintainer_email': 'joana.teixeira@vizidox.com',
    'url': 'https://vizidox.com',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
