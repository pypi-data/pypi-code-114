"""Type annotation constructs."""

from typing import Hashable, TypeVar

_NodeID = TypeVar("_NodeID", bound=Hashable)
_NodeID_co = TypeVar("_NodeID_co", bound=Hashable, covariant=True)
_NodeID_contra = TypeVar("_NodeID_contra", bound=Hashable, contravariant=True)

_EdgeID = TypeVar("_EdgeID", bound=Hashable)
_EdgeID_co = TypeVar("_EdgeID_co", bound=Hashable, covariant=True)
