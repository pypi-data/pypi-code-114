# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tsukuru']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'tsukuru',
    'version': '0.0.1',
    'description': 'GUI Makefile creater',
    'long_description': '# What\'s "tsukuru"?\n"tsukuru" is simple GUI Makefile creator.  \n"tsukuru" can provide simple way to create Makefile from GUI.   \n"Tsukuru" means "Make" in Japanense.  \n\nNowadays, many IDEs provides smart way to build systems.  \nBut in C/C++ language, we sometimes have to make Makefile or CMkaeLists.txt.  \nThese tools has long history and wonderful functions,  \nand helps building from one source code to very very large projects.  \n\n"tsukuru" aim is to private simple way to build C/C++ in provate project or small teams.  \nIn this situation,  If no skillfull Makefile user, someone needs to learn about Makefile.  \nAnd in a few month, his/her knowledge about Makefile goes away...  \n\nI would like to contribute these situation by providing simple GUI Makefile creator.  \nThis tools does not support deep and wide function, \nbut provide creating certain Makefile.   \n\n# Usage\n\n## Lisence\nLisence is MIT lisence\n\n## Contact\nIf you have any question, please use Github issue.',
    'author': 'Yohei Osawa',
    'author_email': 'yohei.osawa.318.niko8@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/senrust/tsukuru',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
