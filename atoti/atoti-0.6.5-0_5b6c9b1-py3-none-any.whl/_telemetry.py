from __future__ import annotations

import atexit
import functools
import json
import os
import platform
import time
from abc import ABC
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta
from functools import lru_cache
from operator import attrgetter
from pathlib import Path
from typing import Any, Callable, Dict, List, Mapping, Optional, TypeVar, Union
from urllib.request import Request, urlopen
from uuid import UUID, uuid4

from atoti_core import get_env_flag, keyword_only_dataclass
from typing_extensions import ParamSpec

from ._get_non_personal_arguments import get_non_personal_arguments
from ._get_non_personal_type_name import get_non_personal_type_name
from ._path_utils import get_atoti_home
from ._plugins import is_plugin_active
from ._version import VERSION

_ASYNC_EXECUTOR = ThreadPoolExecutor(max_workers=1)

_INSTALLATION_ID_PATH = get_atoti_home() / "installation_id.txt"

_TELEMETRY_SERVICE_URL = "https://telemetry.atoti.io/events"

DISABLE_TELEMETRY_ENV_VAR = "ATOTI_DISABLE_TELEMETRY"

TEST_TELEMETRY_ENV_VAR = "ATOTI_TEST_TELEMETRY"

TELEMETERED_API_PATH = Path(__file__).parent / "data" / "telemetered-api.json"

TelemeteredApi = Dict[str, Dict[str, List[str]]]


@lru_cache
def _get_process_id() -> str:
    return str(uuid4())


@keyword_only_dataclass
@dataclass(frozen=True)
class Event(ABC):
    process_id: str = field(default_factory=_get_process_id, init=False)
    event_type: str


@keyword_only_dataclass
@dataclass(frozen=True)
class ImportEvent(Event):
    """Triggered when the library is imported."""

    event_type: str = field(default="import", init=False)
    installation_id: str
    operating_system: str
    python_version: str
    version: str
    environment: Optional[str]


@keyword_only_dataclass
@dataclass(frozen=True)
class ExitEvent(Event):
    """Triggered when the Python process terminates."""

    event_type: str = field(default="exit", init=False)
    duration: timedelta


@keyword_only_dataclass
@dataclass(frozen=True)
class CallEvent(Event):
    """Triggered when a function or method from the public API is called."""

    event_type: str = field(default="call", init=False)
    path: str
    duration: timedelta
    arguments: Mapping[str, str]
    error: Optional[str]


def _send_event_to_telemetry_service(event: Event) -> None:
    action: Callable[..., Any] = urlopen
    data = json.dumps({"events": [asdict(event)]}, default=str).encode("utf8")
    payload: Union[Request, str] = Request(
        _TELEMETRY_SERVICE_URL,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    if get_env_flag(TEST_TELEMETRY_ENV_VAR):
        action = print
        payload = data.decode("utf8")

    # Done in the background to not bother the user.
    _ASYNC_EXECUTOR.submit(
        # https://github.com/microsoft/pylance-release/issues/2025#issuecomment-958612654
        action,  # type: ignore
        payload,
    )


def _disabled_by_atoti_plus() -> bool:
    return is_plugin_active("plus")


def _disabled_by_environment_variable() -> bool:
    return get_env_flag(DISABLE_TELEMETRY_ENV_VAR)


def _get_installation_id_from_file() -> Optional[str]:
    if not _INSTALLATION_ID_PATH.exists():
        return None

    try:
        content = _INSTALLATION_ID_PATH.read_text(encoding="utf8").strip()
        UUID(content)
        return content
    except (OSError, ValueError):
        # The file cannot be read or its content is not a valid UUID.
        return None


def _write_installation_id_to_file(installation_id: str) -> None:
    try:
        _INSTALLATION_ID_PATH.parent.mkdir(
            exist_ok=True,
            parents=True,
        )
        _INSTALLATION_ID_PATH.write_text(
            f"{installation_id}{os.linesep}", encoding="utf8"
        )
    except OSError:
        # To prevent bothering the user, do nothing even if the id could not be written to the file.
        ...


@lru_cache
def _get_installation_id() -> str:
    existing_id = _get_installation_id_from_file()

    if existing_id is not None:
        return existing_id

    new_id = str(uuid4())

    _write_installation_id_to_file(new_id)

    return new_id


def _send_exit_event(*, imported_at: datetime) -> None:
    _send_event_to_telemetry_service(ExitEvent(duration=datetime.now() - imported_at))


@keyword_only_dataclass
@dataclass
class _CallTracker:
    tracking = False


_P = ParamSpec("_P")
_R = TypeVar("_R")


def _track_call(
    function: Callable[_P, _R], call_path: str, *args: _P.args, **kwargs: _P.kwargs
) -> _R:
    error_type_name = None
    call_time = time.perf_counter()
    try:
        return function(*args, **kwargs)
    except Exception as error:  # pylint: disable=broad-except
        try:
            error_type_name = get_non_personal_type_name(type(error))
        except:  # pylint: disable=bare-except
            # Do nothing to let the previous error be the one presented to the user.
            ...
        raise error
    finally:
        arguments: Dict[str, str] = {}

        try:
            arguments = get_non_personal_arguments(function, *args, **kwargs)
        except:  # pylint: disable=bare-except
            # Do nothing to not bother the user.
            ...

        duration = timedelta(seconds=time.perf_counter() - call_time)
        call_event = CallEvent(
            path=call_path,
            duration=duration,
            arguments=arguments,
            error=error_type_name,
        )
        _send_event_to_telemetry_service(call_event)


def _track_calls(
    function: Callable[_P, _R],
    *,
    call_path: str,
    call_tracker: _CallTracker,
) -> Callable[_P, _R]:
    @functools.wraps(function)
    def function_wrapper(
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> _R:
        if call_tracker.tracking:
            return function(*args, **kwargs)

        call_tracker.tracking = True

        try:
            return _track_call(function, call_path, *args, **kwargs)
        finally:
            call_tracker.tracking = False

    return function_wrapper


def _setup_call_tracking() -> None:
    call_tracker = _CallTracker()
    telemetered_api: TelemeteredApi = json.loads(TELEMETERED_API_PATH.read_bytes())

    for module_name, path_in_module_to_function_names in telemetered_api.items():
        module = __import__(module_name)
        for (
            path_in_module,
            function_names,
        ) in path_in_module_to_function_names.items():
            container = attrgetter(path_in_module)(module) if path_in_module else module
            for function_name in function_names:
                function = getattr(container, function_name)
                function_tracking_calls = _track_calls(
                    function,
                    call_path=f"""{module_name}.{f"{path_in_module}." if path_in_module else ""}{function_name}""",
                    call_tracker=call_tracker,
                )
                setattr(container, function_name, function_tracking_calls)


def telemeter() -> None:
    if _disabled_by_atoti_plus() or _disabled_by_environment_variable():
        return

    imported_at = datetime.now()

    import_event = ImportEvent(
        operating_system=platform.platform(),
        installation_id=_get_installation_id(),
        python_version=platform.python_version(),
        version=VERSION,
        environment="CI" if get_env_flag("CI") else None,
    )

    _send_event_to_telemetry_service(import_event)

    _setup_call_tracking()

    atexit.register(_send_exit_event, imported_at=imported_at)
