# Copyright 2020 Karlsruhe Institute of Technology
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from contextlib import contextmanager

from flask import current_app
from flask import send_file
from flask_login import current_user
from sqlalchemy.exc import IntegrityError
from zipstream import ZipStream

from .models import File
from .models import Record
from .models import Upload
from kadi.ext.db import db
from kadi.lib.db import aquire_lock
from kadi.lib.db import escape_like
from kadi.lib.db import update_object
from kadi.lib.revisions.core import create_revision as _create_revision
from kadi.lib.revisions.core import delete_revisions
from kadi.lib.storage.local import create_default_local_storage
from kadi.lib.utils import is_iterable
from kadi.lib.utils import signal_resource_change
from kadi.lib.validation import validate_mimetype
from kadi.modules.permissions.core import get_permitted_objects
from kadi.plugins import run_hook


def aquire_file_lock(file):
    """Aquire a lock on the given file and refresh it.

    Only relevant for local files, as locks are used for updating existing local files'
    data in a consistent manner.

    :param file: The file to aquire a lock from.
    :return: The refreshed file.
    """
    if file.storage_type != "local":
        return file

    return aquire_lock(file)


def update_file(file, **kwargs):
    r"""Update an existing file.

    Note that this function aquires a lock on the given file and issues a database
    commit or rollback.

    :param file: The file to update.
    :param \**kwargs: Keyword arguments that will be passed to
        :func:`kadi.lib.db.update_object`.
    :return: ``True`` if the file was updated successfully, ``False`` otherwise.
    """
    file = aquire_file_lock(file)

    if file.state != "active" or file.record.state != "active":
        return False

    update_object(file, **kwargs)

    update_timestamp = False
    if db.session.is_modified(file):
        update_timestamp = True

    try:
        db.session.flush()
    except IntegrityError:
        db.session.rollback()
        return False

    revision_created = _create_revision(file)

    # Only update the timestamp of the record if the file actually changed.
    if update_timestamp:
        file.record.update_timestamp()

    # Releases the file lock as well.
    db.session.commit()

    if revision_created:
        signal_resource_change(file)

    return True


def delete_file(file, create_revision=True, revision_user=None):
    """Delete an existing file.

    This will mark the file for deletion, i.e. the file's state will be set to
    ``"inactive"``. Note that this function aquires a lock on the given file and issues
    one or more database commits.

    :param file: The file to delete.
    :param create_revision: (optional) Flag indicating whether a revision should be
        created for the deletion.
    :param revision_user: (optional) The user that triggered the file deletion revision.
        Defaults to the current user.
    """
    from .uploads import delete_upload

    revision_user = revision_user if revision_user is not None else current_user

    file = aquire_file_lock(file)
    file.state = "inactive"

    update_timestamp = False
    if db.session.is_modified(file):
        update_timestamp = True

    revision_created = False
    if create_revision:
        revision_created = _create_revision(file, user=revision_user)

    if update_timestamp:
        file.record.update_timestamp()

    # Check if there are any uploads attached to the file and mark them for deletion as
    # well.
    uploads = Upload.query.filter(Upload.file_id == file.id)
    for upload in uploads:
        delete_upload(upload)

    # Releases the file lock as well.
    db.session.commit()

    if revision_created:
        signal_resource_change(file, user=revision_user)


def remove_files(files, delete_from_db=True):
    """Remove multiple files from storage.

    Note that this function may issue one or more database commits.

    :param files: A single :class:`.File` or an iterable of files.
    :param delete_from_db: (optional) A flag indicating whether the file should be
        deleted from the database as well, instead of just doing a soft deletion (i.e.
        setting the file's state to ``"deleted"``).
    """
    from .uploads import remove_uploads

    if not is_iterable(files):
        files = [files]

    for file in files:
        delete_file(file, create_revision=False)

        storage = file.storage
        filepath = storage.create_filepath(str(file.id))

        if filepath is not None:
            storage.delete(filepath)

            if file.storage_type == "local":
                # Check if there are any uploads attached to the file and remove them as
                # well.
                uploads = Upload.query.filter(Upload.file_id == file.id)
                remove_uploads(uploads)

                storage.remove_empty_parent_dirs(filepath)

            if delete_from_db:
                delete_revisions(file)
                db.session.delete(file)
            else:
                file.state = "deleted"

        db.session.commit()


@contextmanager
def open_file(file, mode="rb", encoding=None):
    """Context manager that yields an open file.

    Note that this context manager yields ``None`` if the file has an incompatible
    storage type.

    **Example:**

    .. code-block:: python3

        with open_file(file) as file_object:
            pass

    :param file: The :class:`.File` to open.
    :param mode: (optional) The mode to open the file with.
    :param encoding: (optional) The encoding of the file if opening it in text mode.
    """
    storage = file.storage
    filepath = storage.create_filepath(str(file.id))

    if filepath is None:
        yield None
        return

    f = storage.open(filepath, mode=mode, encoding=encoding)

    try:
        yield f
    finally:
        storage.close(f)


def download_file(file):
    """Send a file to a client for downloading.

    :param file: The :class:`.File` to download.
    :return: The response object or ``None`` if the given file could not be found or has
        an incompatible storage type.
    """
    storage = file.storage
    filepath = storage.create_filepath(str(file.id))

    if filepath is None or not storage.exists(filepath):
        return None

    # Passing a file path instead of an already opened file is required to use
    # "X-Sendfile", which will probably require special handling for different storages
    # in the future. Furthermore, the "conditional" flag seems to be only necessary when
    # using the dev server to support range responses, otherwise the web server handles
    # that via "X-Sendfile".
    return send_file(
        filepath,
        mimetype=file.mimetype,
        download_name=file.name,
        as_attachment=True,
        etag=False,
        conditional=current_app.env == "development",
    )


def stream_files(record):
    """Stream all files of a record to a client as ZIP archive for downloading.

    :param record: The record the files belong to.
    :return: The response object.
    """
    zip_stream = ZipStream(sized=True)

    for file in record.active_files:
        filepath = file.storage.create_filepath(str(file.id))

        if filepath is not None:
            zip_stream.add_path(filepath, arcname=file.name)

    # Manually build the response to include the correct "Content-Length" header.
    headers = {
        "Cache-Control": "no-cache, max-age=0",
        "Content-Disposition": f"attachment; filename={record.identifier}.zip",
        "Content-Length": len(zip_stream),
    }
    return current_app.response_class(
        zip_stream, mimetype="application/zip", headers=headers
    )


def get_custom_mimetype(file, base_mimetype=None):
    """Get a custom MIME type of a file based on its content.

    Uses the ``"kadi_get_custom_mimetype"`` plugin hook for custom MIME types based on
    the file's content.

    :param file: The file to get the MIME type of.
    :param base_mimetype: (optional) The base MIME type of the file on which to base the
        custom MIME type.
    :return: The custom MIME type or ``None`` if no valid custom MIME type was found.
    """
    if base_mimetype is None:
        storage = file.storage
        filepath = storage.create_filepath(str(file.id))

        if filepath is not None:
            base_mimetype = storage.get_mimetype(filepath)

    try:
        custom_mimetype = run_hook(
            "kadi_get_custom_mimetype", file=file, base_mimetype=base_mimetype
        )
        if custom_mimetype is None:
            return None

        validate_mimetype(custom_mimetype)

    except Exception as e:
        current_app.logger.exception(e)
        return None

    return custom_mimetype


def get_permitted_files(filter_term="", user=None):
    """Convenience function to get all record files that a user can access.

    In this context having access to a file means having read permission for the record
    the file belongs to.

    :param filter_term: (optional) A (case insensitive) term to filter the files by
        their name or record identifier.
    :param user: (optional) The user to check for access permissions. Defaults to the
        current user.
    :return: The permitted file objects as query.
    """
    user = user if user is not None else current_user

    record_ids_query = (
        get_permitted_objects(user, "read", "record")
        .filter(Record.state == "active")
        .with_entities(Record.id)
    )

    files_query = File.query.join(Record).filter(
        File.state == "active",
        Record.id.in_(record_ids_query),
        db.or_(
            File.name.ilike(f"%{escape_like(filter_term)}%"),
            Record.identifier.ilike(f"%{escape_like(filter_term)}%"),
        ),
    )

    return files_query


def download_temporary_file(temporary_file):
    """Send a temporary file to a client as attachment for download.

    :param temporary_file: The :class:`.TemporaryFile` to download.
    :return: The response object or ``None`` if the given temporary file could not be
        found.
    """
    storage = create_default_local_storage()
    filepath = storage.create_filepath(str(temporary_file.id))

    if not storage.exists(filepath):
        return None

    return send_file(
        storage.open(filepath),
        mimetype=temporary_file.mimetype,
        download_name=temporary_file.name,
        as_attachment=True,
        etag=False,
    )


def remove_temporary_files(temporary_files):
    """Remove multiple temporary files from storage.

    Note that this function may issue one or more database commits.

    :param temporary_files: A single :class:`.TemporaryFile` or an iterable of temporary
        files.
    """
    if not is_iterable(temporary_files):
        temporary_files = [temporary_files]

    for temporary_file in temporary_files:
        temporary_file.state = "inactive"
        db.session.commit()

        storage = create_default_local_storage()
        filepath = storage.create_filepath(str(temporary_file.id))

        storage.delete(filepath)
        storage.remove_empty_parent_dirs(filepath)

        db.session.delete(temporary_file)
        db.session.commit()
