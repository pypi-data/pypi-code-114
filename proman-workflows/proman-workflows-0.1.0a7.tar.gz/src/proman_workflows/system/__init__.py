# -*- coding: utf-8 -*-
# copyright: (c) 2020 by Jesse Johnson.
# license: Apache 2.0, see LICENSE for more details.
"""Quality Assurance Task-Runner."""

import logging

from ..collection import Collection

logging.getLogger(__name__).addHandler(logging.NullHandler())

# Assemble collections for namespace
namespace = Collection(
    configuration={
        'plugins': [
            # {
            #     'name': 'deploy',
            #     'driver_name': 'ansible',
            #     'driver_namespace': 'proman.workflows.infra',
            # },
            {
                'name': 'system-test',
                'driver_name': 'test-infra',
                'driver_namespace': 'proman.workflows.system',
            },
        ]
    }
)

__all__ = ['namespace']
