# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['messages_sender']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.0.3,<4.0.0', 'Telethon>=1.24.0,<2.0.0']

setup_kwargs = {
    'name': 'messages-sender',
    'version': '0.1.3',
    'description': 'Message sender is a library which create a message to send from a python dictionnary and a Jinja template and send it by the method of your choice.',
    'long_description': '# Messages Sender\n\n<p align="center">\n<a href="https://github.com/psf/black/blob/main/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>\n<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>\n</p>\n\n\nFormat and send a message following a template.\n\n## Description\nMessage sender is a library which create a message to send from a python dictionnary and a Jinja template and send it by [the method of your choice](##Send methods available).\n\n<img src=".doc/create_message.svg" alt="pipeline" style="zoom:60%;" />\n\n\n## Getting Started\n\n### Dependencies\n* python3.8+\n\n### Installing\n```bash\npip install messages-sender\n```\n\n### Use it\n\nexample:\n```python\nfrom messages-sender import MessageSender\ncredentials = {\n    "SMTP": {\n        "port": 465,\n        "password": "your_mail_password",\n        "sender_email": "your_mail",\n    },\n}\nmethod = "smtp"\ntemplate = "templates/mail_template.jinja"\nmessage = {\n    "subject": "Test",\n    "core": "The results of your analyse are available.",\n    "results": {"link": "https://github.com/Ermite28/messages_sender", "label": "See the result"},\n    "greetings": "Best regards,\\nBenoît de Witte",\n    "senders": {"info": "Ermite28, Belgium"},\n}\nMessageSender(credentials=credentials, method=method, template=template).send_message("your_email", message=message)\n\n```\n\n\n\n## TODO\n\n- [X] Maybe rethink about the library interface?\n- [ ] Make more example template\n- [X] Handle mails attached files.\n- [ ] Better error handling.\n- [X] Add unit test\n- [X] should it handle file (config, template, message)? NO\n\n## Send methods available\n\n:white_check_mark: Telegram\n\n:white_check_mark:  SMTP\n\n:red_circle: local\n\n:red_circle: Signal\n\n:red_circle: RSS\n\n:red_circle: SMS\n\n:red_circle: Discord bot\n\n:red_circle: message_senders API (futur project)\n\n\n## License\n\nThis project is licensed under the MIT License - see the LICENSE.md file for details\n',
    'author': 'Ermite28',
    'author_email': 'benoitdewitte28@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Ermite28/messages_sender',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
