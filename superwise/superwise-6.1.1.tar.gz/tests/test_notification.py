from typing import List

import pytest
import requests
from google.cloud import storage
from google.oauth2 import service_account
from requests import Response

from superwise import Client
from superwise import Superwise
from superwise.models.notification import Notification


@pytest.fixture(scope="function")
def mock_get_token(monkeypatch):
    monkeypatch.setattr(
        Client,
        "get_token",
        lambda *args, **kwargs: "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjQ3ZDdmMDg2In0.eyJzdWIiOiI5YzNlZmUxZC03NGNlLTRlZTItYTMyOC1kMWZmNmQyMDAyM2YiLCJlbWFpbCI6InN3X2JhcmFrQHN1cGVyd2lzZS5haSIsInVzZXJNZXRhZGF0YSI6e30sInRlbmFudElkIjoiYmFyYWsiLCJyb2xlcyI6WyJWaWV3ZXIiXSwicGVybWlzc2lvbnMiOlsiZmUuc2VjdXJlLndyaXRlLnVzZXJBcGlUb2tlbnMiLCJmZS5zZWN1cmUuZGVsZXRlLnVzZXJBcGlUb2tlbnMiLCJmZS5zZWN1cmUucmVhZC51c2VyQXBpVG9rZW5zIl0sIm1ldGFkYXRhIjp7fSwiY3JlYXRlZEJ5VXNlcklkIjoiNDg5ZmM5Y2YtZDlhYy00MWMwLWJmM2ItN2VhNDUyNDY4ODEyIiwidHlwZSI6InVzZXJBcGlUb2tlbiIsInVzZXJJZCI6IjQ4OWZjOWNmLWQ5YWMtNDFjMC1iZjNiLTdlYTQ1MjQ2ODgxMiIsImlhdCI6MTYzNjY0ODIyMywiZXhwIjoxNjM2NzM0NjIzLCJpc3MiOiJmcm9udGVnZyJ9.qhEclIsSpfwXpCTFb8qhKpizRWtpQSnkE7VMsy9Et3guLcOcTiTVZ2wOJPmemtL3g3AStKH2jFSOEwQOoqnvgSR3dum9I_Ae3UwrFNRnM3EqOz7UsD0cJAd1AYy-69-67o5oX9A2U4MPZSA5Dr5Edbvn86-AsBJhADGDs5AyEyuGmlJTq0ACGAmoC8qZlxwnOsn9wIzTiQVU7085M73n5iJ26SNhsy4KNpU-8oR2lC1akDroHzL8aIr5dAWSWZz_cfcyWQyC1gqb4_ZAvG1GXiKwsGW2irFyfGoD9zrwMoMGuWXKCbXnHxIzuv8ImX_cRVPXq5xVBYUXwODr83Q3FA",
    )
    monkeypatch.setattr(Client, "get_service_account", lambda *args, **kwargs: {})


@pytest.fixture(scope="function")
def sw(mock_gcp_client):
    return Superwise(client_id="test", secret="test")


@pytest.fixture(scope="function")
def mock_gcp_client(monkeypatch):
    class GCSClient:
        def __init__(self, *args, **kwargs):
            self.name = "test"

        def bucket(self, bucket_name):
            return GCSClient()

        def blob(self, file_name):
            return GCSClient()

        def download_as_string(self):
            return "asdasdaas"

        def upload_from_string(self, data):
            return None

    monkeypatch.setattr(service_account.Credentials, "from_service_account_info", lambda *args, **kwargs: "")
    monkeypatch.setattr(storage, "Client", lambda *args, **kwargs: GCSClient())


@pytest.fixture(scope="function")
def mock_notification_requests(monkeypatch):
    get_response = Response()
    get_response._content = b'{"id": 14, "name": "oryan test 123", "type": "Email", "is_enabled": true, "is_hide": false, "created_at": 1647765197, "notification_metadata": {"target": ["oryan.omer@superwise.ai"]}, "last_delivery_status": "Success", "last_delivery_ts": 1647765208}'
    get_response.status_code = 201
    monkeypatch.setattr(requests, "post", lambda *args, **kwargs: get_response)
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: get_response)


def test_create_notification(mock_notification_requests, mock_get_token, sw):
    notification = sw.notification.create_email_notification(name="oryan test 123", email="oryan.omer@superwise.ai")
    assert isinstance(notification, Notification)
    assert notification.name == "oryan test 123"


def test_get_notification(mock_notification_requests, mock_get_token, sw):
    notification = sw.notification.get(name="oryan test 123")
    assert isinstance(notification, Notification)
