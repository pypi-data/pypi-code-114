"""Module for partial aggregate providers.

These are optimizations to pre-aggregate some table columns up to certain levels.
One can choose the levels and the measures (among table aggregations) to build the provider on.
If a step of a query uses a subset of the aggregate provider's levels and measures it can use this provider and speed up the query.

Aggregate providers will use additional memory to store the intermediate aggregates,
the more levels and measures are added the more memory it requires.

There are actually two kinds of aggregate providers: the bitmap and the leaf.
The bitmap is generally faster but also takes more memory.
"""
from typing import Collection

from .._partial_aggregate_providers import PartialAggregateProvider
from ..level import Level
from ..measure import Measure

_BITMAP_KEY = "BITMAP"
_LEAF_KEY = "LEAF"


def bitmap(
    *, levels: Collection[Level], measures: Collection[Measure]
) -> PartialAggregateProvider:
    """Create a partial bitmap aggregate provider.

    Args:
        levels: The levels to build the bitmap provider on.
        measures: The measures to put in the bitmap provider.
    """
    return PartialAggregateProvider(
        key=_BITMAP_KEY,
        levels_coordinates=[level._coordinates for level in levels],
        measures_names=[measure.name for measure in measures],
    )


def leaf(
    *, levels: Collection[Level], measures: Collection[Measure]
) -> PartialAggregateProvider:
    """Create a partial leaf aggregate provider.

    Args:
        levels: The levels to build the leaf provider on.
        measures: The measures to put in the leaf provider.
    """
    return PartialAggregateProvider(
        key=_LEAF_KEY,
        levels_coordinates=[level._coordinates for level in levels],
        measures_names=[measure.name for measure in measures],
    )
