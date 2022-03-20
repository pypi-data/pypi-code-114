# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mclogger']

package_data = \
{'': ['*']}

install_requires = \
['colorama>=0.4.4,<0.5.0', 'coloredlogs>=15.0,<16.0', 'tailer>=0.4.1,<0.5.0']

entry_points = \
{'console_scripts': ['mclogger = mclogger.__main__:main']}

setup_kwargs = {
    'name': 'mclogger',
    'version': '0.1.1',
    'description': 'MCLogger that shows log records on screen in color and in a log file',
    'long_description': "# MCLogger: Multi color logger to log to screen and file\n\n\n\n## MCLogger to log to file AND screen\n\n### What problem does this solve?\nA challenge for web-server applications (e.g. such as Flask) is to decipher what's going on from a long logging window.  The standard loggers are all single color console test which you have to trawl through manually one by one.\n\nMCLogger helps to solve this by colorising the debug, info, warning, into different colors so that it is much easier to read.  The logger will output to both on screen and also a file\n\n### How does it do this?\nMCLogger builds on the logging library and adds console color libraries to add colors to debug, info, error, warning entries\n\nDEBUG - blue\nWARNING - yellow\nERROR - red\nINFO - cyan\n\n### How to use the logger?\nThe logger is super easy to use.  You need to simply create an instance and add a file/filepath for the logfile\n\n```\nimport multi\n",
    'author': 'Pubs Abayasiri',
    'author_email': 'pubudu.abayasiri@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pubs12/mlogger',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3,<4',
}


setup(**setup_kwargs)
