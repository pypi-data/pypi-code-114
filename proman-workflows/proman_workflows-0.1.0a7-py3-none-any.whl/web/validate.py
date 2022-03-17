# -*- coding: utf-8 -*-
# copyright: (c) 2020 by Jesse Johnson.
# license: Apache 2.0, see LICENSE for more details.
"""Validation Task-Runner."""

# import os
# import re

from cerberus import Validator
from invoke import Context, task

# path_check = re.compile('[a-zA-Z0-9_-/.]+')


@task
def check(ctx, path='static && echo unsafe'):  # type: (Context, str) -> None
    """Check to develop cerberus."""
    schema = {'path': {'type': 'string', 'regex': '^$'}}
    v = Validator(schema)
    print(v.validate({'path': path}))
    ctx.run(f"ls {path}")
