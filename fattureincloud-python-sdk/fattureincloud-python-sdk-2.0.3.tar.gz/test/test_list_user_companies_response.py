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
from fattureincloud_python_sdk.model.list_user_companies_response_data import ListUserCompaniesResponseData
from fattureincloud_python_sdk.model.company import Company
from fattureincloud_python_sdk.model.company_type import CompanyType
from fattureincloud_python_sdk.model.controlled_company import ControlledCompany
globals()['ListUserCompaniesResponseData'] = ListUserCompaniesResponseData
from fattureincloud_python_sdk.model.list_user_companies_response import ListUserCompaniesResponse


class TestListUserCompaniesResponse(unittest.TestCase):
    """ListUserCompaniesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListUserCompaniesResponse(self):
        """Test ListUserCompaniesResponse"""
        model = ListUserCompaniesResponse(
            data = ListUserCompaniesResponseData(
                companies=[
                    Company(
                        id=1,
                        name="mario srl",
                        type=CompanyType("company"),
                        access_token="zpaiefapfjaojf56546456456",
                        connection_id=2,
                        tax_code="0123456789",
                        controlled_companies=[
                            ControlledCompany(
                                id=2,
                                name="mario2 srl",
                                type=CompanyType("company"),
                                access_token="zpaiefadpfjaojf56546456456",
                                connection_id=2.0,
                                tax_code="01234567d9"
                            ),
                            ControlledCompany(
                                id=3,
                                name="mario4 srl",
                                type=CompanyType("company"),
                                access_token="zpa4efadpfjaojf56546456456",
                                connection_id=2.0,
                                tax_code="01234567df"
                            )
                        ]
                    ),
                    Company(
                        id=2,
                        name="mario srl",
                        type=CompanyType("company"),
                        access_token="zpaiefapfjaojf56546456456",
                        connection_id=3,
                        tax_code="0123456789",
                        controlled_companies=[
                            ControlledCompany(
                                id=2,
                                name="mario2 srl",
                                type=CompanyType("company"),
                                access_token="zpaiefadpfjaojf56546456456",
                                connection_id=3.0,
                                tax_code="01234567d9"
                            ),
                            ControlledCompany(
                                id=3,
                                name="mario4 srl",
                                type=CompanyType("company"),
                                access_token="zpa4efadpfjaojf56546456456",
                                connection_id=3.0,
                                tax_code="01234567df"
                            )
                        ]
                    )
                ]
            )
        )
        expected_json = "{\"data\": {\"companies\": [{\"id\": 1, \"name\": \"mario srl\", \"type\": \"company\", \"access_token\": \"zpaiefapfjaojf56546456456\", \"connection_id\": 2, \"tax_code\": \"0123456789\", \"controlled_companies\": [{\"id\": 2, \"name\": \"mario2 srl\", \"type\": \"company\", \"access_token\": \"zpaiefadpfjaojf56546456456\", \"connection_id\": 2.0, \"tax_code\": \"01234567d9\"}, {\"id\": 3, \"name\": \"mario4 srl\", \"type\": \"company\", \"access_token\": \"zpa4efadpfjaojf56546456456\", \"connection_id\": 2.0, \"tax_code\": \"01234567df\"}]}, {\"id\": 2, \"name\": \"mario srl\", \"type\": \"company\", \"access_token\": \"zpaiefapfjaojf56546456456\", \"connection_id\": 3, \"tax_code\": \"0123456789\", \"controlled_companies\": [{\"id\": 2, \"name\": \"mario2 srl\", \"type\": \"company\", \"access_token\": \"zpaiefadpfjaojf56546456456\", \"connection_id\": 3.0, \"tax_code\": \"01234567d9\"}, {\"id\": 3, \"name\": \"mario4 srl\", \"type\": \"company\", \"access_token\": \"zpa4efadpfjaojf56546456456\", \"connection_id\": 3.0, \"tax_code\": \"01234567df\"}]}]}}"
        actual_json = json.dumps(model.to_dict(), default=json_serial)
        assert actual_json == expected_json

if __name__ == '__main__':
    unittest.main()
