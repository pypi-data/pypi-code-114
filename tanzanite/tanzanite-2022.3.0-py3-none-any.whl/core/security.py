# -*- encoding: utf-8 -*-

"""Tanzanite core security functions."""


# pylint: disable=missing-function-docstring

# Standard imports
import json
import logging
import sys

from datetime import datetime, timedelta
from pathlib import Path
from typing import (
    Any,
    AnyStr,
    List,
    Tuple,
    Union,
)
from urllib.parse import urlencode

# External imports
import requests

# TODO(dittrich): https://github.com/Mckinsey666/bullet/issues/2
# Workaround until bullet has fix for Windows missing 'termios'.
try:
    from bullet import (
        Password,
        Input,
        VerticalPrompt,
        colors,
    )
except ModuleNotFoundError:
    pass
from fastapi import status
from jose import jwt
from jose.exceptions import ExpiredSignatureError
from passlib.context import CryptContext
from psec.secrets_environment import SecretsEnvironment
from psec.utils import safe_delete_file
from requests.structures import CaseInsensitiveDict

# Local imports
from tanzanite.core.config import settings
from tanzanite.utils import (
    prompt_for_input,
    prompt_for_password,
    USERNAME_PROMPT,
)


JWT_FILENAME = 'jwt.json'
SECRETS_ENV = SecretsEnvironment()

logger = logging.getLogger(__name__)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(
    subject: Union[str, Any],
    expires_delta: timedelta = None
) -> str:
    """
    Return a time-limited JWT access token for subject `subject`.
    """
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=int(settings.tanzanite_jws_token_expire_minutes)
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(
        to_encode,
        settings.tanzanite_secret_key,
        algorithm=settings.tanzanite_jws_algorithm
    )
    return encoded_jwt


def get_token_exp(token: Union[str, Any]) -> list:
    """
    Get the subject and expiration values for a JWT token string.
    """
    access_token = (
        token.get('access_token')
        if isinstance(token, dict)
        else token
    )
    payload = jwt.decode(
        access_token,
        settings.tanzanite_secret_key,
        algorithms=[settings.tanzanite_jws_algorithm]
    )
    return payload.get('exp', 0.0)


def is_expired_token(token: str):
    """
    Returns `True` if the token is not expired, else `False`.
    """
    try:
        token_expiration = get_token_exp(token=token)
    except ExpiredSignatureError:
        seconds_left = 0.0
    else:
        seconds_left = datetime.utcnow().timestamp() - float(token_expiration)  # noqa
    # Avoid a race condition by 'expiring' a little bit early.
    return seconds_left < 10.0


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify whether plaintext password matches hash.
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Return a hash of `password`.
    """
    return pwd_context.hash(password)


def get_jwt_path():
    """
    Return path to JWT file.
    """
    return Path(SECRETS_ENV.get_tmpdir_path(create_path=True)) / JWT_FILENAME


def get_token_from_environment_dir(
    jwt_path: Path = None,
):
    """
    Reads JWT token from file stored in python-secrets environment.
    """
    if jwt_path is None:
        jwt_path = get_jwt_path()
    try:
        token = json.loads(Path(jwt_path).read_text(encoding='utf-8'))
    except FileNotFoundError:
        token = None
    return token

    # try:
    #     token_username, token_expiration = get_values_from_token(
    #         token=token
    #     )
    # except ExpiredSignatureError:
    #     token_expired = True
    # else:
    #     seconds_left = datetime.utcnow().timestamp() - token_expiration  # noqa
    #     token_expired = seconds_left < 1
    # if (
    #     not token_expired
    #     and token_username == username
    # ):
    #     print(
    #         f"[+] '{token_username}' is already logged in "
    #         f"(expires in {int(seconds_left)} seconds)"
    #     )
    #     sys.exit(0)

    # if is_token_expired(token):
    #     return None
    # return token


def save_token_to_environment_dir(
    token: dict = None,
    jwt_path: Path = None,
):
    """
    Writes JWT token to file stored in python-secrets environment.
    """
    if jwt_path is None:
        jwt_path = get_jwt_path()
    Path(jwt_path).write_text(json.dumps(token), encoding='utf-8')
    logger.info("[+] wrote JWT to '%s'", jwt_path)
    return True


def get_auth_headers(
    token: Union[str, Any]
):
    """
    Return headers associated with a JWT.
    """
    headers = CaseInsensitiveDict()
    headers['Accept'] = 'application/json'
    headers['Authorization'] = f'Bearer {token}'
    return headers


"""    # nosec  # noqa: C901"""  # noqa


def get_cached_auth_token(
    jwt_path: Path = None,
):
    """
    Attempt to get a cached JWT from a previous login event and make
    sure it is a valid token before returning it to the caller. If
    the token is expired, remove the file.
    """
    if jwt_path is None:
        jwt_path = get_jwt_path()
    token = get_token_from_environment_dir(jwt_path=jwt_path)
    if token is not None:
        logger.debug("[+] read JWT from '%s'", jwt_path)
        if is_expired_token(token=token):
            logger.debug("[-] removing expired JWT '%s'", jwt_path)
            try:
                safe_delete_file(str(jwt_path))
            except RuntimeError:
                sys.exit(f"[!] failed to remove JWT '{jwt_path}'")
        else:
            logger.debug("[+] already logged in")
    return token


def prompt_for_login_creds(
    username: AnyStr = '',
) -> List[Tuple[AnyStr, AnyStr]]:
    # ) -> List[Tuple[Union[str, None], Union[str, None]]]:
    """
    Use Bullet vertical prompt to get login credentials.
    """
    cli = VerticalPrompt(
        [
            Input(
                prompt=f"{USERNAME_PROMPT}: ",
                default=username,
                word_color=colors.foreground["yellow"],
                strip=True,
            ),
            Password(
                prompt='Password: ',
                hidden="*",
                word_color=colors.foreground["yellow"]
            ),
        ]
    )
    response = cli.launch()
    return response


# >> Issue: [B107:hardcoded_password_default] Possible hardcoded password: ''
#    Severity: Low   Confidence: Medium
#    Location: tanzanite/core/security.py:XXX:0
#    More Info: https://bandit.readthedocs.io/en/latest/plugins/b107_hardcoded_password_default.html  # noqa
def cli_login_for_access_token(  # nosec  # noqa C901  FIXME
    jwt_path: Path = None,
    cache_auth_token: bool = True,
    grant_type: str = "password",
    username: str = None,
    password: str = None,
    scope: str = "",
    client_id: str = "",
    client_secret: str = "",
):
    """
    If that is not possible, use the API to obtain a new authorization
    token using `username` and `password`.

    If `cache_auth_token` is `True` and `jwt_path` is set, the token will
    be cached for use by later commands until it expires or is deleted.
    """
    if username is None:
        username = prompt_for_input(prompt=USERNAME_PROMPT)
        if username not in ['', None]:
            sys.exit('[-] cancelled login')
    if password is None:
        password = prompt_for_password()
        if password not in ['', None]:
            sys.exit('[-] cancelled login')
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = urlencode(
        {
            "grant_type": grant_type,
            "username": username,
            "password": password,
            "scope": scope,
            "client_id": client_id,
            "client_secret": client_secret,
        }
    )
    try:
        # FIXME (API_BASE_URL vs. get_api_base_url())
        response = requests.post(
            f"{settings.API_BASE_URL}/login/access-token",
            headers=headers,
            data=data,
        )
    except requests.exceptions.ConnectionError as err:
        if 'Connection refused' in str(err):
            sys.exit('[-] connection refused: is the API server running?')
        else:
            sys.exit(str(err))
    result = response.json()
    token = result.get('access_token')
    if token is None or response.status_code != status.HTTP_200_OK:
        sys.exit(
            "[-] failed to get access token: "
            f'{response.status_code} {response.reason}'
        )
    if jwt_path is None:
        jwt_path = get_jwt_path()
    if cache_auth_token:
        save_token_to_environment_dir(
            jwt_path=jwt_path,
            token=token,
        )
    logger.info('[+] login successful')
    return token


# vim: set ts=4 sw=4 tw=0 et :
