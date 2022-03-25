from dataclasses import dataclass
from typing import Any, Dict, Mapping, Protocol, TypeVar, cast

from atoti_core import BaseCubes, keyword_only_dataclass

from ._delegate_mutable_mapping import DelegateMutableMapping
from ._local_cube import LocalCube

_LocalCube = TypeVar("_LocalCube", bound="LocalCube[Any, Any, Any]", covariant=True)


class _DeleteCube(Protocol):
    def __call__(self, cube_name: str) -> None:
        ...


class _RetrieveCube(Protocol[_LocalCube]):
    def __call__(self, cube_name: str) -> _LocalCube:
        ...


class _RetrieveCubes(Protocol[_LocalCube]):
    def __call__(self) -> Mapping[str, _LocalCube]:
        ...


@keyword_only_dataclass
@dataclass(frozen=True)
class LocalCubes(DelegateMutableMapping[str, _LocalCube], BaseCubes[_LocalCube]):
    """Local cubes class."""

    _delete_cube: _DeleteCube
    _retrieve_cube: _RetrieveCube[_LocalCube]
    _retrieve_cubes: _RetrieveCubes[_LocalCube]

    def _update(  # pylint: disable=no-self-use
        self, other: Mapping[str, _LocalCube]
    ) -> None:
        raise NotImplementedError("Use Session.create_cube() to create a cube.")

    def __getitem__(self, key: str) -> _LocalCube:
        """Get the cube with the given name."""
        return self._retrieve_cube(key)

    def _get_underlying(self) -> Dict[str, _LocalCube]:
        return cast(Dict[str, _LocalCube], self._retrieve_cubes())

    def __delitem__(self, key: str) -> None:
        """Delete the cube with the given name."""
        try:
            self._delete_cube(key)
        except KeyError:
            raise Exception(f"No cube named {key}") from None
