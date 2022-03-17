"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.9
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


import unittest
import unittest.mock
import fattureincloud_python_sdk
import functions
from fattureincloud_python_sdk.rest import RESTResponse
from fattureincloud_python_sdk.api.user_api import UserApi  # noqa: E501
from fattureincloud_python_sdk.model.user import User
from fattureincloud_python_sdk.model.company import Company
from fattureincloud_python_sdk.model.company_type import CompanyType
from fattureincloud_python_sdk.model.controlled_company import ControlledCompany
from fattureincloud_python_sdk.model.get_user_info_response import GetUserInfoResponse
from fattureincloud_python_sdk.model.get_user_info_response_info import GetUserInfoResponseInfo
from fattureincloud_python_sdk.model.get_user_info_response_email_confirmation_state import GetUserInfoResponseEmailConfirmationState
from fattureincloud_python_sdk.model.list_user_companies_response import ListUserCompaniesResponse
from fattureincloud_python_sdk.model.list_user_companies_response_data import ListUserCompaniesResponseData

class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = UserApi()
    
    def tearDown(self):
        pass

    def test_get_user_info(self):
        resp = {
            'status': 200,
            'data': b'{"data":{"id":2,"name":"Mario Verdi","first_name":"Mario","last_name":"Verdi","email":"mariov@erdi.it","picture":null,"hash":"aaa"},"info":{"need_password_change":false},"email_confirmation_state":{"need_confirmation":false}}',
            'reason': "OK"
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value = None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value = None)

        self.api.api_client.rest_client.GET = unittest.mock.MagicMock(return_value = mock_resp)
        expected = GetUserInfoResponse(data = User( id=2, name="Mario Verdi", first_name="Mario", last_name="Verdi", email="mariov@erdi.it", hash="aaa", picture=None ),
            info=GetUserInfoResponseInfo(
                need_password_change=False
            ),
            email_confirmation_state=GetUserInfoResponseEmailConfirmationState(
                need_confirmation=False
            ))

        actual = self.api.get_user_info()
        actual.data.id = 2
        assert actual == expected

    def test_list_user_companies(self):
        resp = {
            'status': 200,
            'data': b'{"data": {"companies": [{"access_token": "zpaiefapfjaojf56546456456", "connection_id": 2, "controlled_companies": [{"access_token": "zpaiefadpfjaojf56546456456", "connection_id": 2.0, "id": 2, "name": "mario2 srl", "tax_code": "01234567d9", "type": "company"}, {"access_token": "zpa4efadpfjaojf56546456456", "connection_id": 2.0, "id": 3, "name": "mario4 srl", "tax_code": "01234567df", "type": "company"}], "id": 2, "name": "mario srl", "tax_code": "0123456789", "type": "company"}]}}',
            'reason': "OK"
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value = None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value = None)

        self.api.api_client.rest_client.GET = unittest.mock.MagicMock(return_value = mock_resp)
        expected = ListUserCompaniesResponse(data = ListUserCompaniesResponseData(companies = [Company( id=2, name="mario srl", type=CompanyType("company"), access_token="zpaiefapfjaojf56546456456", connection_id=2, tax_code="0123456789", controlled_companies=[ ControlledCompany( id=2, name="mario2 srl", type=CompanyType("company"), access_token="zpaiefadpfjaojf56546456456", connection_id=2.0, tax_code="01234567d9" ), ControlledCompany( id=3, name="mario4 srl", type=CompanyType("company"), access_token="zpa4efadpfjaojf56546456456", connection_id=2.0, tax_code="01234567df" ) ] )]))
        actual = self.api.list_user_companies()
        actual.data.companies[0].id = 2
        assert actual == expected


if __name__ == '__main__':
    unittest.main()