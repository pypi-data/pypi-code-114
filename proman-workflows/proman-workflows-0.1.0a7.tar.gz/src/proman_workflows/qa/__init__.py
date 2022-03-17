# -*- coding: utf-8 -*-
# copyright: (c) 2020 by Jesse Johnson.
# license: Apache 2.0, see LICENSE for more details.
"""Quality Assurance Task-Runner."""

import logging

from proman_workflows.collection import Collection

logging.getLogger(__name__).addHandler(logging.NullHandler())

# Assemble collections for namespace
namespace = Collection(
    configuration={
        'plugins': [
            {
                'name': 'unit-test',
                'driver_name': 'pytest',
                'driver_namespace': 'proman.workflows.qa',
            },
            {
                'name': 'acceptance-test',
                'driver_name': 'behave',
                'driver_namespace': 'proman.workflows.qa',
            },
        ]
    }
)

__all__ = ['namespace']
