from typing import List, Optional, Tuple, Union

from idac_sdk.asynced.request import (
    DEFAULT_WAIT_INTERVAL,
    DEFAULT_WAIT_TIMEOUT,
    REQUEST_GOOD_STATES,
    IDACRequest as IDACRequestAsync,
    IDACRequestStatus,
    IDACRequestType,
)
from idac_sdk.models.request_state import RequestState
from idac_sdk.synced.helpers import sync_method


class IDACRequest(IDACRequestAsync):
    __idac_synced_obj__ = True

    @sync_method
    def check_controller_auth(self) -> None:
        return super().check_controller_auth()  # type: ignore

    @sync_method
    def create(
        self, request_type: IDACRequestType = IDACRequestType.SIMPLE
    ) -> Tuple[RequestState, Union[str, None]]:
        """Sends Create API request synchronously. All data taken from session_data

        Args:
            request_type (IDACRequestType, optional): Type of the request.
                Defaults to IDACRequestType.SIMPLE.

        Returns:
            RequestState: State of the new request
        """
        return super().create(request_type=request_type)  # type: ignore

    @sync_method
    def get_state(self) -> RequestState:
        """Loads state of a request from controller synchronously

        Raises:
            NoIdError: if no ID/UUID set

        Returns:
            RequestState: State of the request
        """
        return super().get_state()  # type: ignore

    @sync_method
    def restart(self) -> None:
        """Restarts request synchronously

        Raises:
            NoIdError: if no ID/UUID set
        """
        return super().restart()  # type: ignore

    @sync_method
    def cleanup(self) -> None:
        """Cleans request synchronously

        Raises:
            NoIdError: if no ID/UUID set
        """
        return super().cleanup()  # type: ignore

    @sync_method
    def force_cleanup(self) -> None:
        """Forcibly cleans request synchronously

        Raises:
            NoIdError: if no ID/UUID set
        """
        return super().force_cleanup()  # type: ignore

    @sync_method
    def extend(self, minutes: int) -> None:
        """Extend a request by `minutes` minutes

        Args:
            minutes (int): amount of minutes

        Raises:
            NoIdError: if no ID provided
            IncorrectMinutesValue: if incorrect amount of minutes provided
        """
        return super().extend(minutes)  # type: ignore

    @sync_method
    def wait_for_status(
        self,
        wanted_state: List[Union[IDACRequestStatus, str]] = REQUEST_GOOD_STATES,  # type: ignore
        stop_on_error: bool = True,
        timeout: Optional[int] = DEFAULT_WAIT_TIMEOUT,
        interval: int = DEFAULT_WAIT_INTERVAL,
    ) -> None:
        """
        Waits synchronously for the request to land in one of wanted states by periodically checking
        it's status.

        Args:
            wanted_state (List[Union[IDACRequestStatus, str]], optional): List of wanted statuses.
                Defaults to [ IDACRequestStatus.active, IDACRequestStatus.executed,
                IDACRequestStatus.complete, ].
            stop_on_error (bool, optional): Stop waiting if request errored. Defaults to True.
            timeout (int, optional): Timeout (in seconds). Max amout of time process should wait.
                If set to None will wait forever. Defaults to 10 minutes.
            interval (int, optional): Interval (seconds) between request. Defaults to 30 seconds.

        Raises:
            NoIdError: if no ID/UUID set
            IDACRequestStateError: if request is in errored status
            IncorrectWantedStateError: if incorrect wanted state provided
        """
        return super().wait_for_status(  # type: ignore
            wanted_state=wanted_state,
            stop_on_error=stop_on_error,
            timeout=timeout,
            interval=interval,
        )
