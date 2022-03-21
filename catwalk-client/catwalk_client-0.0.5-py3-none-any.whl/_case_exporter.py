import json
import logging
from datetime import datetime, timedelta
from time import sleep
from urllib.parse import urlencode

import requests

from catwalk_common import OpenCase

logger = logging.getLogger("catwalk_client")


class CaseExporter:

    def __init__(self, from_datetime: datetime, to_datetime: datetime, catwalk_url: str,
                 submitter_name: str = None, submitter_version: str = None, max_retries: int = 5, batch: int = 1):
        self.from_datetime = from_datetime
        self.to_datetime = to_datetime
        self.catwalk_url = catwalk_url

        self.filters = self._build_filters(submitter_name, submitter_version, from_datetime, to_datetime)
        self.max_retries = max_retries
        self.batch = batch

    def export(self):
        for date in self._hour_range():
            current_retry = 0
            path = f"/api/cases/export/{date.year}/{date.month}/{date.day}/{date.hour}"

            if self.filters:
                path += f'?{urlencode(self.filters)}'

            next_token = self._get_url(path)

            while next_token:
                response = requests.get(next_token)

                if not response.ok:
                    self._handle_retry(current_retry, response)
                    current_retry += 1
                    continue

                next_token = None
                data = json.loads(response.text)
                for item in data['items']:
                    yield OpenCase.parse_obj(item)

                if data['next_part'] and data['items']:
                    next_token = data['next_part']

    def _handle_retry(self, current_retry: int, response):
        if current_retry < self.max_retries:
            multiplier = (current_retry * 2) or 1
            logger.info(f"[catwalk-export] Retry ({current_retry + 1}/{self.max_retries}) for url {response.url} "
                        f"because got error {response.status_code}")
            sleep(0.5 * multiplier)
        else:
            raise Exception("Max retries exceeded")

    @staticmethod
    def _build_filters(submitter_name: str, submitter_version: str, from_datetime: datetime, to_datetime: datetime):
        filters = {
            "submitter_name": submitter_name,
            "submitter_version": submitter_version,
            "from_timestamp": from_datetime.isoformat(),
            "to_timestamp": to_datetime.isoformat()
        }
        return {k: v for k, v in filters.items() if v is not None}

    def _get_url(self, path: str):
        return self.catwalk_url.rstrip('/') + path

    def _hour_range(self):
        start, end = self.from_datetime, self.to_datetime

        while start < end:
            yield start
            start += timedelta(hours=1)
