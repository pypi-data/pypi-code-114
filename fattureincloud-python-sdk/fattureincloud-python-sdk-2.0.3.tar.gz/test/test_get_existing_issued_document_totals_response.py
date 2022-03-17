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
from fattureincloud_python_sdk.model.issued_document_totals import IssuedDocumentTotals
globals()['IssuedDocumentTotals'] = IssuedDocumentTotals
from fattureincloud_python_sdk.model.get_existing_issued_document_totals_response import GetExistingIssuedDocumentTotalsResponse


class TestGetExistingIssuedDocumentTotalsResponse(unittest.TestCase):
    """GetExistingIssuedDocumentTotalsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetExistingIssuedDocumentTotalsResponse(self):
        """Test GetExistingIssuedDocumentTotalsResponse"""
        model = GetExistingIssuedDocumentTotalsResponse(
            data=IssuedDocumentTotals(
                amount_net=10.0,
                amount_rivalsa=0.0,
                amount_net_with_rivalsa=10.0,
                amount_cassa=3.14,
                taxable_amount=0.0,
                amount_vat=22.0,
                amount_gross=12.2,
                amount_due=12.2,
                payments_sum=12.2
            )
        )
        expected_json = '{"data": {"amount_net": 10.0, "amount_rivalsa": 0.0, "amount_net_with_rivalsa": 10.0, "amount_cassa": 3.14, "taxable_amount": 0.0, "amount_vat": 22.0, "amount_gross": 12.2, "amount_due": 12.2, "payments_sum": 12.2}}'
        actual_json = json.dumps(model.to_dict(), default=json_serial)
        assert actual_json == expected_json


if __name__ == '__main__':
    unittest.main()
