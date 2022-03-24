# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pjsekai_background_gen_pillow']

package_data = \
{'': ['*'], 'pjsekai_background_gen_pillow': ['assets/*']}

install_requires = \
['Pillow>=9.0.1,<10.0.0']

setup_kwargs = {
    'name': 'pjsekai-background-gen-pillow',
    'version': '0.2.0',
    'description': 'Generates PJSekai backgrounds with Pillow',
    'long_description': '# pjsekai_background_gen_pillow\n[![Python Versions](https://img.shields.io/pypi/v/pjsekai_background_gen_pillow.svg)](https://pypi.org/project/pjsekai_background_gen_pillow/)\n\nGenerates PJSekai background image from Image.\n\n## Installation\n\n```\npip install pjsekai_background_gen_pillow\n```\n\n## Example\n\n```python\nfrom PIL import Image\nimport pjsekai_background_gen_pillow as pjbg\n\ngenerator = pjbg.Generator()\ngenerator.generate(Image.open("path/to/image.png")).save("path/to/output.png")\n```\n\n## API\n\n### `Generator`\n\nGenerater for background images.\n\n##### Parameters\n\nbase : PIL.Image\n\n> Base background image.\n> Defaults to Built-in background image.\n\n#### `.generate(image)`\n\nGenerate background image from source image.\n\n##### Parameters\n\nsource : PIL.Image\n\n> Source image.\n\n##### Returns\n\nPIL.Image\n\n## License\n\nThis library is licensed under GPLv3. `test.png` is licensed under CC-BY-SA 4.0.',
    'author': 'sevenc-nanashi',
    'author_email': 'sevenc-nanashi@sevenbot.jp',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sevenc-nanashi/pjsekai_background_gen_pillow',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
