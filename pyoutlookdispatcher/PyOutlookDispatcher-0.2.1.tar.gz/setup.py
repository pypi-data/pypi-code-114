# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyoutlookdispatcher']

package_data = \
{'': ['*']}

install_requires = \
['pywin32>=303,<304']

setup_kwargs = {
    'name': 'pyoutlookdispatcher',
    'version': '0.2.1',
    'description': 'A Simple Email Dispatcher based on top of win32Api',
    'long_description': '# Outlook Email Dispatcher\n\n### A Simple Email Dispatcher based on top of win32Api\n\n## Installation\n\n```\npip install pyoutlookdispatcher\n```\n\n## Examples of Usage: \n\n### Send Email with Attachments\n\nBy default it adds your signature if you have one.\n\n```\nimport os\nfrom pyoutlookdispatcher import Outlook, Mail\n\nFILES_TO_ATTACH_FOLDER = os.path.join(os.getcwd(), \'files_to_attach\')\nATTACHMENTS = [os.path.join(FILES_TO_ATTACH_FOLDER, f) for f in os.listdir(FILES_TO_ATTACH_FOLDER)]\n\nmail = Mail(\n    Subject="Teste",\n    To="example@example.com",\n    HTMLBody="Teste",\n    CC="example@example.com",\n    Attachments=ATTACHMENTS\n)\n\noutlook = Outlook()\noutlook.send(mail)\n```\n\n### Send Email without Signature\n\n```\nfrom pyoutlookdispatcher import Outlook, Mail\n\nmail = Mail(\n    Subject="Teste",\n    To="example@example.com",\n    HTMLBody="Teste",\n    CC="example@example.com",\n    Attachments=ATTACHMENTS,\n    Signature=False\n)\n\noutlook = Outlook()\noutlook.send(mail)\n```\n\n### Preview an Email\n\n```\nfrom pyoutlookdispatcher import Outlook, Mail\n\nmail = Mail(\n    Subject="Teste",\n    To="example@example.com",\n    HTMLBody="Teste",\n    CC="example@example.com",\n    Attachments=ATTACHMENTS,\n)\n\noutlook = Outlook()\noutlook.preview(mail)\n```\n\n## Object Mail Params:\n```\nSubject: str\nTo: str\nHTMLBody: str\nCC: Optional[str] = None\nAttachments: Optional[List[str]] = field(default_factory=list)\nSignature: Optional[bool] = True\n```\n\n## Short Use Cases:\n\n### Initialize Outlook\n\nInstanciate an Object from Outlook Class\n\n```\noutlook = Outlook()\n```\n\n### Preview Mail:\n```\noutlook.preview(mail)\n```\n\n### Send Mail:\n```\noutlook.send(mail)\n```\n\n\n',
    'author': 'Rafael Tedesco',
    'author_email': 'dev.rafaeltedesco@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
