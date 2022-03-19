# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ibson', 'ibson.tool']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'ibson',
    'version': '0.0.3',
    'description': 'BSON parsing library and tool.',
    'long_description': '# ibson\n\nBSON (Binary JSON) parsing library.\n\n## Usage\n\nThis library is designed to implement a basic BSON library with an interface\nthat is similar to python\'s native JSON parsing library. In particular, this\nhas expected usage:\n```python\nimport ibson\n\n\nobj = {\n    "a": {\n        "b": [1, 2, 3],\n        "uuid": uuid.uuid1()\n    }\n}\n\nbuffer = ibson.dumps(obj)\nnew_obj = ibson.loads(buffer)\n\n# Evaluates as \'True\'\nnew_obj == obj\n```\n\nThis mimics the existing `bson` library for python, but also permits reading\nfrom and writing to (seekable) streams and files as well:\n```python\n\nwith open(\'file.bson\', \'wb\') as stm:\n    ibson.dump(obj, stm)\n\n# Elsewhere\nwith open(\'file.bson\', \'rb\') as stm:\n    new_obj = ibson.load(stm)\n\n# Should evaluate True\nnew_obj == obj\n```\nNOTE: It is important that the file is opened in binary mode, not text mode!\n\nUnder the hood, this library is designed in a similar manner as a SAX-style\nevent-driven parser; it avoids explicit recursion wherever possible and has\ncalls that permit iterating over the contents using generators with an\ninterface that can even permit skipping keys/fields altogether. Since the\nparsing stack is maintained separately, it can also be used to verify and\nattempt to fix some issues.\n\n## How It Works\n\nThis library works by noting that the byte offset needed in a few places to\n(de)serialize BSON is already implicitly tracked in seekable streams via the\ncall to: `fp.tell()`, omitting the need to track the byte counts directly.\nIn places where these byte counts are not directly accessible, the caller is\nlikely already loading the content into a bytearray or binary stream that can\nbecome seekable anyway. When this field is needed before the value is actually\navailable (i.e. the `length` of a document before the document is written),\nthis simply registers the position the length needs to be written, writes out\na placeholder value (0), then retroactively writes out these lengths when they\nfinally are known, hence the need for the writable stream to also be seekable.\n(As a slight optimization, these lengths are sorted and written from the start\nto the end of the file again when the encoder is done to effectively make to\nsequential passes instead of an arbitrary number of random-access passes.)\n\nThis library also strives to reduce memory-consumption as best as reasonable\nwith an iterative parser, intentionally avoiding recursion where possible; the\nparser tracks the stack on the heap and also stores various fields internally\nso as to avoid loading everything parsed into memory when just traversing the\ndocument, in a manner analogous to SAX-style parsers for XML. (When decoding\nand storing the document as a python `dict`, yes, that will be in memory.)\n',
    'author': 'Aaron Gibson',
    'author_email': 'eulersidcrisis@yahoo.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/eulersIDcrisis/ibson',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
