# pylint: disable=missing-class-docstring, import-error, missing-function-docstring
import json
from syncari.rest.client import SyncariRestClient
from syncari.logger import SyncariLogger

logger = SyncariLogger.get_logger('test_router')

def test_get_url():
    rest_client = SyncariRestClient('http://universities.hipolabs.com/', None, None)
    resp = rest_client.get_url('http://universities.hipolabs.com/search?country=United+States')
    assert resp.status_code == 200
    university_names = [university['name'] for university in resp.json()]
    assert 'Stanford University' in university_names

def test_rest_request():
    rest_client = SyncariRestClient('http://universities.hipolabs.com/', None, None)
    resp = rest_client.rest_request('GET', 'search?country=United+States')
    assert resp.status_code == 200
    university_names = [university['name'] for university in resp.json()]
    assert 'Stanford University' in university_names

def test_post_request():
    rest_client = SyncariRestClient('https://api.provarity.com/', None, None)
    auth_data = {'user':'customer+syncari_admin@provarity.com', 'pass':'U3luY2FyaTF8Y3VzdG9tZXIrc3luY2FyaV9hZG1pbkBwcm92YXJpdHkuY29t'}
    resp = rest_client.rest_request('POST', 'user/login/provarity', json=auth_data)
    assert resp.status_code == 200
    resp_json = resp.json()
    resp_token_key = resp.json()['token']['key']
    assert resp_token_key is not None
