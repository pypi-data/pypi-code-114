# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rasam', 'rasam.components', 'rasam.importers']

package_data = \
{'': ['*']}

install_requires = \
['Faker>=8.1.4,<14.0.0', 'rasa>=2.8.12,<3.0.0', 'urlextract>=1.2.0,<2.0.0']

setup_kwargs = {
    'name': 'rasam',
    'version': '0.5.2',
    'description': 'Rasa Improved',
    'long_description': '<table>\n    <tr>\n        <td>License</td>\n        <td><img src=\'https://img.shields.io/pypi/l/rasam.svg?style=for-the-badge\' alt="License"></td>\n        <td>Version</td>\n        <td><img src=\'https://img.shields.io/pypi/v/rasam.svg?logo=pypi&style=for-the-badge\' alt="Version"></td>\n    </tr>\n    <tr>\n        <td>Github Actions</td>\n        <td><img src=\'https://img.shields.io/github/workflow/status/roniemartinez/rasam/Python?label=actions&logo=github%20actions&style=for-the-badge\' alt="Github Actions"></td>\n        <td>Coverage</td>\n        <td><img src=\'https://img.shields.io/codecov/c/github/roniemartinez/rasam/branch?label=codecov&logo=codecov&style=for-the-badge\' alt="CodeCov"></td>\n    </tr>\n    <tr>\n        <td>Supported versions</td>\n        <td><img src=\'https://img.shields.io/pypi/pyversions/rasam.svg?logo=python&style=for-the-badge\' alt="Python Versions"></td>\n        <td>Wheel</td>\n        <td><img src=\'https://img.shields.io/pypi/wheel/rasam.svg?style=for-the-badge\' alt="Wheel"></td>\n    </tr>\n    <tr>\n        <td>Status</td>\n        <td><img src=\'https://img.shields.io/pypi/status/rasam.svg?style=for-the-badge\' alt="Status"></td>\n        <td>Downloads</td>\n        <td><img src=\'https://img.shields.io/pypi/dm/rasam.svg?style=for-the-badge\' alt="Downloads"></td>\n    </tr>\n</table>\n\n# rasam\n\nRasa Improved\n\n## Usage\n\n### Installation\n\n```bash\npip install rasam\n```\n\n### Rasa `config.yml`\n\n```yaml\nimporters:\n  - name: rasam.PlaceholderImporter\n    fake_data_count: 10  # default value is 1\n\npipeline:\n  - name: rasam.RegexEntityExtractor\n  - name: rasam.URLEntityExtractor\n```\n\n### Rasa `nlu.yml`\n\n#### PlaceholderImporter\n\nThe `PlaceholderImporter` removes the need to write unnecessary information (eg. name, address, numbers, etc.) and helps focus on writing test data.\n\n#### Using `{}` placeholder\n\n```yaml\nnlu:\n- intent: tell_name\n  examples: |\n    - My name is {name}\n    - I am {name} and he is {name}\n```\n\n#### Using `@` placeholder\n\n```yaml\nnlu:\n- intent: tell_address\n  examples: |\n    - I live in @address\n    - I stay at @address and @address\n```\n\n#### Mixing `{}` and `@` placeholders\n\nIt is possible to mix both `{}` and `@` placeholders but it is recommended to use only one style for consistency.\n\n#### Available placeholders\n\n- any (if you need just any data)    \n- integer    \n- decimal    \n- number     \n- name       \n- first_name \n- last_name  \n- text       \n- word       \n- paragraph  \n- uri        \n- url        \n- local_uri  \n- email      \n- date         \n- time         \n- month        \n- day          \n- timezone     \n- company      \n- license_plate\n- address\n- city\n- country\n- user_agent\n- password\n- user_name\n- file_path\n\n### Rasam decorators\n\nRasa relies too heavily on classes to define objects like actions, forms, etc. \nRasam aims to remove these Rasa boilerplates to make writing chatbots easier.\n\n#### @action decorator\n\nThe `@action` decorator converts function into an Action class. \nHere is an example of how we can write custom classes in Rasa:\n\n```python\nclass ActionHelloWorld(Action):\n\n    def name(self) -> Text:\n        return "action_hello_world"\n\n    def run(self, dispatcher: CollectingDispatcher,\n            tracker: Tracker,\n            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:\n\n        dispatcher.utter_message(text="Hello World!")\n\n        return []\n\n```\n\nThe above code can be simplified using Rasam\'s `@action` decorator.\n\n```python\nfrom rasam import action\n\n\n@action\ndef action_hello_world(\n    self: Action, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]\n) -> List[Dict[Text, Any]]:\n    dispatcher.utter_message(text="Hello World!")\n    return []\n```\n\n\n\n## Author\n\n- [Ronie Martinez](mailto:ronmarti18@gmail.com)\n',
    'author': 'Ronie Martinez',
    'author_email': 'ronmarti18@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/roniemartinez/rasam',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.9',
}


setup(**setup_kwargs)
