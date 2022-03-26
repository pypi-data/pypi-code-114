# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['convert_videos']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0',
 'colorama>=0.4.0,<0.5.0',
 'ffmpy>=0.2.2,<0.3.0',
 'prettytable>=0.7.2,<0.8.0',
 'stringcase>=1.2.0,<2.0.0',
 'video_utils>=2.2.0,<3.0.0']

entry_points = \
{'console_scripts': ['convert-videos = convert_videos.cli:main']}

setup_kwargs = {
    'name': 'convert-videos',
    'version': '2.7.4',
    'description': 'This tool allows bulk conversion of videos using ffmpeg',
    'long_description': '# Convert Videos\n\n![Test Status](https://github.com/justin8/convert_videos/workflows/Workflow/badge.svg?branch=master)\n[![codecov](https://codecov.io/gh/justin8/convert_videos/branch/master/graph/badge.svg)](https://codecov.io/gh/justin8/convert_videos)\n\nThis tool allows bulk conversion of videos using ffmpeg.\n\nBy default it will append the codec name to the file, e.g. `Best Movie Ever.avi` -> `Best Movie Ever - x265.mkv`. This can be optionally overridden using the `--in-place` flag.\n\nVideos are only converted if they do not already match the desired codec, allowing you to process a folder of mixed format files and only convert the ones you desire. This can optionally be overridden.\n\n## File output\n\n### Container\n\nThe default output container is `mkv` format. This can be changed with the `--container` flag to anything that is supported by FFMPEG and the chosen video and audio codecs\n\n## Video output\n\n### Codecs\n\nCurrently only HEVC (x265) and AVC (h264) are supported for video codecs.\n\n### Resizing\n\nVideos can be resized automatically by providing a width. Height is automatically calculated to ensure that the aspect ratio is maintained.\n\n### Hardware Acceleration\n\nHardware acceleration is supported on nVidia devices. Caveats:\n\n- Conversions use constqp mode for the quality setting instead of CRF, this is because nvenc does not support CRF\n- b-frames are not currently supported; nvenc itself supports them on 20xx+ series graphics cards.\n\nDefault settings:\nAudio: 160kbps 2 channel AAC\nVideo: HEVC/x265 at quality of 23\n\n## Subtitles\n\nAll subtitles will be copied from the source if they exist\n\n## Usage\n\n```\nUsage: convert-videos [OPTIONS] DIRECTORIES...\n\nOptions:\n  -i, --in-place            Replace the original files instead of appending\n                            the new codec name\n\n  -f, --force               Force conversion even if the format of the file\n                            already matches the desired format\n\n  --video-codec TEXT        A target video codec. Supported codecs: HEVC, AVC\n                            [default: HEVC]\n\n  -q, --quality INTEGER     The quantizer quality level to use  [default: 23]\n  -p, --preset TEXT         FFmpeg preset to use.  [default: medium]\n  -w, --width INTEGER       Specify a new width to enable resizing of the\n                            video\n\n  --extra-input-args TEXT   Specify any extra arguments you would like to pass\n                            to FFMpeg input here\n\n  --extra-output-args TEXT  Specify any extra arguments you would like to pass\n                            to FFMpeg output here\n\n  --audio-codec TEXT        A target audio codec  [default: AAC]\n  --audio-channels INTEGER  The number of channels to mux sound in to\n                            [default: 2]\n\n  --audio-bitrate INTEGER   The bitrate to use for the audio codec  [default:\n                            160]\n\n  --temp-dir TEXT           Specify a temporary directory to use during\n                            conversions instead of the system default\n\n  -v, --verbose             Enable verbose log output\n  --container TEXT          Specify a video container to convert the videos in\n                            to  [default: mkv]\n\n  --dry-run                 Do not make actual changes\n  --nvidia-hw-accel         Use Nvidia HW acceleration instead of software\n                            encoding\n\n  -h, --help                Show this message and exit.\n```\n',
    'author': 'Justin Dray',
    'author_email': 'justin@dray.be',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
