"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.9
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


import json
import sys
import unittest
import datetime
import fattureincloud_python_sdk
from functions import json_serial
from functions import create_from_json
from fattureincloud_python_sdk.model.archive_document import ArchiveDocument
from fattureincloud_python_sdk.model.list_archive_documents_response_page import ListArchiveDocumentsResponsePage
from fattureincloud_python_sdk.model.pagination import Pagination
globals()['ArchiveDocument'] = ArchiveDocument
globals()['ListArchiveDocumentsResponsePage'] = ListArchiveDocumentsResponsePage
globals()['Pagination'] = Pagination
from fattureincloud_python_sdk.model.list_archive_documents_response import ListArchiveDocumentsResponse


class TestListArchiveDocumentsResponse(unittest.TestCase):
    """ListArchiveDocumentsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListArchiveDocumentsResponse(self):
        """Test ListArchiveDocumentsResponse"""
        model = ListArchiveDocumentsResponse(
            data=[
                ArchiveDocument(
                    id=1,
                    date=datetime.datetime.strptime("2022-01-01", '%Y-%m-%d').date(),
                    description="description_example",
                    category="category_example",
                    attachment_token="attachment_token_example"
                ),
                ArchiveDocument(
                    id=10,
                    date=datetime.datetime.strptime("2022-01-02", '%Y-%m-%d').date(),
                    description="description_example",
                    category="category_example",
                    attachment_token="attachment_token_example"
                )
            ],
            current_page=10,
            first_page_url="http://url.com",
            last_page=10,
            last_page_url="http://url.com",
            next_page_url="http://url.com",
            path="http://url.com",
            per_page=10,
            prev_page_url="http://url.com",
            to=10,
            total=10
        )
        expected_json = '{"data": [{"id": 1, "date": "2022-01-01", "description": "description_example", "category": "category_example", "attachment_token": "attachment_token_example"}, {"id": 10, "date": "2022-01-02", "description": "description_example", "category": "category_example", "attachment_token": "attachment_token_example"}], "current_page": 10, "first_page_url": "http://url.com", "last_page": 10, "last_page_url": "http://url.com", "next_page_url": "http://url.com", "path": "http://url.com", "per_page": 10, "prev_page_url": "http://url.com", "to": 10, "total": 10}'
        actual_json = json.dumps(model.to_dict(), default=json_serial)
        assert actual_json == expected_json


if __name__ == '__main__':
    unittest.main()
