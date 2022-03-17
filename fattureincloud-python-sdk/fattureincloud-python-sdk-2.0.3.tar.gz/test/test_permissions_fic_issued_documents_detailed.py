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
from fattureincloud_python_sdk.model.permission_level import PermissionLevel
globals()['PermissionLevel'] = PermissionLevel
from fattureincloud_python_sdk.model.permissions_fic_issued_documents_detailed import PermissionsFicIssuedDocumentsDetailed


class TestPermissionsFicIssuedDocumentsDetailed(unittest.TestCase):
    """PermissionsFicIssuedDocumentsDetailed unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPermissionsFicIssuedDocumentsDetailed(self):
        """Test PermissionsFicIssuedDocumentsDetailed"""
        model = PermissionsFicIssuedDocumentsDetailed(
            quotes=PermissionLevel("write"),
            proformas=PermissionLevel("write"),
            invoices=PermissionLevel("write"),
            receipts=PermissionLevel("write"),
            deliveryNotes=PermissionLevel("write"),
            creditNotes=PermissionLevel("write"),
            orders=PermissionLevel("write"),
            workReports=PermissionLevel("write"),
            supplierOrders=PermissionLevel("write"),
            selfInvoices=PermissionLevel("write")
        )
        expected_json = "{\"quotes\": \"write\", \"proformas\": \"write\", \"invoices\": \"write\", \"receipts\": \"write\", \"deliveryNotes\": \"write\", \"creditNotes\": \"write\", \"orders\": \"write\", \"workReports\": \"write\", \"supplierOrders\": \"write\", \"selfInvoices\": \"write\"}"
        actual_json = json.dumps(model.to_dict(), default=json_serial)
        assert actual_json == expected_json
        

if __name__ == '__main__':
    unittest.main()
