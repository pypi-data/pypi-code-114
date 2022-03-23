# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['playbacker', 'playbacker.app', 'playbacker.tracks']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML==6.0',
 'SoundFile==0.10.3-post1',
 'inquirer==2.9.1',
 'numpy==1.22.3',
 'pydantic==1.9.0',
 'sounddevice==0.4.4',
 'soxr==0.2.7',
 'textual-inputs==0.2.5',
 'textual==0.1.17',
 'typer==0.4.0',
 'uvloop==0.16.0']

entry_points = \
{'console_scripts': ['playbacker = playbacker.main:main']}

setup_kwargs = {
    'name': 'playbacker',
    'version': '0.0.1',
    'description': 'Live music performance playback',
    'long_description': '# Playbacker\n\n<img src="img/tui.png">\n\nTUI application for managing playback on live music performances (metronome, cues and backing tracks).\n\n## Rational\n\nUsually people use Ableton Live, Logic Pro or any other DAW for performances. I had issues with this kind of setup: too big, clumsy and require a lot of time.\nThere\'s [MultiTracks\' Playback](https://www.multitracks.com/products/playback/), but you have to pay a subscription to get important functionality. Also, it doesn\'t seem that robust.\n\n## Solution\n\nMake my own app! 😃\n\n- Works only on macOS (with minimal effort can be adapted for Linux or Windows)\n- Configurable channel map\n- Storage management based on simple yaml files\n- Fully customizable: can be used as library to make your own frontend, tracks or whatever\n\n## Installation\n\n```sh\npip install git+https://github.com/vrslev/playbacker\n```\n\nOr better of with pipx:\n\n```sh\npipx install git+https://github.com/vrslev/playbacker\n```\n\n## Usage\n\n- Setup configuration and storage files (example is in /example directory)\n- Run `playbacker`\n\n🧸❗️ This is a toy project! There\'s no release management, PyPI releases, etc for now.\n',
    'author': 'Lev Vereshchagin',
    'author_email': 'mail@vrslev.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
