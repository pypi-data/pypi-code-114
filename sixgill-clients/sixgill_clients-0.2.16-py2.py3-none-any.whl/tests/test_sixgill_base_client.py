import os
from unittest import TestCase
from mock import patch
import logging
import requests
import json
import io

from sixgill.sixgill_base_client import SixgillBaseClient
from sixgill.sixgill_exceptions import AuthException


def util_load_json(path):
    file_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(file_dir, path)
    with io.open(abs_file_path, mode='r', encoding='utf-8') as f:
        return f.read()


class MockedResponse(object):
    def __init__(self, status_code, text, reason=None, url=None, method=None):
        self.status_code = status_code
        self.text = text
        self.reason = reason
        self.url = url
        self.request = requests.Request('GET')

    def json(self):
        return json.loads(self.text)


class TestSixgillBaseClient(TestCase):

    def setUp(self):
        self.sixgill_client = SixgillBaseClient('client_id', 'secret', 'random', logging.getLogger("test"))
        self.mocked_incidents_response = json.loads(util_load_json("mock_data/Darkfeed/darkfeed_data.json"))
        self.mocked_get_token_response = util_load_json("mock_data/token_response.json")
        self.mocked_alerts_response = mocked_alerts_response
        self.mocked_put_response = mocked_put_response

        self.bundle = 0
        self.submitted_indicators = 0

    def mocked_request(self, *args, **kwargs):
        request = kwargs.get("request", {})
        end_point = request.path_url
        method = request.method

        if (method == 'PUT') and request.body:
            self.mocked_incidents_response = '''[]'''
            self.mocked_alerts_response = '''[]'''

        self.response_dict = {
            'POST': {
                '/auth/token':
                    MockedResponse(200, self.mocked_get_token_response),
                '/darkfeed/ioc/ack':
                    MockedResponse(200, str(self.submitted_indicators)),
                '/darkfeed_freemium/ioc/ack':
                    MockedResponse(200, str(self.submitted_indicators)),
                '/ioc/enrich':
                    MockedResponse(200, util_load_json("mock_data/Darkfeed/darkfeed_enrich_data.json")),
                '/intel/intel_items':
                    MockedResponse(200, json.dumps(util_load_json("mock_data/IntelItems/post_intel_items.json")))
            },
            'GET': {
                '/alerts/feed/alerts?include_delivered_items=False&limit=1000&skip=0':
                    MockedResponse(200, json.dumps(json.loads(util_load_json("mock_data/Alerts/get_alerts.json")))),
                '/alerts/feed/alerts?include_delivered_items=False&skip=0&limit=1000':
                    MockedResponse(200, json.dumps(json.loads(util_load_json("mock_data/Alerts/get_alerts.json")))),
                '/darkfeed/ioc?limit=7':
                    MockedResponse(200, json.dumps(self.mocked_incidents_response[self.bundle])),
                '/darkfeed_freemium/ioc?limit=7':
                    MockedResponse(200, json.dumps(self.mocked_incidents_response[self.bundle])),
                '/intel/intel_items?query=sample':
                    MockedResponse(200, util_load_json("mock_data/IntelItems/get_intel_items.json"))
            },
            'PUT': {
                '/alerts/feed?consumer=random': MockedResponse(200, self.mocked_put_response)
            },
        }

        response_dict = self.response_dict.get(method)
        response = response_dict.get(end_point)

        if ((method == 'GET' and end_point == '/darkfeed/ioc?limit=7') or
                (method == 'GET' and end_point == '/darkfeed_freemium/ioc?limit=7')):
            self.submitted_indicators = len(self.mocked_incidents_response[self.bundle].get("objects")) - 2
            self.bundle += 1

        return response

    def mocked_bad_request(self, *args, **kwargs):
        return MockedResponse(404, self.mocked_get_token_response, "Bad request", '/mocked_url')

    def test_get_access_token(self):
        with patch('requests.sessions.Session.send', new=self.mocked_request):
            access_token = self.sixgill_client._get_access_token()

        expected_output = "this_is_my_token"
        self.assertEqual(access_token, expected_output)

    def test_bad_access_token(self):
        with patch('requests.sessions.Session.send', new=self.mocked_bad_request):
            self.assertRaises(AuthException, self.sixgill_client._get_access_token)


mocked_put_response = '''{"status": 200, "message": "Successfully Marked as Ingested Feed Items"}'''

mocked_alerts_response = '''[
    {
        "alert_name": "someSecretAlert2",
        "content": "",
        "date": "2019-08-06 23:20:35", 
        "id": "1", 
        "lang": "English", 
        "langcode": "en",
        "read": false, 
        "severity": 10, 
        "threat_level": "emerging", 
        "threats": ["Phishing"],
        "title": "someSecretAlert2", 
        "user_id": "123"},
    {
        "alert_name": "someSecretAlert4",
        "content": "",
        "date": "2019-08-18 09:58:10", 
        "id": "2", 
        "read": false, 
        "severity": 10,
        "threat_level": "imminent", 
        "threats": ["Data Leak", "Phishing"], 
        "title": "someSecretAlert4",
        "user_id": "132"}, 
    {
        "alert_name": "someSecretAlert1",
         "content": "",
         "date": "2019-08-18 22:58:23",
         "id": "3", 
         "read": false,
         "severity": 10, 
         "threat_level": "imminent",
         "threats": ["Data Leak", "Phishing"],
         "title": "someSecretAlert1",
         "user_id": "123"},
    {
        "alert_name": "someSecretAlert2",
        "content": "",
        "date": "2019-08-19 19:27:24", 
        "id": "4", 
        "lang": "English", 
        "langcode": "en",
        "read": false, 
        "severity": 10, 
        "threat_level": "emerging", 
        "threats": ["Phishing"],
        "title": "someSecretAlert2", 
        "user_id": "123"},
    {
        "alert_name": "someSecretAlert3",
        "content": "",
        "date": "2019-08-22 08:27:19",
        "id": "5", 
        "read": false, 
        "severity": 10,
        "threat_level": "imminent", 
        "threats": ["Data Leak", "Phishing"], 
        "title": "someSecretAlert3",
        "user_id": "123"}, 
    {
        "alert_name": "someSecretAlert1",
        "content": "",
        "date": "2019-08-22 08:43:15",
        "id": "6", 
        "read": false,
        "severity": 10, 
        "threat_level": "imminent",
        "threats": ["Data Leak", "Phishing"],
        "title": "someSecretAlert1",
        "user_id": "123"
    }]'''
