import json
import os
import sys
from enum import Enum
from typing import Optional, Union

import requests
from automagically.exceptions import (
    AutomagicallyAuthenticationError,
    AutomagicallyError,
    AutomagicallyPermissionError,
    AutomagicallyServicesTransactionLimitError,
    DeserializeException,
)
from automagically.response import AutomagicallyResponse
from automagically.services.emails import Email, EmailsServiceAPI
from automagically.services.sms import Sms, SmsServiceAPI
from dotenv import load_dotenv
from loguru import logger


class AppEnvironmentTypes(Enum):
    PRODUCTION = "production"
    STAGING = "staging"
    LOCAL = "local"


AUTOMAGICALLY_STATUS_CODE_EXCEPTION = {
    429: AutomagicallyServicesTransactionLimitError,
    401: AutomagicallyAuthenticationError,
    403: AutomagicallyPermissionError,
}


load_dotenv()


class Client:
    def __init__(self, api_key: str = None, logging: bool = False):

        self.logging = logging

        if api_key:
            self.api_key = api_key
        elif os.getenv("AUTOMAGICALLY_API_KEY"):
            self.api_key = os.getenv("AUTOMAGICALLY_API_KEY")
        else:
            logger.error(
                "You need to set AUTOMAGICALLY_API_KEY env or pass api_key to Client - More Infos: aty.sh/api-key-missing"
            )
            raise AutomagicallyAuthenticationError()

        self._emails = EmailsServiceAPI(client=self)
        self._sms = SmsServiceAPI(client=self)

    @property
    def sms(self) -> SmsServiceAPI:
        return self._sms

    @property
    def emails(self) -> EmailsServiceAPI:
        return self._emails

    @property
    def api_url(self) -> str:
        # staging url for now
        if os.getenv("AUTOMAGICALLY_API_URL"):
            return os.getenv("AUTOMAGICALLY_API_URL")
        return "https://api.automagically.sh/"

    @property
    def api_version(self) -> str:
        return "v0"

    def request(
        self,
        method: str,
        url: str,
        params: dict = None,
        data: dict = None,
        headers: dict = None,
        content_type: Optional[str] = "application/json",
    ) -> requests.Response:

        headers = headers or {}

        headers["api-key"] = self.api_key
        headers["Content-type"] = content_type

        if content_type == "text/plain":
            return requests.request(
                method=method, url=url, data=data, params=params, headers=headers
            )

        return requests.request(
            method=method, url=url, json=data, params=params, headers=headers
        )

    def do_service_request(
        self,
        method: str,
        service_url: Optional[str] = None,
        data: Optional[Union[dict, Email, Sms, str]] = None,
        params: Optional[dict] = None,
        url_for_request: Optional[str] = None,
        content_type: Optional[str] = "application/json",
    ) -> AutomagicallyResponse:
        if isinstance(data, (Email, Sms)):
            data = data.get()

        url = url_for_request or f"{self.api_url}{service_url}"
        logger.info(url)

        raw_response = self.request(
            method=method, url=url, data=data, params=params, content_type=content_type
        )

        automagically_response = AutomagicallyResponse(
            content=raw_response.text,
            status_code=raw_response.status_code,
            headers=raw_response.headers,
            url=raw_response.url,
            method=raw_response.request.method,
        )

        if not automagically_response.ok:
            if automagically_response.status_code == 404:
                logger.error(
                    "Can not connect to Automagically API. Do you have internet access? More Infos: aty.sh/api-404"
                )
                return automagically_response
            elif automagically_response.status_code == 502:
                logger.error(
                    "Can not connect to Automagically API. Please try again in a few minutes! More Infos: aty.sh/api-502"
                )
                return automagically_response

            logger.error(
                f"status_code={raw_response.status_code}, content={raw_response.content}"
            )
            self.raise_automagically_exception(automagically_response)

        try:
            caller_name = sys._getframe().f_back.f_code.co_name + " - "
        except Exception:
            caller_name = ""

        if self.logging:
            logger.warning(
                f"{caller_name}Status_code: {automagically_response.status_code}, Content: {automagically_response.json}"
            )

        return automagically_response

    def raise_automagically_exception(
        self, automagically_response: AutomagicallyResponse
    ) -> None:

        try:
            error_content = json.loads(automagically_response.content)
        except ValueError as error:
            raise DeserializeException(automagically_response.content) from error
        messages = error_content.get("messages")
        error_code = error_content.get("error_code")
        status_code = error_content.get("status_code")
        support_id = error_content.get("support_id")
        self.specify_error(
            messages,
            error_code,
            status_code,
            support_id,
            automagically_response.method,
            automagically_response.url,
        )

    def specify_error(
        self,
        message: str,
        error_code: str,
        status_code: int,
        support_id: str,
        method: Optional[str],
        url: str,
    ) -> None:
        exception = AUTOMAGICALLY_STATUS_CODE_EXCEPTION.get(
            status_code, AutomagicallyError
        )
        raise exception(message, error_code, status_code, support_id, method, url)

    def send_email(self, data: Union[Email, dict]) -> requests.Response:
        if isinstance(data, Email):
            data = data.get()
        return self._emails.send(data)

    def send_sms(self, data: Union[Sms, dict]) -> requests.Response:
        if isinstance(data, Sms):
            data = data.get()
        return self._sms.send(data)

    def send_telegram_message(
        self,
        message: str,
        bot_slug: str = os.getenv("AUTOMAGICALLY_TELEGRAM_BOT_SLUG"),
        chat_id: int = os.getenv("AUTOMAGICALLY_TELEGRAM_CHAT_ID"),
    ) -> requests.Response:

        if not bot_slug:
            logger.error(
                "You need to set AUTOMAGICALLY_TELEGRAM_BOT_SLUG - More Infos: aty.sh/AUTOMAGICALLY_TELEGRAM_BOT_SLUG"
            )
            return

        if not chat_id:
            logger.error(
                "You need to set AUTOMAGICALLY_TELEGRAM_CHAT_ID - More Infos: aty.sh/AUTOMAGICALLY_TELEGRAM_CHAT_ID"
            )
            return

        SERVICE_URL = f"telegram/bots/{bot_slug}/send_message?chat_id={chat_id}"

        return self.do_service_request(
            "POST", SERVICE_URL, message.encode("utf-8"), content_type="text/plain"
        )

    def publish_event(self, event_name: str, event: dict) -> requests.Response:

        SERVICE_URL = "events/events"

        return self.do_service_request(
            "POST", SERVICE_URL, event, params={"event_name": event_name}
        )
