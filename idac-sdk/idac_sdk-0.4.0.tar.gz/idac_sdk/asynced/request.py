import httpx
import ujson
import asyncio
from typing import Any, Dict, List, Optional, Tuple, Union
from functools import wraps
from idac_sdk.models.vpn_config import VPNConfig, VPNType

from idac_sdk.types import IDACRequestStatus, IDACRequestType
from idac_sdk.log import logger
from . import DEFAULT_USER_AGENT, DEFAULT_WAIT_INTERVAL, DEFAULT_WAIT_TIMEOUT

from idac_sdk.asynced.controller import IDACAuthType, IDACController
from idac_sdk.errors import (
    IDACRequestStateError,
    IncorrectMinutesValue,
    IncorrectWantedStateError,
    NoControllerError,
    NoIdError,
    UnknownVPNType,
)
from idac_sdk.models.request_state import RequestState
from idac_sdk.session_data import SessionData


def check_controller(method):
    @wraps(method)
    def wrapper(self, *method_args, **method_kwargs):
        if not isinstance(self.controller, IDACController):
            raise NoControllerError("iDAC controller not provided")
        return method(self, *method_args, **method_kwargs)

    return wrapper


REQUEST_ERROR_STATES = [
    IDACRequestStatus.cancelled,
    IDACRequestStatus.error,
    IDACRequestStatus.onboardError,
]
REQUEST_GOOD_STATES = [
    IDACRequestStatus.active,
    IDACRequestStatus.executed,
    IDACRequestStatus.complete,
]


class IDACRequest:
    session_data: Optional[SessionData]
    controller: IDACController
    uuid: Optional[str]
    user_agent: str
    vpn: VPNConfig

    def __init__(
        self,
        uuid: Optional[str] = None,
        session_data: Optional[SessionData] = None,
        controller: Optional[IDACController] = None,
        user_agent: Optional[str] = None,
        vpn: Optional[VPNConfig] = None,
    ) -> None:
        """
        IDACRequest Object

        IDACRequest describes iDAC request object.
        Handles all operations with requests: create, cleanup, restart.

        Args:
            uuid (Optional[str], optional): Request UUID. Should be provided to work with existing
                requests Defaults to None.
            session_data (Optional[SessionData], optional): SessionData object. Will be send to iDAC
                controller Defaults to None.
            controller (Optional[IDACController], optional): IDACCOntroller object.
                Defaults to None.
            user_agent (Optional[str], optional): User-Agent string. Defaults to None.
            vpn (Optional[VPNConfig], optional): VPN options
        """
        if not uuid:
            # no UUID -> new request, need to set session_data and controller
            self.session_data = SessionData() if not session_data else session_data
            self.uuid = None
        else:
            # UUID provided -> existing request
            self.session_data = None
            self.uuid = uuid

        self.user_agent = user_agent if user_agent else DEFAULT_USER_AGENT

        if not controller and controller is not False:
            if isinstance(self.session_data, SessionData) and self.session_data.has("creds"):
                self.controller = IDACController(
                    auth_type=IDACAuthType.DCLOUD_SESSION,
                    auth=self.session_data.get("creds"),
                )
            else:
                self.controller = IDACController()
        else:
            self.controller = controller

        self.vpn = vpn or self.controller.vpn

    async def check_controller_auth(self) -> None:
        """Tells controller to request auth token if auth type is DCLOUD_SESSION"""
        logger.debug(f"Checking auth. Type is {self.controller.auth.type}")
        if self.controller.auth.type == IDACAuthType.DCLOUD_SESSION.name:
            assert self.session_data, "Session data not set"
            token = await self.controller.get_auth_token(
                self.session_data.get("creds"), self.session_data.get("datacenter")
            )
            logger.debug(f"dCloud token is: {token}")
        elif self.controller.auth.type == IDACAuthType.WORKER.name:
            token = await self.controller.get_auth_token()
            logger.debug(f"Worker token is: {token}")

    def add_vpn(self, where: dict[str, Any]) -> dict[str, Any]:
        """Adds VPN parameters to request

        Args:
            where (dict[str, Any]): Where VPN params should be added

        Raises:
            UnknownVPNType: Raised if unknown VPN type configured

        Returns:
            dict[str, Any]: updated dictionary with VPN parameters
        """
        logger.debug("Adding VPN parameters: %s", self.vpn)
        if ("idacVpn" in where) or (self.vpn.type == VPNType.none):
            return where

        if self.vpn.type == VPNType.vpod:
            # adding params for vPod VPN. `datacenter`, `vpod` and `anycpwd` should be loaded from session.xml
            where.update({"idacVpn": "dcloud-vpod"})
        elif self.vpn.type == VPNType.request or self.vpn.type == VPNType.explicit:
            # adding params for `request` - explicit VPN settings
            where.update(
                {
                    "idacVpn": "request",
                    "idacVpnHost": self.vpn.params.host,
                    "idacVpnUsername": self.vpn.params.username,
                    "idacVpnPassword": self.vpn.params.password,
                }
            )
        elif self.vpn.type == VPNType.secure_repo:
            # adding params for `secure_repo` - VPN settings will be loaded from secure repo
            where.update(
                {
                    "idacVpn": "secureRepo",
                    "idacVpnSecureRepoSpace": self.vpn.params.secure_repo_space,
                    "idacVpnSecureRepoFile": self.vpn.params.secure_repo_file,
                    "idacVpnSecureRepoBlock": self.vpn.params.secure_repo_block,
                    "idacVpnSecureRepoKey": self.vpn.params.secure_repo_key,
                }
            )
        else:
            raise UnknownVPNType("Unknown VPN type provided")

        return where

    @check_controller
    async def create(
        self, request_type: IDACRequestType = IDACRequestType.SIMPLE
    ) -> Tuple[RequestState, Optional[str]]:
        """Sends Create API request. All data taken from session_data

        Args:
            request_type (IDACRequestType, optional): Type of the request.
                Defaults to IDACRequestType.SIMPLE.

        Returns:
            RequestState: State of the new request
        """
        assert self.session_data, "Session data not set"
        await self.check_controller_auth()

        if request_type == IDACRequestType.STATEFUL:
            api, method = self.controller.api_create_stateful()
        elif request_type == IDACRequestType.STATELESS:
            api, method = self.controller.api_create_stateless()
        else:
            api, method = self.controller.api_create()

        headers: Dict[str, str] = {"Accept": "application/json"}
        self.controller.with_auth(headers)
        logger.debug(f"API: {method} to {api}")
        logger.debug(f"Headers are: {headers}")

        # convert SessionData to dict and populate VPN parameters
        data = self.add_vpn(self.session_data.dict(exclude_none=True))

        if method == "POST":
            # put data in body if POST
            kwargs = {"json": data}
            headers.update({"Content-Type": "application/json"})
        else:
            # put data in query string if GET
            kwargs = {"params": data}

        redirect = None
        st = None
        async with httpx.AsyncClient() as client:
            client.headers.update({"User-Agent": self.user_agent})
            r = await client.request(method, api, headers=headers, **kwargs)
            logger.debug(f"Got response: {r.status_code} {r.reason_phrase}")
            if r.status_code < 200 or r.status_code > 399:
                r.raise_for_status()

            json_body: dict = ujson.loads(r.text)
            st = RequestState(**json_body)
            if st.request:
                # grab UUID of a new automation
                self.uuid = st.request.uuid

            if r.status_code >= 300 and r.status_code < 400:
                # redirected
                redirect = r.headers.get("location")

        return st, redirect

    @check_controller
    async def get_state(self) -> RequestState:
        """Loads state of a request from controller

        Raises:
            NoIdError: if no ID/UUID set

        Returns:
            RequestState: State of the request
        """
        if not self.uuid:
            raise NoIdError("No ID/UUID provided for Get State")
        await self.check_controller_auth()

        api, method = self.controller.api_get_state(self.uuid)
        logger.debug(f"API: {method} to {api}")

        headers: Dict[str, str] = {"Accept": "application/json"}
        self.controller.with_auth(headers)

        async with httpx.AsyncClient() as client:
            client.headers.update({"User-Agent": self.user_agent})
            r = await client.request(method, api, headers=headers)
            if r.status_code < 200 or r.status_code > 399:
                r.raise_for_status()

            json_body: dict = ujson.loads(r.text)
            return RequestState(**json_body)

    @check_controller
    async def restart(self) -> None:
        """Restarts request

        Raises:
            NoIdError: if no ID/UUID set
        """
        if not self.uuid:
            raise NoIdError("No ID/UUID provided for Restart")
        await self.check_controller_auth()

        api, method = self.controller.api_restart(self.uuid)
        logger.debug(f"API: {method} to {api}")

        headers: Dict[str, str] = {"Accept": "application/json"}
        self.controller.with_auth(headers)

        async with httpx.AsyncClient() as client:
            client.headers.update({"User-Agent": self.user_agent})
            r = await client.request(method, api, headers=headers)
            logger.debug(f"Got response: {r.status_code} {r.reason_phrase}")
            if r.status_code < 200 or r.status_code > 399:
                r.raise_for_status()
            return

    @check_controller
    async def cleanup(self) -> None:
        """Cleans request

        Raises:
            NoIdError: if no ID/UUID set
        """
        if not self.uuid:
            raise NoIdError("No ID/UUID provided for Cleanup")
        await self.check_controller_auth()

        api, method = self.controller.api_cleanup(self.uuid)
        logger.debug(f"API: {method} to {api}")

        headers: Dict[str, str] = {"Accept": "application/json"}
        self.controller.with_auth(headers)

        async with httpx.AsyncClient() as client:
            client.headers.update({"User-Agent": self.user_agent})
            r = await client.request(method, api, headers=headers)
            logger.debug(f"Got response: {r.status_code} {r.reason_phrase}")
            if r.status_code < 200 or r.status_code > 399:
                r.raise_for_status()
            return

    @check_controller
    async def force_cleanup(self) -> None:
        """Forcibly cleans request

        Raises:
            NoIdError: if no ID/UUID set
        """
        if not self.uuid:
            raise NoIdError("No ID/UUID provided for Force Cleanup")
        await self.check_controller_auth()

        api, method = self.controller.api_force_cleanup(self.uuid)
        logger.debug(f"API: {method} to {api}")

        headers: Dict[str, str] = {"Accept": "application/json"}
        self.controller.with_auth(headers)

        async with httpx.AsyncClient() as client:
            client.headers.update({"User-Agent": self.user_agent})
            r = await client.request(method, api, headers=headers)
            logger.debug(f"Got response: {r.status_code} {r.reason_phrase}")
            if r.status_code < 200 or r.status_code > 399:
                r.raise_for_status()
            return

    @check_controller
    async def extend(self, minutes: int) -> None:
        """Extend a request by `minutes` minutes

        Args:
            minutes (int): amount of minutes

        Raises:
            NoIdError: if no ID provided
            IncorrectMinutesValue: if incorrect amount of minutes provided
        """
        if not self.uuid:
            raise NoIdError("No ID/UUID provided for Extend")
        if not minutes or not isinstance(minutes, int):
            raise IncorrectMinutesValue("Minutes should be an integer")
        await self.check_controller_auth()

        api, method = self.controller.api_extend(self.uuid, minutes=minutes)
        logger.debug(f"API: {method} to {api}")
        headers: Dict[str, str] = {"Accept": "application/json"}
        self.controller.with_auth(headers)

        async with httpx.AsyncClient() as client:
            client.headers.update({"User-Agent": self.user_agent})
            r = await client.request(method, api, headers=headers)
            logger.debug(f"Got response: {r.status_code} {r.reason_phrase}")
            if r.status_code < 200 or r.status_code > 399:
                r.raise_for_status()
            return

    @check_controller
    async def wait_for_status(
        self,
        wanted_state: List[Union[IDACRequestStatus, str]] = REQUEST_GOOD_STATES,  # type: ignore
        stop_on_error: bool = True,
        timeout: Optional[int] = DEFAULT_WAIT_TIMEOUT,
        interval: int = DEFAULT_WAIT_INTERVAL,
    ) -> None:
        """Waits for request to land in one of wanted states by periodically checking it's status

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
        if not self.uuid:
            raise NoIdError("No ID/UUID provided for Wait For Status")

        for idx, val in enumerate(wanted_state):
            if isinstance(val, str):
                wanted_state[idx] = IDACRequestStatus(val)
            elif not isinstance(val, IDACRequestStatus):
                raise IncorrectWantedStateError(f"Incorrect wanted state: {val}")

        async def try_infinite():
            while True:
                st = await self.get_state()
                status = IDACRequestStatus(st.status)
                if status in wanted_state:
                    return
                if stop_on_error and status in REQUEST_ERROR_STATES:
                    raise IDACRequestStateError(f"Request landed in error state: {status.value}")
                await asyncio.sleep(interval)

        await asyncio.wait_for(try_infinite(), timeout=timeout)

        return
