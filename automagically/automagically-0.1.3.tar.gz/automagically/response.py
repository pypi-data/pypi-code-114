import json
from typing import Any, Optional

from automagically.exceptions import DeserializeException
from loguru import logger
from requests.structures import CaseInsensitiveDict


class AutomagicallyResponse(object):
    def __init__(
        self,
        content: str,
        status_code: int,
        url: str,
        method: Optional[str],
        headers: CaseInsensitiveDict,
    ):
        self.content = content
        self.status_code = status_code
        self.headers = headers
        self.url = url
        self.method = method
        self._json = None

    @property
    def ok(self) -> bool:
        return not (self.status_code < 200 or self.status_code >= 400)

    @property
    def json(self) -> Optional[dict]:
        if self.status_code < 200 or self.status_code >= 400:
            return None

        if self._json is not None:
            return self._json

        try:
            json_content = json.loads(self.content)
        except ValueError:
            return self.content
        self._json = json_content

        return self._json

    @property
    def data_id(self) -> str:
        try:
            return self.content.text["data_id"]
        except Exception:
            logger.error("Response does not contain a data_id")
            return None

    @property
    def management_url(self) -> str:
        try:
            return self.content.text["management_url"]
        except Exception:
            logger.error("Response does not contain a management_url")
            return None

    @property
    def resource_url(self) -> str:
        try:
            return self.content.text["resource_url"]
        except Exception:
            logger.error("Response does not contain a resource_url")
            return None


class PageResponse(AutomagicallyResponse):
    def __init__(
        self,
        content: str,
        status_code: int,
        url: str,
        method: Optional[str],
        headers: CaseInsensitiveDict,
    ):
        super().__init__(content, status_code, url, method, headers)

    @property
    def next(self):
        return self._json.get("next")

    @property
    def previous(self):
        return self._json.get("previous")

    @property
    def count(self):
        return self._json.get("count")

    @property
    def results(self):
        return self._json.get("results")
