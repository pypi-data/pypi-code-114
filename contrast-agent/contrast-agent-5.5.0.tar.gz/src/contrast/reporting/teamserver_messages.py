# -*- coding: utf-8 -*-
# Copyright © 2022 Contrast Security, Inc.
# See https://www.contrastsecurity.com/enduser-terms-0317a for more details.
import base64

from requests.models import Response
from requests import put, post

import contrast
from contrast.agent.settings import Settings
from contrast.utils.timer import now_ms
from contrast.utils.decorators import fail_safely
from contrast.utils.service_util import sleep
from contrast.extern import structlog as logging

logger = logging.getLogger("contrast")

PYTHON = "Python"


class BaseTsMessage:
    def __init__(self):
        self.settings = Settings()

        self.base_url = f"{self.settings.api_url}/api/ng/"
        self.proxy = (
            self.settings.build_proxy_url() if self.settings.is_proxy_enabled else {}
        )

        self.server_name_b64 = _b64url_stripped(self.settings.get_server_name())
        self.server_path_b64 = _b64url_stripped(self.settings.get_server_path())
        self.server_type_b64 = _b64url_stripped(self.settings.get_server_type())
        auth_header = f"{self.settings.api_user_name}:{self.settings.api_service_key}"

        self.headers = {
            # the Authorization header must not have its padding stripped
            "Authorization": base64.urlsafe_b64encode(auth_header.encode()).decode(),
            "API-Key": self.settings.api_key,
            "Server-Name": self.server_name_b64,
            "Server-Path": self.server_path_b64,
            "Server-Type": self.server_type_b64,
            "X-Contrast-Agent": f"{PYTHON} {contrast.__version__}",
            "X-Contrast-Header-Encoding": "base64",
        }

        self.body = ""

    @property
    def name(self):
        raise NotImplementedError("This method should be implemented by subclass")

    @property
    def path(self):
        raise NotImplementedError("This method should be implemented by subclass")

    @property
    def request_method(self):
        raise NotImplementedError("This method should be implemented by subclass")

    @property
    def expected_response_code(self):
        return 200

    @property
    def last_update_or_now(self):
        return (
            self.settings.last_update_time_ms
            if self.settings.last_update_time_ms != 0
            else now_ms()
        )

    @fail_safely("Failed to process TS response")
    def process_response(self, response):
        raise NotImplementedError("This method should be implemented by subclass")

    def process_response_code(self, response):
        """
        Return True if response code is expected response code
        """
        if not isinstance(response, Response):
            return False

        # TODO: PYT-2120 handle 409, 410, and 5xx properly
        if response.status_code in (401, 408, 409, 410, 412):
            logger.debug(
                "Received %s response code from Teamserver. Sleeping for 15 minutes",
                direct_to_teamserver=1,
            )

            sleep(900)

            return False

        return response.status_code == self.expected_response_code


class ServerActivity(BaseTsMessage):
    def __init__(self):
        super().__init__()

        self.body = {"lastUpdate": self.last_update_or_now}

    @property
    def name(self):
        return "activity_server"

    @property
    def path(self):
        return "activity/server"

    @property
    def request_method(self):
        return put

    @fail_safely("Failed to process ServerActivity response")
    def process_response(self, response):
        settings = Settings()
        if not self.process_response_code(response):
            return

        body = response.json()

        settings.apply_ts_server_settings(body)


class BaseTsAppMessage(BaseTsMessage):
    def __init__(self):
        super().__init__()

        # App language should only be encoded for url paths, not for headers.
        self.app_language_b64 = _b64url_stripped(PYTHON)
        self.app_name_b64 = _b64url_stripped(self.settings.app_name)

        self.headers.update(
            {
                "Application-Language": PYTHON,
                "Application-Name": self.app_name_b64,
                "Application-Path": _b64url_stripped(self.settings.app_path),
            }
        )


class Preflight(BaseTsAppMessage):
    def __init__(self, findings):
        super().__init__()

        self.findings = findings

        self.body = {"messages": []}
        for idx, finding in enumerate(self.findings):
            message = {
                "appLanguage": PYTHON,
                "appName": self.settings.app_name,
                "appPath": self.settings.app_path,
                "appVersion": self.settings.app_version,
                "code": "TRACE",
                "data": finding.preflight,
                "key": idx,
            }
            self.body["messages"].append(message)

    @property
    def name(self):
        return "preflight"

    @property
    def path(self):
        return "preflight"

    @property
    def request_method(self):
        return put

    @fail_safely("Failed to process Preflight response")
    def process_response(self, response):
        if not self.process_response_code(response):
            return

        body = response.text
        finding_idxs_to_report = self._parse_body(body)
        for finding_idx in finding_idxs_to_report:
            finding = self.findings[finding_idx]  # pylint: disable=unused-variable

            # TODO: PYT-2118 here we will need to construct a Traces message and add it
            # to the reporting queue

    @staticmethod
    def _parse_body(body):
        """
        A preflight response body is a comma-separated list of finding indices that
        should be reported in a Traces message. Some elements of this list will have a
        *, meaning TS needs an AppCreate message before it will accept this finding. For
        now, we do not send findings with a *.

        TODO: PYT-2119 handle * preflight findings
        """
        indices = body.strip('"').split(",")
        return [int(index) for index in indices if index.isdigit()]


class Traces(BaseTsAppMessage):
    def __init__(self, findings):
        super().__init__()
        # TODO: PYT-2118


class ObservedRoute(BaseTsAppMessage):
    def __init__(self, observed_route):
        # This message does not need "Application-Path" header but it doesn't hurt
        # either.
        super().__init__()
        self.base_url = f"{self.settings.api_url}/agents/v1.0/"

        self.body = {
            "signature": observed_route.signature,
            "verb": observed_route.verb,
            "url": observed_route.url,
            "sources": self._parse_sources(observed_route.sources),
        }

        session_id = self.settings.config.get_session_id()
        if session_id:
            self.body.update({"session_id": session_id})

    @property
    def name(self):
        return "observed_route"

    @property
    def path(self):
        return f"routes/{self.server_name_b64}/{self.server_path_b64}/{self.server_type_b64}/{self.app_language_b64}/{self.app_name_b64}/observed"

    @property
    def request_method(self):
        return post

    @property
    def expected_response_code(self):
        return 204

    @fail_safely("Failed to process ObservedRoute response")
    def process_response(self, response):
        if not self.process_response_code(response):
            logger.debug("Unexpected ObservedRoute response from TS %s", response)

    def _parse_sources(self, sources):
        new_sources = []
        for source in sources:
            try:
                new_sources.append(dict(type=source.type, name=source.name))
            except Exception:
                logger.debug("Could not parse source %s", source)

        return new_sources


class ApplicationUpdate(BaseTsAppMessage):
    def __init__(self, libraries):
        super().__init__()

        self.headers.update({"Content-Type": "application/json"})

        # activity message sends "components" as "architectures"
        # so we will not send the "components" field at this time.

        # field "timestamp" represents the last time the app settings were changed.
        self.body = {
            "timestamp": self.last_update_or_now,
            "libraries": [
                lib.to_json(self.settings) for lib in libraries if lib.hash_code
            ],
        }

    @property
    def name(self):
        return "update_application"

    @property
    def path(self):
        return "update/application"

    @property
    def expected_response_code(self):
        return 204

    @property
    def request_method(self):
        return put

    @fail_safely("Failed to process ApplicationUpdate response")
    def process_response(self, response):
        if not self.process_response_code(response):
            logger.debug("Unexpected ApplicationUpdate response from TS %s", response)


class ApplicationInventory(BaseTsAppMessage):
    def __init__(self, routes):
        # This message does not need "Application-Path" header but it doesn't hurt
        # either.
        super().__init__()
        self.base_url = f"{self.settings.api_url}/agents/v1.0/"

        self.body = {
            "routes": [route.to_json() for route in routes.values()],
        }

        session_id = self.settings.config.get_session_id()
        if session_id:
            self.body.update({"session_id": session_id})

    @property
    def name(self):
        return "applications-inventory"

    @property
    def path(self):
        return f"applications/{self.server_name_b64}/{self.server_path_b64}/{self.server_type_b64}/{self.app_language_b64}/{self.app_name_b64}/inventory"

    @property
    def request_method(self):
        return post

    @property
    def expected_response_code(self):
        return 204

    @fail_safely("Failed to process ObservedRoute response")
    def process_response(self, response):
        if not self.process_response_code(response):
            logger.debug("Unexpected ObservedRoute response from TS %s", response)


def _b64url_stripped(header_str):
    """
    For some headers, TS expects a value that
    - is base64 encoded using URL-safe characters
    - has any padding (= or ==) stripped

    This follows RFC-4648 - base64 with URL and filename safe alphabet
    """
    return base64.urlsafe_b64encode(header_str.encode()).rstrip(b"=").decode("utf-8")
