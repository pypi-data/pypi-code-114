# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['paradigm_panes']

package_data = \
{'': ['*']}

install_requires = \
['hfst-optimized-lookup>=0.0.13,<0.1.0',
 'more-itertools>=8.7.0,<8.8.0',
 'pathlib',
 'requests',
 'typing-extensions>=3.7,<4.0']

setup_kwargs = {
    'name': 'paradigm-panes',
    'version': '0.2.1',
    'description': 'Paradigm panes meant to provide layout specification to be reused elsewhere.',
    'long_description': '# paradigm-panes\n\nInstallable package that produces a paradigm for a given word, given a pointer to paradigm layouts and FST file. Originally\nbuilt for [itwêwina](https://itwewina.altlab.app/).\n\n# Example Usage:\n\n```\n    import paradigm_panes\n    pg = paradigm_panes.PaneGenerator()\n\n    lemma = "amisk"\n    p_type = "NA"\n\n    pg.set_layouts_dir("/home/ubuntu/cmput401/paradigm-panes/paradigm_panes/resources/layouts")\n    pg.set_fst_filepath("/home/ubuntu/cmput401/paradigm-panes/paradigm_panes/resources/fst/generator-gt-norm.hfstol")\n\n    pg.generate_pane(lemma, p_type)\n```\n\n- `set_layouts_dir(path)` specifies a location of a directory with paradigm layouts that are relevant for current paradigm generation.\n\n- `set_fst_filepath(path)` specifies FST file location with layout translation that are relevant for current paradigm generation.\n\n- `set_tag_style(path)` specifies template rendering type.\n\n> Available tag styles:\n>\n> 1.  "Plus"\n> 2.  "Bracket"\n\nThe generator must specify both location before generating a paradigm.\n\nSize is optional to paradigm generation; by default a base size (or first available) will be used.\n',
    'author': 'Uladzimir Bondarau',
    'author_email': 'bondarau@ualberta.ca',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/UAlbertaALTLab/paradigm-panes',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
