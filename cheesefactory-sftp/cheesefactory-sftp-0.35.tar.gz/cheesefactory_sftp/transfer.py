# cheesefactory-sftp/transfer.py

import hashlib
import logging
import os
from pathlib import Path
from typing import List

from .exceptions import CfSftpBadListValueError
from .log import CfSftpLogTransfer
from .utilities import CfSftpUtilities

logger = logging.getLogger(__name__)


class CfSftpTransfer(CfSftpUtilities):
    """File transfer and logging attributes and methods shared by CfSftpGet() and CfSftpPut().

    Notes:
            CfSftp --> CfSftpGet ----> CfSftpTransfer --> CfSftpUtilities --> CfSftpConnection
                   |-> CfSftpPut ->|
    """
    def __init__(self):
        super().__init__()

        # Counters used for status messages and logging.
        self._new_file_count = 0
        self._new_dir_count = 0
        self._existing_file_count = 0
        self._existing_dir_count = 0
        self._regex_skip_count = 0

    #
    # PROTECTED METHODS
    #

    def transfer(self, action: str = None, local_path: str = None, log_checksum: bool = False,
                 preserve_mtime: bool = False, remote_path: str = None, remove_source: bool = False) -> dict:
        """GET/PUT a single file.

        Args:
            action: GET or PUT
            local_path: Local path, including filename.
            log_checksum: Calculate file SHA256 checksum and log resulting value.
            preserve_mtime: Keep modification time of source file.
            remote_path: Remote path, including filename.
            remove_source: Remove the source file.

        Returns:
            A log of the transfer.

        Notes:
            Paramiko's get() already does a size match check between local and remote file.
        """
        if action not in ('GET', 'PUT'):
            raise ValueError("action != 'GET' or 'PUT'")
        if not isinstance(local_path, str):
            raise ValueError('local_path != str type')
        if not isinstance(preserve_mtime, bool):
            raise ValueError('preserve_mtime != str type')
        if not isinstance(remote_path, str):
            raise ValueError('remote_path != str type')
        if not isinstance(remove_source, bool):
            raise ValueError('remove_source != bool type')

        transfer_log = CfSftpLogTransfer()
        transfer_log.action = action
        transfer_log.action_ok = False
        transfer_log.client = 'CfSftp'
        transfer_log.local_path = local_path
        transfer_log.preserve_mtime = preserve_mtime
        transfer_log.remote_path = remote_path
        transfer_log.remove_source = remove_source
        transfer_log.size_match = True
        transfer_log.size_match_ok = False

        try:
            transfer_log.note = 'Stat source file.'
            if action == 'GET':
                source_file_stats = self.sftp.stat(remote_path)
            else:  # action == 'PUT'
                source_file_stats = os.stat(local_path)
            transfer_log.size = source_file_stats.st_size

            transfer_log.note = 'Ensuring destination dir exists.'
            if action == 'GET':
                destination_dir = Path(local_path).parent
                destination_dir.mkdir(exist_ok=True, parents=True)
            else:  # action == 'PUT'
                destination_dir = str(Path(remote_path).parent)
                try:
                    self.sftp.stat(destination_dir)
                except IOError:  # If remote directory does not exist...
                    try:
                        self.sftp.mkdir(destination_dir)
                    except IOError as e:
                        raise IOError(f'Unable to create remote directory: {destination_dir} ({e})')

            if action == 'GET':
                transfer_log.note = 'Downloading file.'
                self.sftp.get(remotepath=remote_path, localpath=local_path)

            else:  # action == 'PUT'
                transfer_log.note = 'Uploading file.'
                self.sftp.put(remotepath=remote_path, localpath=local_path, confirm=True)  # confirm does filesize stat

            if log_checksum is True:
                transfer_log.sha256_checksum = self.sha256_checksum(local_path)

            transfer_log.action_ok = True
            transfer_log.size_match_ok = True  # TODO: Make sure parmioko does size match for both PUT and GET.

            if preserve_mtime is True:
                transfer_log.note = 'Preserving mtime.'
                transfer_log.preserve_mtime_ok = False
                # Restamp the local file with the appropriate modification time.
                if action == 'GET':
                    os.utime(local_path, (source_file_stats.st_atime, source_file_stats.st_mtime))
                else:  # action == 'PUT'
                    local_path_times = (source_file_stats.st_atime, source_file_stats.st_mtime)
                    self.sftp.utime(remote_path, local_path_times)
                transfer_log.preserve_mtime_ok = True
                # TODO: Add preserve_mtime for PUT

            if remove_source is True:
                transfer_log.note = 'Removing source.'
                transfer_log.remove_source_ok = False
                if action == 'GET':
                    self.remove_file(remote_path)
                else:  # action == 'PUT'
                    Path(local_path).unlink()
                transfer_log.remove_source_ok = True

        except (FileNotFoundError, IOError) as e:
            transfer_log.note = f"{transfer_log.note}; {str(e)}"
            transfer_log.status = 'ERROR'
            raise
        except CfSftpBadListValueError as e:
            logger.error(str(e))
            raise
        else:
            if preserve_mtime is True:
                transfer_log.note = 'preserve_mtime not yet implemented for PUT'
            else:
                transfer_log.note = ''
            transfer_log.status = 'OK'
        finally:
            self.log.transfers.append(transfer_log)  # In case transfer() is being called by transfer_by_list()

        return transfer_log.as_dict()

    def transfer_by_list(self, action: str = None, file_list: List[dict] = None, log_checksum: bool = False,
                         preserve_mtime: bool = False,  remove_source: bool = False) -> List[dict]:
        """GET/PUT a list of files.

        Args:
            action: GET or PUT
            file_list: A list of dicts containing source and destination paths.
                       Ex: [{'src': '<source path>', 'dst': '<destination path>'}, ...]
            log_checksum: Calculate file SHA256 checksum and log resulting value.
            preserve_mtime: Keep modification time of source file.
            file_list: Source path and filename.
            remove_source: Remove the source file.

        Returns:
            List of file transfer logs.
        """
        if not isinstance(file_list, list):
            raise ValueError("file_list != List[dict] type. "
                             "Expecting [{'src': '<source path>', 'dst': '<destination path>'}, ...]")
        for files in file_list:
            if not isinstance(files, dict):
                raise ValueError("file_list needs to contain only dictionaries. "
                                 "Expecting [{'src': '<source path>', 'dst': '<destination path>'}, ...]")
            if 'src' not in files or 'dst' not in files:
                raise ValueError("A dict in the file_list is missing a 'src' or 'dst' key. "
                                 "Expecting [{'src': '<source path>', 'dst': '<destination path>'}, ...]")

        for file in file_list:
            if action == 'GET':
                local_path = file['dst']
                remote_path = file['src']
            else:
                local_path = file['src']
                remote_path = file['dst']

            try:
                self.transfer(action=action, local_path=local_path, log_checksum=log_checksum,
                              preserve_mtime=preserve_mtime, remote_path=remote_path, remove_source=remove_source)
            except FileExistsError as e:
                logger.warning(str(e))

        transfer_log = []
        for transfer in self.log.transfers:
            transfer_log.append(transfer.as_dict())

        return transfer_log

    #
    # PUBLIC METHODS
    #

    @staticmethod
    def sha256_checksum(file_path: str = None) -> str:
        """Calculate SHA256 checksum for a file."""
        blocksize = 65536  # blocksize limits memory usage.
        sha256 = hashlib.sha256()

        with open(file_path, 'rb') as fp:
            for block in iter(lambda: fp.read(blocksize), b''):
                sha256.update(block)
        return sha256.hexdigest()

    @staticmethod
    def transferred_local_files(log: dict) -> List[str]:
        """Get a list of transferred local files (after any renaming)."""
        transferred_files = []
        for transfer in log['sftp_transfers']:
            if transfer['renamed_local_path'] is not None:
                transferred_files.append(transfer['renamed_local_path'])
            else:
                transferred_files.append(transfer['local_path'])
        return transferred_files

    @staticmethod
    def transferred_remote_files(log: dict) -> List[str]:
        """Get a list of transferred remote files (after any renaming)."""
        transferred_files = []
        for transfer in log['sftp_transfers']:
            if transfer['renamed_remote_path'] is not None:
                transferred_files.append(transfer['renamed_remote_path'])
            else:
                transferred_files.append(transfer['remote_path'])
        return transferred_files
