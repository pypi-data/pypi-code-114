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
from fattureincloud_python_sdk.model.permissions_fic_issued_documents_detailed import PermissionsFicIssuedDocumentsDetailed
globals()['PermissionLevel'] = PermissionLevel
globals()['PermissionsFicIssuedDocumentsDetailed'] = PermissionsFicIssuedDocumentsDetailed
from fattureincloud_python_sdk.model.permissions import Permissions


class TestPermissions(unittest.TestCase):
    """Permissions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPermissions(self):
        """Test Permissions"""
        model = Permissions(
            fic_situation=PermissionLevel("write"),
            fic_clients=PermissionLevel("write"),
            fic_suppliers=PermissionLevel("write"),
            fic_products=PermissionLevel("write"),
            fic_issued_documents=PermissionLevel("write"),
            fic_received_documents=PermissionLevel("write"),
            fic_receipts=PermissionLevel("write"),
            fic_calendar=PermissionLevel("write"),
            fic_archive=PermissionLevel("write"),
            fic_taxes=PermissionLevel("write"),
            fic_stock=PermissionLevel("write"),
            fic_cashbook=PermissionLevel("write"),
            fic_settings=PermissionLevel("write"),
            fic_emails=PermissionLevel("write"),
            fic_export=PermissionLevel("write"),
            fic_import_bankstatements=PermissionLevel("write"),
            fic_import_clients_suppliers=PermissionLevel("write"),
            fic_import_issued_documents=PermissionLevel("write"),
            fic_import_products=PermissionLevel("write"),
            fic_recurring=PermissionLevel("write"),
            fic_riba=PermissionLevel("write"),
            dic_employees=PermissionLevel("write"),
            dic_settings=PermissionLevel("write"),
            dic_timesheet=PermissionLevel("write"),
            fic_issued_documents_detailed=PermissionsFicIssuedDocumentsDetailed(
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
        )
        expected_json = "{\"fic_situation\": \"write\", \"fic_clients\": \"write\", \"fic_suppliers\": \"write\", \"fic_products\": \"write\", \"fic_issued_documents\": \"write\", \"fic_received_documents\": \"write\", \"fic_receipts\": \"write\", \"fic_calendar\": \"write\", \"fic_archive\": \"write\", \"fic_taxes\": \"write\", \"fic_stock\": \"write\", \"fic_cashbook\": \"write\", \"fic_settings\": \"write\", \"fic_emails\": \"write\", \"fic_export\": \"write\", \"fic_import_bankstatements\": \"write\", \"fic_import_clients_suppliers\": \"write\", \"fic_import_issued_documents\": \"write\", \"fic_import_products\": \"write\", \"fic_recurring\": \"write\", \"fic_riba\": \"write\", \"dic_employees\": \"write\", \"dic_settings\": \"write\", \"dic_timesheet\": \"write\", \"fic_issued_documents_detailed\": {\"quotes\": \"write\", \"proformas\": \"write\", \"invoices\": \"write\", \"receipts\": \"write\", \"deliveryNotes\": \"write\", \"creditNotes\": \"write\", \"orders\": \"write\", \"workReports\": \"write\", \"supplierOrders\": \"write\", \"selfInvoices\": \"write\"}}"
        actual_json = json.dumps(model.to_dict(), default=json_serial)
        assert actual_json == expected_json
        

if __name__ == '__main__':
    unittest.main()
