# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pysdrweb', 'pysdrweb.data', 'pysdrweb.fmserver', 'pysdrweb.util']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'SoundFile>=0.10.3,<0.11.0',
 'click>=8.0.4,<9.0.0',
 'lameenc==1.3.0',
 'tornado>=6.1,<7.0']

entry_points = \
{'console_scripts': ['sdrfm_server = '
                     'pysdrweb.fmserver.server:fm_server_command']}

setup_kwargs = {
    'name': 'pysdrweb',
    'version': '0.3.2',
    'description': 'Server to host FM Radio via RTL-SDR utilities.',
    'long_description': '# pysdrweb\n\nProject to create a web interface to RTL-SDR tooling.\n\n## FM Radio Receiver\n\nThe first focus of the project is to make a simple, web-based\nFM Radio receiver that can be controlled entirely through a\nweb browser. By visiting the main page, the user can listen in\non an (FM) radio station using any compatible RTL-SDR dongle\nand change the frequency, as desired.\n\nThis receiver is backed by some _driver_, which implements the\nset of calls necessary to run the radio, i.e. calls to generate\na raw PCM data stream that is then encoded on the fly. Usually,\nthis driver is simply the RTL-SDR program: `rtl_fm`, which the\nserver searches for by default.\n(Other driver types are planned for the future, but are not yet\nimplemented.)\n\nBy default, python supports some (usually uncompressed) formats\nout of the box:\n - WAV: Raw format used in CDs and other media.\n - AIFF: Another format used in places. Can potentially\n        support compression.\n\nIf `soundfile` is also present (and installed correctly), then\nthis can also encode into more formats:\n - FLAC: Free Lossless Audio Codec, supported by most browsers\n       with some possible compression.\n - OGG: Container format, supported by browsers. This format\n       usually compresses fairly well, especially compared to\n       more raw formats.\n(The list isn\'t exhaustive, but the goal is to support more\nbrowsers, not as many formats. The code should be easy enough\nto add more formats, however, if that is ever really needed.)\n\nCurrently, this server appears to work on Firefox and Chrome,\nwhich support dynamically playing audio as it is downloaded.\nThe hope is to support Safari in the future, but this is not\nyet implemented.\n\n### Goal\n\nThe goal of this server is to support multiple formats and\nmultiple clients simultaneously, without straining _too_ many\nsystem resources; the hope is that this server is low-key\nenough to run on weaker hardware.\n\n## Running the Server\n\nCurrently, the server requires `rtl_fm` to be installed and\na valid RTL-SDR device to be plugged in.\n\nThe simplest way to run the server is:\n```sh\nsdrfm_server -p 8080 -f 107.3M\n```\nThis runs the server on port 8080 and listens (initially) on\n107.3 FM.\n\nIf `rtl_fm` is not on the path, that can be passed in with:\n```sh\nsdrfm_server -p 8080 -f 107.3M -m ${RTL_FM_PATH}\n```\n\nFor the full set of options, it is easier to configure the\nserver with a configuration file. A sample configuration file\nis shown below:\n```yaml\n#\n# Sample \'native\' driver configuration file.\n# \n---\nport: 9000\n# Uncomment to require auth to change the frequency.\n# auth:\n#   type: basic\n#   # This indicates whether \'readonly\' (GET) requests require auth or not.\n#   ignore_on_read: true\n#   # Each user is denoted by: <user>: <password>\n#   users:\n#     admin: admin\n\n# Starting (FM) channel/frequency to listen on startup.\ndefault_frequency: 107.3M\n# Driver settings.\ndriver:\n  # Path to rtl_fm, if not on the path of the server.\n  rtl_fm: /usr/local/bin/rtl_fm\n  # Optional.\n  kb_buffer_size: 128\n```\nThen, to run the server:\n```sh\nsdrfm_server -c config.yml\n```\nThis permits adding authentication as well.\n\n## Server REST API\n\nCurrently, the server supports a REST API that the main page\ninvokes to render. The main calls are described below:\n\n| Method | Route | Description |\n---------|-------|-------------|\n| GET | `/api/frequency` | Returns the current frequency the server is listening on. |\n| POST | `/api/frequency` | Change the frequency the server is listening on. |\n| GET | `/api/procinfo` | Returns any (stderr) logging for the current driver. |\n| GET | `/api/radio/audio.<ext>` | Fetch the audio streamed from the radio. |\n\n### Audio Route (More Detail)\n\nMuch of this server relies on `/api/radio/audio.<ext>` to function since this\nis the route that actually serves the audio file. This route uses the given\n`<ext>` extension to determine the format to stream in. The route also accepts\nan optional `timeout` parameter, telling the server how long to listen for (in\nseconds). If not passed, the server will continue streaming indefinitely.\n\nTo download 10 seconds of the audio in WAV format (assuming the server is\nrunning locally on port 8080) call:\n```sh\ncurl http://localhost:8080/api/radio/audio.wav?timeout=10 > audio.wav\n```\n\nIf a format is not supported, the response will indicate as such.\n\n### Authentication\n\nBy default, the requests are not authenticated. If configured, however,\nthe requests can all require authentication using "HTTP Basic"-style\nauthentication. When making a request, the browser will prompt for the\nusername/password combination.\n\nOther authentication may be added later.\n\n## How It Works\n\nFor simplicity, the RTL-SDR tooling includes `rtl_fm`, which\nstreams FM audio data as raw, mono, 16-bit (2 byte) PCM data\nat some configurable frequency. For example, the following\nshell pipeline streams the frequency `107.3M` to an MP3 file:\n```sh\n# Listen on 107.3 FM, sampling at 48kHz\nrtl_fm -f 107.3M -M fm -s 48000 | \\\nsox -traw -r48000 -es -b16 -c1 -V1 - -tmp3 - > output.mp3\n```\nThe `sox` command is used to convert raw PCM data into framed\nMP3 data. (It is possible to use `ffmpeg` in a similar vain as\nwell). The quality is quite bad; we need to sample more quickly\nthen resample down to a lower frequency:\n```sh\n# Sample at 200k, then resample down to 48k.\n# Passing \'-A fast\' denotes the way to perform the resample.\nrtl_fm -f 107.3M -M fm -s 200k -r 48k -A fast | \\\nsox -traw -r48k -es -b16 -c1 -V1 - -tmp3 - > output.mp3\n```\nThis command can be run remotely and played (once) in the\nbrowser using:\n```sh\n# Like above, but pipes the output to port 8080.\nrtl_fm -f 107.3M -M fm -s 200k -r 48k -A fast | \\\nsox -traw -r48k -es -b16 -c1 -V1 - -tmp3 - | \\\nsocat -u - TCP-LISTEN:8080\n```\nThis pipeline is cool, but has some obvious problems. In\nparticular, the pipeline ends as soon as the browser stops\nlistening for any more input. Also, only one browser/client\ncan listen at a time. (Also, some browsers might not support\nthis for some formats...) Once finished, the command must be\nexecuted again.\nChanging the frequency also requires rerunning or otherwise\nchanging the command.\n\nTo address these issues, pysdrweb will buffer the PCM output\nfrom whatever source (currently `rtl_fm`) and encode it on\nthe fly, which permits _multiple clients and formats_. This\nalso permits changing the frequency more easily.\n',
    'author': 'Aaron Gibson',
    'author_email': 'eulersidcrisis@yahoo.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/eulersIDcrisis/pysdrweb',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4',
}


setup(**setup_kwargs)
