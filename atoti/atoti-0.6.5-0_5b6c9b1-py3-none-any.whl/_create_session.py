from __future__ import annotations

from typing import Any, Mapping

from atoti_core import EMPTY_MAPPING, deprecated

from ._runtime_type_checking_utils import typecheck
from .config._session_config import SessionConfig
from .session import Session


@typecheck
def create_session(
    name: str = "Unnamed", *, config: Mapping[str, Any] = EMPTY_MAPPING
) -> Session:
    deprecated(
        "Creating sessions with `create_session()` is deprecated, use `Session()` directly instead."
    )
    return Session(
        config=SessionConfig._from_mapping(config),
        name=name,
    )
