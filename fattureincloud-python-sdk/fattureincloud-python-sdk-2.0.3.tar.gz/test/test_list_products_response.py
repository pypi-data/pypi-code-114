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
from fattureincloud_python_sdk.model.list_products_response_page import ListProductsResponsePage
from fattureincloud_python_sdk.model.pagination import Pagination
from fattureincloud_python_sdk.model.product import Product
from fattureincloud_python_sdk.model.vat_type import VatType
globals()['ListProductsResponsePage'] = ListProductsResponsePage
globals()['Pagination'] = Pagination
globals()['Product'] = Product
from fattureincloud_python_sdk.model.list_products_response import ListProductsResponse


class TestListProductsResponse(unittest.TestCase):
    """ListProductsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListProductsResponse(self):
        """Test ListProductsResponse"""
        model = ListProductsResponse(
            data=[
                Product(
                    id=1,
                    name="name_example",
                    code="code_example",
                    net_price=3.14,
                    gross_price=3.14,
                    use_gross_price=True,
                    default_vat=VatType(
                        id=1,
                        value=22.0,
                        description="Non imponibile art. 123",
                        notes="IVA non imponibile ai sensi dell articolo 123, comma 2",
                        e_invoice=True,
                        ei_type="2",
                        ei_description="ei_description_example",
                        is_disabled=True,
                    ),
                    net_cost=3.14,
                    measure="measure_example",
                    description="description_example",
                    category="category_example",
                    notes="notes_example",
                    in_stock=True,
                    stock_initial=3.14,
                    average_cost=3.14,
                    average_price=3.14,
                    created_at="created_at_example",
                    updated_at="updated_at_example",
                ),
                Product(
                    id=2,
                    name="name_example2",
                    code="code_example2",
                    net_price=23.14,
                    gross_price=23.14,
                    use_gross_price=True,
                    default_vat=VatType(
                        id=1,
                        value=22.0,
                        description="Non imponibile art. 123",
                        notes="IVA non imponibile ai sensi dell articolo 123, comma 2",
                        e_invoice=True,
                        ei_type="2",
                        ei_description="ei_description_example",
                        is_disabled=True,
                    ),
                    net_cost=23.14,
                    measure="measure_example",
                    description="description_example",
                    category="category_example",
                    notes="notes_example",
                    in_stock=True,
                    stock_initial=23.14,
                    average_cost=23.14,
                    average_price=23.14,
                    created_at="created_at_example",
                    updated_at="updated_at_example",
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
        expected_json = '{"data": [{"id": 1, "name": "name_example", "code": "code_example", "net_price": 3.14, "gross_price": 3.14, "use_gross_price": true, "default_vat": {"id": 1, "value": 22.0, "description": "Non imponibile art. 123", "notes": "IVA non imponibile ai sensi dell articolo 123, comma 2", "e_invoice": true, "ei_type": "2", "ei_description": "ei_description_example", "is_disabled": true}, "net_cost": 3.14, "measure": "measure_example", "description": "description_example", "category": "category_example", "notes": "notes_example", "in_stock": true, "stock_initial": 3.14, "average_cost": 3.14, "average_price": 3.14, "created_at": "created_at_example", "updated_at": "updated_at_example"}, {"id": 2, "name": "name_example2", "code": "code_example2", "net_price": 23.14, "gross_price": 23.14, "use_gross_price": true, "default_vat": {"id": 1, "value": 22.0, "description": "Non imponibile art. 123", "notes": "IVA non imponibile ai sensi dell articolo 123, comma 2", "e_invoice": true, "ei_type": "2", "ei_description": "ei_description_example", "is_disabled": true}, "net_cost": 23.14, "measure": "measure_example", "description": "description_example", "category": "category_example", "notes": "notes_example", "in_stock": true, "stock_initial": 23.14, "average_cost": 23.14, "average_price": 23.14, "created_at": "created_at_example", "updated_at": "updated_at_example"}], "current_page": 10, "first_page_url": "http://url.com", "last_page": 10, "last_page_url": "http://url.com", "next_page_url": "http://url.com", "path": "http://url.com", "per_page": 10, "prev_page_url": "http://url.com", "to": 10, "total": 10}'
        actual_json = json.dumps(model.to_dict(), default=json_serial)
        assert actual_json == expected_json


if __name__ == '__main__':
    unittest.main()
