import typing as t

import jwt
import requests
from jwt import PyJWKClient
from pydantic import ValidationError

from taktile_auth.exceptions import InvalidAuthException
from taktile_auth.schemas.session import SessionState
from taktile_auth.schemas.token import TaktileIdToken
from taktile_auth.settings import settings

ALGORITHM = "RS256"
AUTH_SERVER_URL: t.Dict[str, str] = {
    "local": "http://taktile-api.local.taktile.com:8000",
    "dev": "https://taktile-api.dev.taktile.com",
    "stg": "https://taktile-api.stg.taktile.com",
    "prod": "https://taktile-api.taktile.com",
    "expo": "https://taktile-api.expo.taktile.com",
}


class AuthClient:
    def __init__(
        self,
        url: str = AUTH_SERVER_URL[settings.ENV],
    ) -> None:
        self.public_key_url = f"{url}/.well-known/jwks.json"
        self.access_token_url = f"{url}/api/v1/login/access-token"
        self.client = PyJWKClient(self.public_key_url)

    def decode_id_token(self, token: t.Optional[str]) -> TaktileIdToken:
        if not token:
            raise InvalidAuthException("no-auth-provided")
        try:
            key = self.client.get_signing_key_from_jwt(token).key
            payload = jwt.decode(
                token,
                key,
                algorithms=[ALGORITHM],
                audience=settings.ENV,
            )
            token_data = TaktileIdToken(**payload)
        except jwt.ExpiredSignatureError:
            raise InvalidAuthException("signature-expired")
        except (jwt.PyJWTError, ValidationError):
            raise InvalidAuthException("could-not-validate")

        return token_data

    def get_access(
        self, *, session_state: SessionState
    ) -> t.Tuple[TaktileIdToken, SessionState]:
        if not session_state.api_key and not session_state.jwt:
            raise InvalidAuthException("no-auth-proved")
        if not session_state.jwt:
            res = requests.post(
                self.access_token_url,
                headers=session_state.to_auth_headers(),
            )
            res.raise_for_status()
            session_state.jwt = res.json()["id_token"]
        return self.decode_id_token(session_state.jwt), session_state
