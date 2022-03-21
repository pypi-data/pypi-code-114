# -*- coding: utf-8 -*-

"""
Tasks related to database creation, initialization, connections, etc.
"""

# Standard imports
import logging
import os
import warnings

from typing import (
    Dict,
    List,
    Union,
)
from pathlib import Path
from urllib.parse import urlparse

# External imports
import alembic

from alembic.config import Config
from fastapi import FastAPI
from sqlalchemy.orm import Session
from sqlalchemy_utils.functions import (
    database_exists,
    drop_database,
)

# Local imports
from tanzanite import TANZANITE_BASE_DIR
from tanzanite.backend.app.app import (
    crud,
    schemas,
)
from tanzanite.backend.app.app.db.session import (
    database,
    SessionLocal,
    URI,
)
from tanzanite.core.config import settings
from tanzanite.utils import set_directory


logger = logging.getLogger(__name__)
TESTING = os.environ.get('TANZANITE_TESTING') is not None
backend_app_dir = Path(TANZANITE_BASE_DIR) / 'backend' / 'app'
config = Config(backend_app_dir / "alembic.ini")
warnings.filterwarnings("ignore", category=DeprecationWarning)


def create_revision(message="initial revision"):
    """
    Generate an `alembic` migration revision script via its API.
    """
    with set_directory(backend_app_dir):
        alembic.command.revision(config, message=message)


def apply_migrations():
    """
    Perform `alembic` database migrations via its API.
    """
    # Ensure that the sqlite3 database file is created as an empty
    # file with the file permissions you want, as otherwise the
    # process umask will not produce the permissions you expect.
    # See: https://stackoverflow.com/questions/28454551/
    #      pdo-sqlite-create-database-default-permissions
    db_file = Path(urlparse(URI).path)
    db_file.touch(mode=0o640, exist_ok=True)
    db_file.chmod(mode=0o640)
    with set_directory(backend_app_dir):
        alembic.command.upgrade(config, "head")


def seed_database(
    db: Session,
    initial_users: Union[List[Dict], None] = None,
) -> None:
    """
    Seed the database.

    Ensures initial users are bootstrapped in the database. This is
    primarily to get an initial superuser created from the
    `tanzanite_admin_user_email` and `tanzanite_admin_password`
    settings, but more than one user can be created initially.

    The first user is always created as a superuser. Any other users
    will initially be normal users and will need permissions set
    explicitly thereafter.
    """
    db_users = crud.user.get_multi(db)
    first_users = len(db_users) < 1
    for i, user in enumerate(initial_users):
        db_user = crud.user.get_by_email(
            db,
            email=user.get('username')
        )
        if not db_user:
            user_in = schemas.UserCreate(
                email=user.get('username'),
                full_name=user.get('full_name', ''),
                password=user.get('password'),
                is_proctor=False,
                is_superuser=True if (first_users and i == 0) else False,
            )
            new_user = crud.user.create(db, obj_in=user_in)
            if new_user is None:
                username = user_in.get('username')
                raise RuntimeError(
                    f"[-] failed to create initial user '{username}'"
                )


def prepare_database(
    initial_users: Union[List[Dict], None] = None,
) -> None:
    """
    Perform all necessary preparation of the database for use.
    This includes creation of the tables using alembic migrations
    and ensuring an initial superuser entry is present to manage
    the system on first startup.

    This same function should be usable by both testing and production
    in order to keep testing as close to production as possible.
    """
    if initial_users is None:
        initial_users = [
            {
                'username': settings.tanzanite_admin_user_email,
                'full_name': 'System Owner',
                'password': settings.tanzanite_admin_password,
            }
        ]
    apply_migrations()
    db = SessionLocal()
    seed_database(db=db, initial_users=initial_users)


def remove_database(engine):
    """
    Completely remove the sqlite3 database file.
    """
    if settings.SQLALCHEMY_DATABASE_DIALECT == 'sqlite':
        if database_exists(engine.url):
            drop_database(engine.url)
            db_file = Path(str(engine.url.database))
            if db_file.exists():
                db_file.unlink()


# https://www.jeffastor.com/blog/testing-fastapi-endpoints-with-docker-and-pytest

# pylint: disable=protected-access
async def connect_to_db(app: FastAPI) -> None:
    """
    Connect to database.
    """
    try:
        await database.connect()
        await database.execute("SELECT 1")
        app.state._db = database
        logger.debug("[+] database connected")
    except Exception as err:
        logger.warning("[!] DATABASE CONNECTION ERROR: %s", str(err))
        raise
# pylint: enable=protected-access


# pylint: disable=protected-access
async def close_db_connection(app: FastAPI) -> None:
    """
    Disconnect from database.
    """
    try:
        if app.state._db.is_connected:
            await app.state._db.disconnect()
        logger.debug("[+] database disconnected")
    except Exception as err:
        logger.warning("[!] DATABASE DISCONNECT FAILURE: %s", str(err))
        raise
# pylint: enable=protected-access


# async def create_user_direct(
#     username: str,
#     shell_login: str,
#     password: str,
#     is_superuser: bool = False,
#     is_verified: bool = False,
# ):
#     """Create a user entry directly rather than through API."""
#     try:
#         async with get_user_db_context() as user_db:
#             async with get_user_manager_context(user_db) as user_manager:
#                 user = await user_manager.create(
#                     UserCreate(
#                         email=username,
#                         shell_login=shell_login,
#                         password=password,
#                         is_superuser=is_superuser,
#                         is_verified=is_verified,
#                     )
#                 )
#                 logger.debug("[+] created user '%s'", user)
#     except UserAlreadyExists:
#         sys.exit(f"[-] user '{username}'' already exists")


# vim: set ts=4 sw=4 tw=0 et :
