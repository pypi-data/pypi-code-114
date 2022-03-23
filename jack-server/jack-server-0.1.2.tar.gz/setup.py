# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['jack_server']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'jack-server',
    'version': '0.1.2',
    'description': 'Control JACK server with Python',
    'long_description': '[![Test](https://github.com/vrslev/jack_server/actions/workflows/test.yml/badge.svg)](https://github.com/vrslev/jack_server/actions/workflows/test.yml)\n\nControl [JACK](https://jackaudio.org/) audio server with Python.\nCan be used as replacement for [jackd](https://manpages.debian.org/buster/jackd2/jackd.1.en.html) for more robust configuration, for example, when using [`jack`](https://github.com/spatialaudio/jackclient-python) package.\n\n## Installation\n\n`pip install jack_server`\n\nAlso you need to have `jackserver` library on your machine, it comes with [JACK2](https://github.com/jackaudio/jack2). I had problems with apt-package on Ubuntu (`jackd2`), if you do too, compile jack yourself.\n\n## Usage\n\n### 🎛 `jack_server.Server`\n\nOn server creation you _can_ specify some parameters:\n\n```python\nimport jack_server\n\nserver = jack_server.Server(\n    name="myfancyserver",\n    sync=True,\n    realtime=False,\n    driver="coreaudio",\n    device="BuiltInSpeakerDevice",\n    rate=48000,\n    period=1024,\n)\nserver.start()\n\ninput()\n```\n\nThey are actually an equivalent of `jackd` flags:\n\n- `-n`, `--name` to `name`,\n- `-S`, `--sync` to `sync`,\n- `-R`, `--realtime`, `-r`, `--no-realtime` to `realtime`,\n- `-d` to `driver`,\n\nAnd driver arguments:\n\n- `-d`, `--device` to `device`,\n- `-r`, `--rate` to `rate`,\n- `-p`, `--period` to `period`,\n\n#### `start(self) -> None`\n\n_Open_ and _start_ the server. All state controlling methods are idempotent.\n\n#### `stop(self) -> None`\n\nStop and close server.\n\n#### `driver: jack_server.Driver`\n\nSelected driver.\n\n#### `name: str`\n\nActual server name. It is property that calls C code, so you can actually set the name.\n\n#### `sync: bool`\n\nWhether JACK runs in sync mode. Useful when you`re trying to send and receive multichannel audio.\n\n#### `realtime: bool`\n\nWhether JACK should start in realtime mode.\n\n#### `params: dict[str, jack_server.Parameter]`\n\nServer parameters mapped by name.\n\n### 💼 `jack_server.Driver`\n\nDriver (JACK backend), can be safely changed before server is started. Not supposed to be created by user code.\n\n#### `name: str`\n\nDriver name, read-only.\n\n#### `device: str`\n\nSelected device.\n\n#### `rate: jack_server.SampleRate`\n\nSampling rate.\n\n#### `period: int`\n\nBuffer size.\n\n#### `params: dict[str, jack_server.Parameter]`\n\nDriver parameters mapped by name.\n\n### 📻 `jack_server.SampleRate`\n\nValid sampling rate, `44100` or `48000`.\n\n### 🔻 `jack_server.Parameter`\n\nNot supposed to be created by user code.\n\n#### `name: str`\n\nRead-only verbose name of parameter.\n\n#### `value: int | str | bytes | bool`\n\nValue of the parameter, can be changed.\n\n### ❗️ `jack_server.set_info_function(callback: Callable[[str], None] | None) -> None`\n\nSet info output handler. By default JACK does is itself, i. e. output is being printed in stdout.\n\n### ‼️ `jack_server.set_error_function(callback: Callable[[str], None] | None) -> None`\n\nSet error output handler. By default JACK does is itself, i. e. output is being printed in stderr.\n',
    'author': 'Lev Vereshchagin',
    'author_email': 'mail@vrslev.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
