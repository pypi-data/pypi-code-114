"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.10
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


import datetime
import json
import sys
import unittest

import fattureincloud_python_sdk
from functions import json_serial
from functions import create_from_json
from fattureincloud_python_sdk.model.e_invoice_rejection_reason import EInvoiceRejectionReason
globals()['EInvoiceRejectionReason'] = EInvoiceRejectionReason
from fattureincloud_python_sdk.model.get_e_invoice_rejection_reason_response import GetEInvoiceRejectionReasonResponse


class TestGetEInvoiceRejectionReasonResponse(unittest.TestCase):
    """GetEInvoiceRejectionReasonResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetEInvoiceRejectionReasonResponse(self):
        """Test GetEInvoiceRejectionReasonResponse"""
        model = GetEInvoiceRejectionReasonResponse(
            data = EInvoiceRejectionReason(
                reason="invalid date",
                code="c01",
                ei_status="rejected",
                date=datetime.datetime.strptime('2022-01-01', '%Y-%m-%d').date()
            )
        )
        expected_json = "{\"data\": {\"reason\": \"invalid date\", \"code\": \"c01\", \"ei_status\": \"rejected\", \"date\": \"2022-01-01\"}}"
        actual_json = json.dumps(model.to_dict(), default=json_serial)
        assert actual_json == expected_json


if __name__ == '__main__':
    unittest.main()
