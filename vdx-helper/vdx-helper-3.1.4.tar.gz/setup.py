# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vdx_helper']

package_data = \
{'': ['*']}

install_requires = \
['nndict==1.0.0', 'requests==2.22.0']

setup_kwargs = {
    'name': 'vdx-helper',
    'version': '3.1.4',
    'description': 'Python client library to connect to the VDX Core API',
    'long_description': "# VDX Helper\nThis repository provides a wrapper for every call made to VDX Core Api.\n\n## How it works\nThis helper first needs to be authorized by wielding valid token from Keycloak, then use that token for further requests as long as it has not expired.\n\nEach method also allows one to include their own custom mappers, enabling the method to return the result in the format the user wishes.\n![workflow illustration](docs/images/vdx-helper.png)\n\n## Prerequisites\n\n- Python Poetry\n- Docker + Docker-compose\n\n## Usage\n\n### Initialization\n\nRequired parameters: \n- api_url: The url leading to Core API server\n- auth_url: The url leading to authentication server\n- client_secret: The authentication secret\n- client_id: The ID of the client / partner\n\n\n```\nvdx_helper = VDXHelper(api_url='https://vizidox-core-api.com', auth_url='https://auth.com', client_secret=secret, client_id=client_id)\n```\n\n### Mapper example\nA mapper will receive a json-formatted parameter as their input. The following example mapper will add a field\n\n```\ndef example_mapper(json_file):\n    returned_json = copy.deepcopy(json_file)\n    returned_json['additional_field'] = 'additional_value'\n    return returned_json\n```\n\n### Usage example\n\n```\nvdx_helper.upload_file(file=the_file_to_upload, mapper=example_mapper)\n```\n\n## Running the tests\n\nYou can run the tests with poetry if you like. You can also obtain the code coverage.\n\n```\npoetry run pytest --cov=vdx_helper\n```\n\n### Run the test locally with docker-compose step-by-step\n1. Turn up the docker-containers\n```\ndocker-compose up -d\n```\n\n2. Run the tests via the vdx-helper docker container\n```\ndocker-compose run vdx-helper pytest tests\n```\n\n\n## Documentation\n\nTo build the documentation locally:\n\n```shell\ncd docs\nmake html\n```\n\nThe build files can be found in docs/build. Open the generated index.html file in the html folder, and you can now \nnavigate the documentation. Repeat the above command and refresh your browser every time you update the documentation.\nAll source files are in docs/source, with vdx_helper containing the documentation generated from docstrings.\n \n## Authors\n\n* **Tiago Santos** - *Initial work* - [Vizidox](https://vizidox.com)\n* **Joana Teixeira** - *Corrections and improvements* - [Vizidox](https://vizidox.com)\n* **Rita Mariquitos** - *Corrections and improvements* - [Vizidox](https://vizidox.com)\n\n## License\n\nAll of the code developed in this project belongs to Vizidox Solutions Limited under the ownership of Freddy Elturk and \nany distribution or use must be authorized and agreed upon previously.\n",
    'author': 'Joana Teixeira',
    'author_email': 'joana.teixeira@vizidox.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://vizidox.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
