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

import fattureincloud_python_sdk
from functions import json_serial
from functions import create_from_json
from fattureincloud_python_sdk.model.receipt_pre_create_info import ReceiptPreCreateInfo
from fattureincloud_python_sdk.model.payment_account import PaymentAccount
from fattureincloud_python_sdk.model.vat_type import VatType
globals()['ReceiptPreCreateInfo'] = ReceiptPreCreateInfo
from fattureincloud_python_sdk.model.get_receipt_pre_create_info_response import GetReceiptPreCreateInfoResponse


class TestGetReceiptPreCreateInfoResponse(unittest.TestCase):
    """GetReceiptPreCreateInfoResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetReceiptPreCreateInfoResponse(self):
        """Test GetReceiptPreCreateInfoResponse"""
        model = GetReceiptPreCreateInfoResponse(
            data=ReceiptPreCreateInfo(
                numerations_list=[
                    "a/",
                    "b/"
                ],
                rc_centers_list=[
                    "bg",
                    "mi"
                ],
                payment_accounts_list=[
                    PaymentAccount(
                        id=1,
                        name="bank"
                    )
                ],
                categories_list=[
                    "cat5",
                    "cat6"
                ],
                vat_types_list=[
                    VatType(
                        value=22.0
                    )
                ]
            )          
        )

        expected_json = '{"data": {"numerations_list": ["a/", "b/"], "rc_centers_list": ["bg", "mi"], "payment_accounts_list": [{"id": 1, "name": "bank"}], "categories_list": ["cat5", "cat6"], "vat_types_list": [{"value": 22.0}]}}'
        actual_json = json.dumps(model.to_dict(), default=json_serial)
        assert actual_json == expected_json


if __name__ == '__main__':
    unittest.main()
