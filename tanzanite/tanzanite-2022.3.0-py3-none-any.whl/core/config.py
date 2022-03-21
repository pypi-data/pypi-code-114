# -*- coding: utf-8 -*-

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

"""
Settings class for consolidating configuration settings values.

The original code base from which this project repository was created split
variable definition between several files (including a `.env` file in the
`tanzanite/tanzanite/` directory.  That file has been removed and all variables
defined in it moved into `psec` secrets descriptions in the
`tanzanite/secrets.d/' directory. A few are set below (see comments) for lack
of a better way to handle them.
"""

# Standard imports
import json
import os
import sys
import textwrap
import warnings

from pathlib import Path
from typing import (
    Any,
    Dict,
    List,
    Optional,
    Union,
)

# External imports
from psec.exceptions import InvalidBasedirError
with warnings.catch_warnings():
    warnings.simplefilter("ignore", category=DeprecationWarning)
    from psec.secrets_environment import SecretsEnvironment
from pydantic import (  # pylint: disable=no-name-in-module
    AnyHttpUrl,
    BaseSettings,
    EmailStr,
    HttpUrl,
    PostgresDsn,
    validator,
)

# Local imports
from tanzanite import (
    DEFAULT_API_VER,
    SERVER_HOST,
    SERVER_NAME,
    SERVER_PORT,
)
from tanzanite.utils import get_version


ENVIRONMENT_REQUIRED_MSG = textwrap.dedent(
    """\
    [-] Tanzanite requires a fully configured python-secrets (psec) environment
    [-] holding necessary settings and secrets for operation. Please ensure the
    [-] default environment is set (see `psec environments default --help`), the
    [-] environment variables `D2_ENVIRONMENT` and/or `D2_SECRETS_BASEDIR` are
    [-] set as needed, or create the environment and ensure it is correctly
    [-] populated before trying again.
    """  # noqa
)
# FIXME: insert help URL here

# class SqliteUrl(AnyUrl):
#     """Validator class for sqlite3 database URLs."""
#     allowed_schemes = {'sqlite'}


# Ensure required settings that were not already exported as environment
# variables just above are exported now before the Settings() object
# is created.
#
try:
    secrets_environment = SecretsEnvironment(
        environment=os.getenv('D2_ENVIRONMENT', None),
        export_env_vars=True
    )
except InvalidBasedirError:
    sys.exit(ENVIRONMENT_REQUIRED_MSG)

secrets_environment.requires_environment()
secrets_environment.read_secrets_and_descriptions()
secrets_file_path = secrets_environment.get_secrets_file_path()

# TODO(dittrich): Integrate these into secrets environment files.

#
# The `FLOWER_BASIC_AUTH` variable was only being set in `.env` file.
# It appears to only be accessed by `flower` when it runs via the
# process environment. For now, setting it here manually to get rid of
# the `.env` file (though this now requires that it be set in the
# environment via `psec` or the `Settings` class.
# TODO(dittrich): Work out a psec variable for this?
FLOWER_BASIC_AUTH = f"admin:{os.environ.get('TANZANITE_ADMIN_PASSWORD')}"
os.environ['FLOWER_BASIC_AUTH'] = FLOWER_BASIC_AUTH
#

# Re-export for Settings()
os.environ['EMAILS_FROM_EMAIL'] = os.environ.get(
    'tanzanite_admin_user_email', ''
)
os.environ['EMAILS_FROM_NAME'] = 'Tanzanite System Owner'
os.environ['SERVER_NAME'] = os.environ.get('SERVER_NAME', SERVER_NAME)
os.environ['SERVER_HOST'] = os.environ.get('SERVER_HOST', SERVER_HOST)
os.environ['SERVER_PORT'] = str(SERVER_PORT)
#
os.environ['SMTP_TLS'] = str(os.environ.get('SMTP_TLS', 'false'))

SQLITE_DATABASE_PATH = (
    Path(secrets_environment.get_environment_path()) / f"{str(secrets_environment)}.db"  # noqa
)
os.environ['SQLITE_DATABASE_PATH'] = str(SQLITE_DATABASE_PATH)

# Build `BACKEND_CORS_ORIGINS` similarly to what was in `tanzanite/.env` file.
# It will look like this:
# '["http://localhost","http://localhost:3000","http://localhost:4200",\
# "http://localhost:8080","http://tanzanite.com","http://dev.tanzanite.com",\
# "http://stage.tanzanite.com"]'

CORS_DOMAIN = os.environ.get('SERVER_NAME')
BACKEND_CORS_ORIGINS = [f"http://{CORS_DOMAIN}", f"https://{CORS_DOMAIN}"]
ports = ['3000', '4200', '8080']
if SERVER_PORT not in ports:
    ports.append(SERVER_PORT)
BACKEND_CORS_ORIGINS.extend(
    [f"http://{CORS_DOMAIN}:{port}" for port in ports]
)
BACKEND_CORS_ORIGINS.extend(
    [f"https://{CORS_DOMAIN}:{port}" for port in ports]
)
BACKEND_CORS_ORIGINS.extend(
    [
        "http://tanzanite.com",
        "http://dev.tanzanite.com",
        "http://stage.tanzanite.com",
        # "http://local.dockertoolbox.tiangolo.com",
        # "http://localhost.tiangolo.com",
        "https://tanzanite.com",
        "https://dev.tanzanite.com",
        "https://stage.tanzanite.com",
        # "https://local.dockertoolbox.tiangolo.com",
        # "https://localhost.tiangolo.com",
    ]
)
ORIGINS = ",".join([f'"{item}"' for item in BACKEND_CORS_ORIGINS])
os.environ['BACKEND_CORS_ORIGINS'] = f'[{ORIGINS}]'
os.environ['API_VER'] = os.environ.get('API_VER', DEFAULT_API_VER)
# os.environ['API_BASE_URL'] = get_api_base_url(
#     api_ver=os.environ.get('API_VER'),
#     port=os.environ.get('SERVER_PORT', DEFAULT_API_PORT),
# )
os.environ['API_BASE_URL'] = f"{SERVER_HOST}:{SERVER_PORT}"
os.environ['API_PATH'] = f"api/{os.environ.get('API_VER')}"

# See: https://pydantic-docs.helpmanual.io/usage/settings/


def json_config_settings_source(
    settings: BaseSettings,  # pylint: disable=redefined-outer-name
) -> Dict[str, Any]:
    """
    A simple settings source that loads variables from a JSON file
    in the project's python-secrets environment directory. This is
    a callback invoked by `Config.customize_settings()` in the
    `Settings` class below.
    """
    return json.loads(Path(secrets_file_path).read_text(encoding='utf-8'))


# pylint: disable=no-self-use


class Settings(BaseSettings):
    """
    Class to hold application settings.

    These come from Linux process environment variables and
    the "secrets" file from a python-secrets environment.

    The original code base from which this application was bootstrapped
    used a `.env` file to populate the process environment from which
    the `Settings` class inherits variables and values. Using `.env`
    files in a source code repository directory at runtime while
    developing code is a risky security practice in that secrets may
    be leaked by accident.
    """

    PROJECT_NAME: str = "Tanzanite"
    PROJECT_VERSION: str = get_version()

    SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl
    SERVER_PORT: str

    API_VER: str = DEFAULT_API_VER
    API_PATH: str
    API_BASE_URL: str
    # FIXME - Resolve `API_BASE_URL`` vs. `get_api_base_url()``

    # @validator("API_BASE_URL", pre=True, always=True, allow_reuse=True)
    # def assemble_api_base_url(  # pylint: disable=no-self-argument
    #     cls,
    #     v: Optional[str],
    #     values: Dict[str, Any],
    # ) -> Any:
    #     from tanzanite.utils import get_api_base_url

    #     if isinstance(v, str) and not v == "":
    #         return v
    #     return get_api_base_url(
    #         api_ver=values.get('API_VER'),
    #         port=values.get('SERVER_PORT'),
    #     )

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", \
    # "http://localhost:3000", "http://localhost:8080", \
    # "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True, always=True, allow_reuse=True)
    def assemble_cors_origins(  # pylint: disable=no-self-argument
        cls,
        v: Union[str, List[str]],
    ) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        if isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    SENTRY_DSN: Optional[Union[HttpUrl, str]] = " "

    @validator("SENTRY_DSN", pre=True, always=True, allow_reuse=True)
    def sentry_dsn_can_be_blank(  # pylint: disable=no-self-argument
        cls,
        v: str,
    ) -> Optional[str]:
        if len(v) == 0:
            return None
        return v

    # https://www.postgresql.org/docs/9.3/libpq-pgpass.html
    POSTGRES_SERVER: str = ""
    POSTGRES_PORT: str = ""
    POSTGRES_USER: str = ""
    POSTGRES_PASSWORD: str = ""
    POSTGRES_DB: str = ""
    SQLALCHEMY_DATABASE_DIALECT: str = "sqlite"
    # SQLALCHEMY_DATABASE_URI: Optional[Union[PostgresDsn, SqliteUrl]] = None
    SQLALCHEMY_DATABASE_URI: str = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True, always=True, allow_reuse=True)  # noqa
    def assemble_db_connection(  # pylint: disable=no-self-argument
        cls,
        v: Optional[str],
        values: Dict[str, Any],
    ) -> Any:
        test_ext = '_test' if os.environ.get('TANZANITE_TESTING') else ''
        if (
            v is None
            and values.get("SQLALCHEMY_DATABASE_DIALECT") == "sqlite"
        ):
            return f"sqlite:///{SQLITE_DATABASE_PATH}".replace(
                '.db', f'{test_ext}.db'
            )
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            port=values.get("POSTGRES_PORT"),
            path=f"/{values.get('PGADATABASE') or 'pgdb'}{test_ext}",
        )

    SMTP_TLS: bool = True

    @validator("SMTP_TLS", pre=True, always=True, allow_reuse=True)
    def get_smtp_tls(  # pylint: disable=no-self-argument
        cls,
        v: bool,  # pylint: disable=unused-argument
        values: Dict[str, Any],
    ) -> bool:
        return str(values.get('SMTP_TLS')).lower() == "true"

    SMTP_PORT: Optional[int] = None
    SMTP_HOST: Optional[str] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAILS_FROM_EMAIL: Optional[EmailStr] = None
    EMAILS_FROM_NAME: Optional[str] = None

    # @validator("EMAILS_FROM_NAME", pre=True, always=True, allow_reuse=True)
    def get_project_name(  # pylint: disable=no-self-argument
        cls,
        v: Optional[str],
        values: Dict[str, Any],
    ) -> str:
        if not v:
            return values["PROJECT_NAME"]
        return v

    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48
    EMAIL_TEMPLATES_DIR: str = str(
        Path(__file__).parents[1] / "backend" / "app" / "app" / "email-templates" / "build"  # noqa
    )
    EMAILS_ENABLED: bool = False

    @validator("EMAILS_ENABLED", pre=True, always=True, allow_reuse=True)
    def get_emails_enabled(  # pylint: disable=no-self-argument
        cls,
        v: bool,  # pylint: disable=unused-argument
        values: Dict[str, Any],
    ) -> bool:
        return bool(
            values.get("SMTP_HOST")
            and values.get("SMTP_PORT")
            and values.get("EMAILS_FROM_EMAIL")
        )

    USERS_OPEN_REGISTRATION: bool = False

    @validator("USERS_OPEN_REGISTRATION", pre=True, always=True, allow_reuse=True)  # noqa
    def get_users_open_registration(  # pylint: disable=no-self-argument
        cls,
        v: bool,  # pylint: disable=unused-argument
        values: Dict[str, Any],
    ) -> bool:
        return str(values.get('USERS_OPEN_REGISTRATION')).lower() == "true"

    class Config:
        case_sensitive = True
        env_file_encoding = 'utf-8'
        extra = 'allow'

        @classmethod
        def customise_sources(
            cls,
            init_settings,
            env_settings,
            file_secret_settings,
        ):
            return (
                init_settings,
                json_config_settings_source,
                env_settings,
                file_secret_settings,
            )

# def __init__(self, secrets_environment=None):
#     if secrets_environment is None:
#         secrets_environment = SecretsEnvironment(
#             environment=os.getenv('D2_ENVIRONMENT', None),
#             export_env_vars=True
#         )
#         secrets_environment.requires_environment()
#         secrets_environment.read_secrets_and_descriptions()
#     # Store secrets_environment object directly, just in case.
#     self.secrets_environment = secrets_environment
#     # Create attributes from secrets variables and some method values.
#     for k, v in self.secrets_environment.items():
#         self.__setattr__(k, v)
#     self.__setattr__(
#         'environment_path',
#         self.secrets_environment.environment_path()
#     )
#     return None


settings = Settings()
