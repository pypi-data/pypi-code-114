# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['secrules_parsing', 'secrules_parsing.model']

package_data = \
{'': ['*']}

install_requires = \
['importlib-metadata>=4.11.3,<5.0.0', 'textX>=2.3.0,<3.0.0']

entry_points = \
{'console_scripts': ['secrules-parser = secrules_parsing.cli:run']}

setup_kwargs = {
    'name': 'secrules-parsing',
    'version': '0.2.1',
    'description': 'ModSecurity DSL Parser package using textX',
    'long_description': '# OWASP CRS Rules parser\n\nIncomplete parser model and sample application for parsing [Core Rule Set](https://github.com/coreruleset/coreruleset/) written in the ModSecurity DSL SecRule language. It uses the python library [textX](http://www.igordejanovic.net/textX/) for parsing.\n\n## How to use it (CLI):\n\n1. Install dependencies\n    Dependencies can be installed system-wide, or just for your user (using `--user`).\n\n    System-wide:\n    ```shell\n    sudo pip install -r requirements.txt\n    ```\n    User:\n    ```shell\n    pip install --user -r requirements.txt\n    ```\n2. Execute `secrules-parser` specifying the location of the files you want to scan using the -f/--files argument. This takes wildcards or individual files.\n   `$ secrules-parser -c -f /owasp-crs/rules/*.conf`\n\n3. Add flags to accomplish needed tasks:\n\n - -h, --help:\n    * *Description:* show the help message and exit\n    * *Example:* `$ secrules-parser -h`\n\n - -r, --regex:\n    * *Description:* Extract regular expressions from rules file\n    * *Example:*\n    ```shell\n    $ secrules-parser --regex /owasp-crs/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf\n    {"/owasp-crs/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf": [{"920100": ["^(?i:(?:[a-z]{3,10}\\\\s+(?:\\\\w{3,7}?://[\\\\w\\\\-\\\\./]*(?::\\\\d+)?)?/[^?#]*(?:\\\\?[^#\\\\s]*)?(?:#[\\\\S]*)?|connect (?:\\\\d{1,3}\\\\.){3}\\\\d{1,3}\\\\.?(?::\\\\d+)?|options \\\\*)\\\\s+[\\\\w\\\\./]+|get /[^?#]*(?:\\\\?[^#\\\\s]*)?(?:#[\\\\S]*)?)$"]}, {"920120": ["(?<!&(?:[aAoOuUyY]uml)|&(?:[aAeEiIoOuU]circ)|&(?:[eEiIoOuUyY]acute)|&(?:[aAeEiIoOuU]grave)|&(?:[cC]cedil)|&(?:[aAnNoO]tilde)|&(?:amp)|&(?:apos));|[\'\\\\\\"=]"]}, {"920160": ["^\\\\d+$"]}, {"920170": ["^(?:GET|HEAD)$"]}, {"920171": ["^(?:GET|HEAD)$"]}, {"920180": ["^POST$"]}, {"920190": ["(\\\\d+)\\\\-(\\\\d+)\\\\,"]}, {"920210": ["\\\\b(?:keep-alive|close),\\\\s?(?:keep-alive|close)\\\\b"]}, {"920220": ["\\\\%(?:(?!$|\\\\W)|[0-9a-fA-F]{2}|u[0-9a-fA-F]{4})"]}, {"920240": ["^(?:application\\\\/x-www-form-urlencoded|text\\\\/xml)(?:;(?:\\\\s?charset\\\\s?=\\\\s?[\\\\w\\\\d\\\\-]{1,18})?)??$"]}, {"920260": ["\\\\%u[fF]{2}[0-9a-fA-F]{2}"]}, {"920290": ["^$"]}, {"920310": ["^$"]}, {"920311": ["^$"]}, {"920330": ["^$"]}, {"920340": ["^0$"]}, {"920350": ["^[\\\\d.:]+$"]}, {"920420": ["^(?:GET|HEAD|PROPFIND|OPTIONS)$"]}, {"920440": ["\\\\.(.*)$"]}, {"920450": ["^.*$"]}, {"920200": ["^bytes=(?:(?:\\\\d+)?\\\\-(?:\\\\d+)?\\\\s*,?\\\\s*){6}"]}, {"920230": ["\\\\%((?!$|\\\\W)|[0-9a-fA-F]{2}|u[0-9a-fA-F]{4})"]}, {"920121": ["[\'\\\\\\";=]"]}, {"920460": ["(?<!\\\\Q\\\\\\\\\\\\E)\\\\Q\\\\\\\\\\\\E[cdeghijklmpqwxyz123456789]"]}]}\n    ```\n\n * -c, --correctness:\n    * *Description:* Check the validity of the syntax\n    * *Example:*\n    ```\n    $ secrules-parser -c -f /owasp-crs/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf\n    Syntax OK: ../../../rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf\n    ```\n\n * -v, --verbose\n    * *Description:* Print verbose messages\n    * *Example:*\n    ```\n    $ secrules-parser -c -v -f /owasp-crs/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf\n    ...\n    ```\n\n * -o FILE, --output FILE\n    * *Description:* Output results to file\n    * *Example:*\n    ```\n    $ secrules-parser -c -o out.json -f /owasp-crs/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf    \n    ```\n\n * --output-type github | plain\n    * *Description:* Desired output format. Useful if running from Github Actions and you want annotated output\n    * *Example:*\n    ```\n    $ secrules-parser -c --output-type github -f /owasp-crs/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf\n    ```\n\n## How to use it (API):\n\n### process_rules(list files)\nTakes a list of file path\'s and returns models\n```python\nimport glob\nimport os\nfrom secrules_parsing import parser\n\n# Extract all of our pathing\nfiles = glob.glob("../../rules/*.conf")\n# Pass absolute paths because of module location\nfiles = [os.path.abspath(path) for path in files]\nmodels = parser.process_rules(files)\n```\n\n### get_correctness(list files, list models)\n```python\nimport glob\nimport os\nfrom secrules_parsing import parser\n\n# Extract all of our pathing\nfiles = glob.glob("../../rules/*.conf")\n# Pass absolute paths because of module location\nfiles = [os.path.abspath(path) for path in files]\nmodels = parser.process_rules(files)\nparser.get_correctness(files, models)\n```\n\n## Misc\n\nTo visualize the syntax tree, use:\n\n```\ntextx visualize secrules.tx\ndot -Tpng -O secrules.tx.dot\n```\n\nThen review the generated PNG modsec.tx.dot.png!\n\nPlease file an [issue](https://github.com/coreruleset/secrules_parsing/issues) if you find a bug or you want some feature added.\n',
    'author': 'Felipe Zipitria',
    'author_email': 'felipe.zipitria@owasp.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/coreruleset/secrules_parsing',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
