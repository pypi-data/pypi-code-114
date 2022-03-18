# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fasteve',
 'fasteve.core',
 'fasteve.endpoints',
 'fasteve.io',
 'fasteve.io.mongo',
 'fasteve.io.sql',
 'fasteve.methods',
 'fasteve.middleware']

package_data = \
{'': ['*']}

install_requires = \
['email-validator==1.1.1',
 'fastapi>=0.70.1,<0.71.0',
 'motor>=2.5.1,<3.0.0',
 'sqlmodel>=0.0.6,<0.0.7',
 'uvicorn>=0.16.0,<0.17.0']

setup_kwargs = {
    'name': 'fasteve',
    'version': '0.2.0',
    'description': 'A simple and feature complete REST API framework designed for speed',
    'long_description': '![fasteve logo](https://i.ibb.co/Czrk2L9/fasteve-logo.png)\n\n[![PyPi](https://img.shields.io/pypi/v/fasteve.svg)](https://pypi.org/project/fasteve/)\n[![testing](https://github.com/Wytamma/fasteve/actions/workflows/testing.yml/badge.svg)](https://github.com/Wytamma/fasteve/actions/workflows/testing.yml)\n[![coverage](https://codecov.io/gh/Wytamma/fasteve/branch/master/graph/badge.svg)](https://codecov.io/gh/Wytamma/fasteve)\n[![image](https://img.shields.io/github/license/wytamma/fasteve.svg)](https://github.com/Wytamma/fasteve/blob/master/LICENSE)\n[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://img.shields.io/badge/code%20style-black-000000.svg)\n\nFasteve is a rebuild of [Eve](https://github.com/pyeve/eve) using [FastAPI](https://github.com/tiangolo/fastapi) as a base.\n\nFasteve is Simple\n-------------\n\nCreate a file `main.py` with:\n```python\nfrom fasteve import Fasteve, MongoModel, Resource\n\nclass People(MongoModel):\n    name: str\n\npeople = Resource(model=People)\nresources = [people]\n\napp = Fasteve(resources=resources)\n```\n\nStart a database ([mongodb default](https://hub.docker.com/_/mongo)):\n```console\n$ docker run --rm -p 27017:27017 mongo\n```\n\nRun the server with:\n```console\n$ uvicorn main:app --reload\n```\n\nThe API is now live, ready to be consumed:\n\n```console\n$ curl -i http://localhost:8000/people\nHTTP/1.1 200\n...\n{\n    "_data": [],\n    "_meta": {"max_results": 25, "total": 0, "page": 1},\n    "_links": {\n        "self": {"href": "/people", "title": "people"},\n        "parent": {"href": "/", "title": "home"},\n    },\n}\n```\n\nFeatures (TODO)\n---------------\n* Powered by FastAPI ✅\n* Emphasis on REST ✅\n* Full range of CRUD operations ✅\n* Customizable resource endpoints ✅\n* Sub Resources ✅\n* Pagination ✅\n* HATEOAS ✅\n* Bulk create ✅\n* Data Validation ✅\n* Extensible Data Validation ✅\n* Unique Fields ✅\n* CORS Cross-Origin Resource Sharing ✅\n* Read-only by default ✅\n* Default Values ✅\n* Embedded Resource Serialization ✅\n* Event Hooks ✅\n* Custom ID Fields ✅\n* Alternative ID Fields ✅\n* Interactive API docs (provided by Swagger UI) ✅\n* Alternative API docs (provided by ReDoc) ✅\n* Repeated Background Tasks ✅\n* MongoDB Support ✅\n* SQL Support ✅\n* Predefined Database Filters\n* Projections\n* JSONP\n* Customizable, multiple item endpoints\n* Filtering and Sorting\n* JSON and XML Rendering\n* Conditional Requests\n* Data Integrity and Concurrency Control\n* Resource-level Cache Control\n* API Versioning\n* Document Versioning\n* Authentication\n* Rate Limiting\n* File Storage\n* GeoJSON\n* Internal Resources\n* Enhanced Logging\n* Operations Log\n* MongoDB Aggregation Framework\n\n\nLicense\n-------\nFasteve is a open source project,\ndistributed under the `BSD license`\n\n\nLatest Changes\n-\n\n* :sparkles: add SQL support via sqlmodel. PR [#21](https://github.com/Wytamma/fasteve/pull/21) by [@Wytamma](https://github.com/Wytamma).\n* :tada: v0.1.3. PR [#20](https://github.com/Wytamma/fasteve/pull/20) by [@Wytamma](https://github.com/Wytamma).\n* :sparkles: Add event hooks. PR [#17](https://github.com/Wytamma/fasteve/pull/17) by [@Wytamma](https://github.com/Wytamma).\n* :sparkles: break up endpoints. PR [#16](https://github.com/Wytamma/fasteve/pull/16) by [@Wytamma](https://github.com/Wytamma).\n* :sparkles: Add PATCH method. PR [#15](https://github.com/Wytamma/fasteve/pull/15) by [@Wytamma](https://github.com/Wytamma).\n* :bug: PUT does upsert when ID not found. PR [#14](https://github.com/Wytamma/fasteve/pull/14) by [@Wytamma](https://github.com/Wytamma).\n* :art: PUT returns 204 (No Content). PR [#13](https://github.com/Wytamma/fasteve/pull/13) by [@Wytamma](https://github.com/Wytamma).\n* :sparkles: Add PUT method. PR [#12](https://github.com/Wytamma/fasteve/pull/12) by [@Wytamma](https://github.com/Wytamma).\n* :art: Formatting with Black. PR [#11](https://github.com/Wytamma/fasteve/pull/11) by [@Wytamma](https://github.com/Wytamma).\n',
    'author': 'Wytamma Wirth',
    'author_email': 'wytamma.wirth@me.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Wytamma/fasteve',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0',
}


setup(**setup_kwargs)
