import json
import logging
import os
from datetime import datetime, timedelta

import requests
from ._case_builder import CaseBuilder
from ._case_exporter import CaseExporter
from catwalk_common import CommonCaseFormat

logger = logging.getLogger("catwalk_client")


def _hour_range(start, end):
    while start < end:
        yield start
        start += timedelta(hours=1)


class CatwalkClient:
    submitter_name: str
    submitter_version: str
    catwalk_url: str

    def __init__(self, submitter_name: str = None, submitter_version: str = None, catwalk_url: str = None):
        self.submitter_name = submitter_name
        self.submitter_version = submitter_version
        self.catwalk_url = catwalk_url or os.environ.get("CATWALK_URL")

    def new_case(self) -> CaseBuilder:
        return CaseBuilder(client=self)

    def _get_url(self, path: str):
        return self.catwalk_url.rstrip('/') + path

    def send(self, case: dict):
        case = CommonCaseFormat(
            submitter={"name": self.submitter_name, "version": self.submitter_version},
            **case
        )

        response = requests.post(self._get_url("/api/cases/collect"), data=case.json())

        if response.ok:
            data = json.loads(response.text)
            logger.info(f"Collected catwalk case: {data['id']}")

    def export_cases(self, from_datetime: datetime, to_datetime: datetime,
                     submitter_name: str = None, submitter_version: str = None, max_retries: int = 5):
        exporter = CaseExporter(from_datetime=from_datetime, to_datetime=to_datetime, catwalk_url=self.catwalk_url,
                                submitter_name=submitter_name, submitter_version=submitter_version,
                                max_retries=max_retries)
        yield from exporter.export()
