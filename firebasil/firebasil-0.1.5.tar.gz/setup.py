# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['firebasil', 'firebasil.auth', 'firebasil.sse']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp-sse-client>=0.2.1,<0.3.0',
 'aiohttp>=3.8.1,<4.0.0',
 'dateparser>=1.1.0,<2.0.0',
 'stringcase>=1.2.0,<2.0.0',
 'typing-extensions>=4.1.1,<5.0.0']

setup_kwargs = {
    'name': 'firebasil',
    'version': '0.1.5',
    'description': 'A modern async Firebase library',
    'long_description': '# firebasil\n\n[![CI](https://github.com/k2bd/firebasil/actions/workflows/ci.yml/badge.svg)](https://github.com/k2bd/firebasil/actions/workflows/ci.yml)\n[![codecov](https://codecov.io/gh/k2bd/firebasil/branch/main/graph/badge.svg?token=0X48PIN0MC)](https://codecov.io/gh/k2bd/firebasil)\n[![PyPI](https://img.shields.io/pypi/v/firebasil)](https://pypi.org/project/firebasil/)\n[![Documentation Status](https://readthedocs.org/projects/firebasil/badge/?version=latest)](https://firebasil.readthedocs.io/en/latest/?badge=latest)\n\nA modern async Firebase client.\n\n# Features\n\n## Auth\n\n[![Auth Baseline](https://img.shields.io/github/milestones/progress/k2bd/firebasil/1)](https://github.com/k2bd/firebasil/milestone/1)\n[![Auth High level](https://img.shields.io/github/milestones/progress/k2bd/firebasil/6)](https://github.com/k2bd/firebasil/milestone/6)\n\nThe `AuthClient` async context manager provides access to auth routines.\nEvery method returns a typed object with the information provided by the Firebase auth REST API.\n\n```python\nfrom firebasil.auth import AuthClient\n\n\nasync with AuthClient(api_key=...) as auth_client:\n    # Sign up a new user\n    signed_up = await auth_client.sign_up("kevin@k2bd.dev", "password1")\n\n    # Sign in as a user\n    signed_in = await auth_client.sign_in_with_password(\n        email="kevin@k2bd.dev",\n        password="password1",\n    )\n\n    updated = await auth_client.update_profile(\n        signed_in.id_token,\n        display_name="Kevin Duff",\n    )\n```\n\nThe `AuthClient` class will use production GCP endpoints and routes for auth by default, unless the `FIREBASE_AUTH_EMULATOR_HOST` environment variable is set, in which case the defaults change to the emulator. This can be overridden in both cases by passing in `identity_toolkit_url`, `secure_token_url`, and `use_emulator_routes` explicitly.\n\n## Realtime Database (RTDB)\n\n[![RTDB Baseline](https://img.shields.io/github/milestones/progress/k2bd/firebasil/2)](https://github.com/k2bd/firebasil/milestone/2)\n[![RTDB High level](https://img.shields.io/github/milestones/progress/k2bd/firebasil/5)](https://github.com/k2bd/firebasil/milestone/5)\n\nThe `Rtdb` async context manager yields the root node of the database.\n\n```python\nfrom firebasil.rtdb import Rtdb\n\n\nasync with Rtdb(database_url=...) as root_node:\n\n    # Set the database state from the root node\n    await rtdb_root.set({"scores": {"a": 5, "b": 4, "c": 3, "d": 2, "e": 1}})\n\n    # Build a child node that references the \'scores\' path\n    child_node: RtdbNode = rtdb_root / "scores"\n\n    # Get the value of the further \'c\' child\n    c_value = await (child_node / "c").get()\n    assert c_value == 3\n\n    # Query for the last two entries at that location, ordered by key\n    query_value = await child_node.order_by_key().limit_to_last(2).get()\n    assert query_value == {"d": 2, "e": 1}\n\n    # Watch a node for live changes\n    async with child_node.events() as event_queue:\n        event: RtdbEvent = await event_queue.get()\n        ...\n        # Somewhere, \'b\' gets set to 7\n        # RtdbEvent(event=EventType.put, path=\'/b\', data=7)\n```\n\nEither a user ID token, or a machine credential access token, can be provided `Rtdb` through the `id_token` or `access_token` arguments, which will be used to pass the database\'s auth.\n\nA local emulator URL may be passed to `Rtdb` to test against the Firebase Emulator Suite.\n\n## Firestore Database\n\n[![Firestore Baseline](https://img.shields.io/github/milestones/progress/k2bd/firebasil/3)](https://github.com/k2bd/firebasil/milestone/3)\n\nStill in planning!\n\n## Storage\n\n[![Storage Baseline](https://img.shields.io/github/milestones/progress/k2bd/firebasil/4)](https://github.com/k2bd/firebasil/milestone/4)\n\nStill in planning!\n\n# Developing on this Project\n\n## Installation\n\nInstall [Poetry](https://python-poetry.org/) and `poetry install` the project\n\nInstall the [Firebase CLI](https://firebase.google.com/docs/cli). Make sure the emulators are installed and configured with `firebase init emulators`.\n\n### Useful Commands\n\nNote: if Poetry is managing a virtual environment for you, you may need to use `poetry run poe` instead of `poe`\n\n- `poe autoformat` - Autoformat code\n- `poe lint` - Linting\n- `poe test` - Run tests\n- `poe docs` - Build docs\n\n### Release\n\nRelease a new version by manually running the release action on GitHub with a \'major\', \'minor\', or \'patch\' version bump selected.\nThis will create an push a new semver tag of the format `v1.2.3`.\n\nPushing this tag will trigger an action to release a new version of your library to PyPI.\n\nOptionally create a release from this new tag to let users know what changed.\n',
    'author': 'Kevin Duff',
    'author_email': 'kevinkelduff@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/k2bd/firebasil',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
