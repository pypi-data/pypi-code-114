# -*- coding: utf-8 -*-
# copyright: (c) 2020 by Jesse Johnson.
# license: Apache 2.0, see LICENSE for more details.
"""Provide package task-runner.

All-in-one (python included)
- PyInstaller
- PyOxidizer

Bundled module and depdencies
- Pex
- Subpar
- Shiv
- ZipApp

"""

# import importlib

from invoke import Collection

namespace = Collection()
# namespace.configure({})
# namespace.load_collections(
#     plugins=[
#         {
#             'name': 'exec',
#             'driver_name': 'briefcase',
#             'driver_namespace': 'proman.workflows.executable',
#         }
#     ]
# )
