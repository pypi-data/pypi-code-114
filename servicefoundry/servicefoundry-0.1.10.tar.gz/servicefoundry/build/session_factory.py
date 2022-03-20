import os
import json
from .const import SESSION_FILE

from .session import ServiceFoundrySession
from .auth_service_client import AuthServiceClient


# @TODO Call service foundry to get this.
DEFAULT_TENANT_ID = "e9101843-f287-4637-b089-8f5aab4a39aa"


def get_session(session_file=SESSION_FILE):
    if os.getenv("SERVICE_FOUNDRY_API_KEY"):
        auth_client = AuthServiceClient()
        return auth_client.login_with_api_token(
            DEFAULT_TENANT_ID, os.getenv("SERVICE_FOUNDRY_API_KEY")
        )

    if os.path.isfile(session_file):
        with open(session_file, "r") as file:
            data = json.load(file)
            return ServiceFoundrySession(
                **data, refresher=AuthServiceClient().refresh_token
            )
