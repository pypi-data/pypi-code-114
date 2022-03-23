import pytest
import requests
from google.cloud import storage
from google.oauth2 import service_account
from pandas import DataFrame
from requests import Response

from superwise import Client
from superwise import Superwise
from superwise.models.notification import Notification
from superwise.resources.superwise_enums import NotifyUpon
from superwise.resources.superwise_enums import ScheduleCron


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
def mock_monitor_get_policy_templates(monkeypatch):
    def mock_monitors_get_templates_logic(*args, **kwargs):
        get_response = Response()
        get_response._content = b"""
            [
          {
            "description": "Scanning the X top important features for long-lasting drift on the entire set level",
            "name": "Feature stability"
          },
          {
            "description": "Scan input drift on the segment level",
            "name": "Dataset shift"
          },
          {
           "description": "Alert when input is above a certain threshold from the baseline",
           "name": "Training-Serving skew"
          },
          {
            "description": "Missing values on a feature level on a segment level",
            "name": "Missing values"
          },
          {
            "description": "Anomaly in % of outliers on a feature level (numeric only)",
            "name": "Out-of-Range"
          },
          {
            "description": "Anomaly in % of new values on a feature level (categorical only)",
            "name": "New values"
          }]
            """
        get_response.status_code = 200
        return get_response

    monkeypatch.setattr(requests, "get", mock_monitors_get_templates_logic)


@pytest.fixture(scope="function")
def mock_empty_monitor_get_policy_templates(monkeypatch):
    def mock_monitors_get_templates_not_templates_logic(*args, **kwargs):
        get_response = Response()
        get_response._content = b""
        get_response.status_code = 200
        return get_response

    monkeypatch.setattr(requests, "get", mock_monitors_get_templates_not_templates_logic)


@pytest.fixture(scope="function")
def mock_bad_response_monitor_get_policy_templates(monkeypatch):
    def mock_monitors_get_templates_not_bad_status_code_logic(*args, **kwargs):
        get_response = Response()
        get_response._content = b"Internal Server Error"
        get_response.status_code = 500
        return get_response

    monkeypatch.setattr(requests, "get", mock_monitors_get_templates_not_bad_status_code_logic)


@pytest.fixture(scope="function")
def mock_monitor_post_create_policy_from_templates(monkeypatch):
    def mock_monitor_create_policy_from_template_logic(*args, **kwargs):
        post_response = Response()
        post_response.status_code = 201
        return post_response

    monkeypatch.setattr(requests, "post", mock_monitor_create_policy_from_template_logic)


def test_get_policy_templates(mock_monitor_get_policy_templates, mock_get_token, sw):
    templates = sw.policy.get_policy_templates()
    assert isinstance(templates, DataFrame)
    assert sorted(templates.columns.tolist()) == ["description", "name"]
    assert len(templates) == 6


def test_get_policy_templates_when_no_template(mock_empty_monitor_get_policy_templates, mock_get_token, sw):
    with pytest.raises(AssertionError):
        sw.policy.get_policy_templates()


def test_get_policy_templates_when_get_error_response(
    mock_bad_response_monitor_get_policy_templates, mock_get_token, sw
):
    with pytest.raises(Exception):
        sw.policy.get_policy_templates()


def test_create_policy_from_template(mock_monitor_post_create_policy_from_templates, mock_get_token, sw):
    response = sw.policy.create_policy_from_template(
        model_id=1,
        template_name="template_id",
        policy_name="test policy",
        notification_channels=[Notification(id=1)],
        notify_upon=NotifyUpon.detection_and_resolution,
        schedule=ScheduleCron.EVERY_2ND_MONTH,
    )
    assert response.status_code == 201
