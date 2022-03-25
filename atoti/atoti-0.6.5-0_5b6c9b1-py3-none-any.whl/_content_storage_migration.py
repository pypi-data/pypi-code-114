from __future__ import annotations

import logging
from pathlib import Path
from shutil import copy2
from subprocess import STDOUT, CalledProcessError, check_output  # nosec
from tempfile import TemporaryDirectory
from typing import Optional

from ._get_java_executable_path import get_java_executable_path
from ._server_subprocess import H2_MIGRATION_JAR_PATH, JAR_PATH


def is_h2_v1_error(traceback: str, *, driver: Optional[str]) -> bool:
    return (
        "org.h2.mvstore.MVStoreException: The write format 1 is smaller than the supported format 2 [2.1.210/5]"
        in traceback
        and driver == "org.h2.Driver"
    )


def _convert_user_content_storage_to_sql_script(
    *,
    java_executable_path: Path,
    sql_script_path: Path,
    user_content_storage_url: str,
) -> None:
    try:
        check_output(
            [
                str(java_executable_path),
                "-jar",
                str(H2_MIGRATION_JAR_PATH),
                user_content_storage_url,
                str(sql_script_path),
            ],
            stderr=STDOUT,
            text=True,
        )
    except CalledProcessError as error:
        raise RuntimeError(
            "Could not convert user content storage to SQL script."
        ) from error


def _create_user_content_storage_from_sql_script(
    *,
    java_executable_path: Path,
    sql_script_path: Path,
    user_content_storage_url: str,
) -> None:
    try:
        check_output(
            [
                str(java_executable_path),
                "-jar",
                str(JAR_PATH),
                "--migrate-user-content-storage",
                user_content_storage_url,
                str(sql_script_path),
            ],
            stderr=STDOUT,
            text=True,
        )
    except CalledProcessError as error:
        raise RuntimeError(
            "Could not create user content storage from SQL script."
        ) from error


def _backup_user_content_storage(
    user_content_storage_database_path: Path, *, session_directory: Path
) -> None:
    copy2(user_content_storage_database_path, session_directory)
    logging.getLogger("atoti.session").warning(
        "Backing up existing user content storage before migration to %s.",
        str(session_directory),
    )


def migrate_user_content_storage(
    user_content_storage_url: str, *, session_directory: Path
) -> None:
    java_executable_path = get_java_executable_path()
    user_content_storage_database_path = Path(
        f"{user_content_storage_url.replace('jdbc:h2:file:', '')}.mv.db"
    )

    with TemporaryDirectory() as directory:
        sql_script_path = Path(directory) / "h2_migration.zip"

        _backup_user_content_storage(
            user_content_storage_database_path,
            session_directory=session_directory,
        )
        _convert_user_content_storage_to_sql_script(
            java_executable_path=java_executable_path,
            sql_script_path=sql_script_path,
            user_content_storage_url=user_content_storage_url,
        )
        user_content_storage_database_path.unlink()
        _create_user_content_storage_from_sql_script(
            java_executable_path=java_executable_path,
            sql_script_path=sql_script_path,
            user_content_storage_url=user_content_storage_url,
        )
