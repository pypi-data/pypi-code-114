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
from fattureincloud_python_sdk.model.f24 import F24
from fattureincloud_python_sdk.model.list_f24_response_aggregated_data import ListF24ResponseAggregatedData
from fattureincloud_python_sdk.model.list_f24_response_aggregation import ListF24ResponseAggregation
from fattureincloud_python_sdk.model.list_f24_response_page import ListF24ResponsePage
from fattureincloud_python_sdk.model.pagination import Pagination
from fattureincloud_python_sdk.model.f24_status import F24Status
from fattureincloud_python_sdk.model.payment_account import PaymentAccount
from fattureincloud_python_sdk.model.payment_account_type import PaymentAccountType
globals()['F24'] = F24
globals()['ListF24ResponseAggregatedData'] = ListF24ResponseAggregatedData
globals()['ListF24ResponseAggregation'] = ListF24ResponseAggregation
globals()['ListF24ResponsePage'] = ListF24ResponsePage
globals()['Pagination'] = Pagination
from fattureincloud_python_sdk.model.list_f24_response import ListF24Response



class TestListF24Response(unittest.TestCase):
    """ListF24Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListF24Response(self):
        """Test ListF24Response"""
        model = ListF24Response(
                        data=[
                F24(
                    id=1,
                    due_date=datetime.datetime.strptime("2022-01-01", '%Y-%m-%d').date(),
                    status=F24Status("paid"),
                    payment_account=PaymentAccount(
                        id=1,
                        name="Conto Banca Intesa",
                        type=PaymentAccountType("standard"),
                        iban="iban_example",
                        sia="sia_example",
                        cuc="cuc_example",
                        virtual=True
                    ),
                    amount=300.0,
                    attachment_token="attachment_token_example",
                    description="description_example"
                ),
                F24(
                    id=2,
                    due_date=datetime.datetime.strptime("2022-01-02", '%Y-%m-%d').date(),
                    status=F24Status("paid"),
                    payment_account=PaymentAccount(
                        id=2,
                        name="Conto Banca Unicredici",
                        type=PaymentAccountType("standard"),
                        iban="iban_example",
                        sia="sia_example",
                        cuc="cuc_example",
                        virtual=True
                    ),
                    amount=31.0,
                    attachment_token="attachment_token_example",
                    description="description_example"
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
        expected_json = '{"data": [{"id": 1, "due_date": "2022-01-01", "status": "paid", "payment_account": {"id": 1, "name": "Conto Banca Intesa", "type": "standard", "iban": "iban_example", "sia": "sia_example", "cuc": "cuc_example", "virtual": true}, "amount": 300.0, "attachment_token": "attachment_token_example", "description": "description_example"}, {"id": 2, "due_date": "2022-01-02", "status": "paid", "payment_account": {"id": 2, "name": "Conto Banca Unicredici", "type": "standard", "iban": "iban_example", "sia": "sia_example", "cuc": "cuc_example", "virtual": true}, "amount": 31.0, "attachment_token": "attachment_token_example", "description": "description_example"}], "current_page": 10, "first_page_url": "http://url.com", "last_page": 10, "last_page_url": "http://url.com", "next_page_url": "http://url.com", "path": "http://url.com", "per_page": 10, "prev_page_url": "http://url.com", "to": 10, "total": 10}'
        actual_json = json.dumps(model.to_dict(), default=json_serial)
        assert actual_json == expected_json


if __name__ == '__main__':
    unittest.main()
