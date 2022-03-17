# -*- coding: utf-8 -*-
# copyright: (c) 2021 by Jesse Johnson.
# license: MPL-2.0, see LICENSE for more details.
"""Convenience tools to manage drivers."""

import logging
from typing import Any, Optional

from invoke import Runner  # Executor

logging.getLogger(__name__).addHandler(logging.NullHandler())


class Exec(Runner):
    """Provide Invoke integration with Stevedore."""

    def __init__(self, start: Optional[str] = None, **kwargs: Any) -> None:
        """Initialize collection."""
        self.plugins = kwargs['config']['plugins']
        super().__init__(**kwargs)
        self.config = kwargs.pop('config', {})
        if start is None:
            start = self.config.tasks.search_root
        self._start = start
        # namespace=kwargs.pop('driver_namespace'),
        # name=kwargs.pop('driver_name', name),
        # **kwargs,
