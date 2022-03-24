# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_firebase']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>0.60.0',
 'firebase-admin>=5.2.0,<6.0.0',
 'python-multipart>=0.0.5,<0.0.6']

setup_kwargs = {
    'name': 'fastapi-firebase',
    'version': '0.2.3',
    'description': 'FastAPI integration with firebase',
    'long_description': '# FastAPI Firebase integration\n\nThis package contains some utilities to work with firebase in a FastAPI project.\n\n## Example usage\n\nFor example, if you want to send the firebase app name:\n\n```python\nfrom fastapi import FastAPI, Depends\nfrom fastapi_firebase import setup_firebase, firebase_app\nfrom firebase_admin.app import App\n\napp=FastAPI()\n\nsetup_firebase(app)\n\n@app.get("/appname")\ndef get_appname(fb_app: App = Depends(firebase_app)):\n    return fb_app.name\n\n```\n\nSee the `setup_firebase` documentation for how to initialize.\n',
    'author': 'Francisco Del Roio',
    'author_email': 'francipvb@hotmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
