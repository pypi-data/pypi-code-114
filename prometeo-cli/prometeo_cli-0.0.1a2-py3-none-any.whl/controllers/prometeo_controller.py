import os

from client.prometeo_client import PrometeoClient
from pmo.helpers import SessionHandler
from pmo.config import PROMETEO_API_KEY


PROMETEO_SESSION = 'PROMETEO_SESSION'


def login(provider: str, username: str, password: str) -> None:
    client = PrometeoClient(PROMETEO_API_KEY)
    session_key = client.login(provider, username, password)
    session = SessionHandler()
    session.create_session(PROMETEO_SESSION, session_key)



def get_accounts():
    client = PrometeoClient(PROMETEO_API_KEY)
    client.get_accounts()
