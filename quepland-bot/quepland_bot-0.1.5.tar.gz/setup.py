# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['quepland_bot',
 'quepland_bot.application',
 'quepland_bot.application.exceptions',
 'quepland_bot.domain',
 'quepland_bot.domain.entities',
 'quepland_bot.domain.enums',
 'quepland_bot.domain.exceptions',
 'quepland_bot.domain.ports',
 'quepland_bot.domain.use_cases',
 'quepland_bot.domain.value_objects',
 'quepland_bot.infrastructure',
 'quepland_bot.infrastructure.adapters',
 'quepland_bot.infrastructure.adapters.pynput_click_recorder']

package_data = \
{'': ['*']}

install_requires = \
['PyAutoGUI>=0.9.53,<0.10.0', 'pynput>=1.7.6,<2.0.0']

setup_kwargs = {
    'name': 'quepland-bot',
    'version': '0.1.5',
    'description': 'Simple library to record and play mouse macros at regular intervals between clicks.',
    'long_description': 'A simple library for recording and playing mouse macros at regular intervals between clicks.\n\n# Compatibility\n\nBuilt and tested on Ubuntu 21.04. \n\nProbably works with other distributions as well as Windows and Mac.\n\n# Installation\n\n```\npip install quepland_bot\n```\n\n# Usage\nImport and instantiate QueplandBot\n\n```\nfrom quepland_bot import QueplandBot\n\n\nbot = QueplandBot()\n```\n\nRecord clicks: once the method is called, it will wait for a space bar press to begin recording.\nPress any kay to stop recording.\n```\nbot.record_clicks()\n```\n\nPlay what you recorded until any key is pressed:\n```\nbot.run()\n```\n\n\n## Changing intervals between clicks\n\nWhen instantiating QueplandBot you can define how many seconds it will take between clicks when playing a sequence.\nDefault is 0.1 seconds.\n\n```\nbot = Queplandbot(default_seconds_between_clicks=0.5)\n```\n\n## Saving routines\n\nYou can save a sequence of clicks by assigning the return of `record_clicks()` to a variable.\nTo play it, pass it as an argument to `run()`. \nWhen `run()` is called without arguments it runs last routine recorded.\n\n```\n\nbot = QueplandBot()\n\none_routine = bot.record_clicks()\nother_routine = bot.record_clicks()\n\nbot.run(one_routine)\n\n```',
    'author': 'Francisco Mascarenhas',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/francisco-mascarenhas/quepland_bot',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
