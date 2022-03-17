# cheesefactory-sftp/get.py

import logging
from typing import List
from .transfer import CfSftpTransfer

logger = logging.getLogger(__name__)


class CfSftpGet(CfSftpTransfer):
    """GET-related attributes and methods.

    Notes:
        CfSftp --> CfSftpGet ----> CfSftpTransfer --> CfSftpUtilities --> CfSftpConnection
               |-> CfSftpPut ->|
    """
    def __init__(self):
        super().__init__()

    #
    # PUBLIC METHODS
    #

    def get(self, local_path: str = None, log_checksum: bool = False, preserve_mtime: bool = False,
            remote_path: str = None, remove_source: bool = False) -> dict:
        """Download a single remote file from the SFTP server to the local host.

        Args:
            local_path: Local/destination path and filename.
            log_checksum: Calculate file SHA256 checksum and log resulting value.
            preserve_mtime: Keep modification time of source file.
            remote_path: Remote/source path and filename.
            remove_source: Remove the remote source file.

        Returns:
            A log of the transfer.
        """
        log = self.transfer(
            action='GET', local_path=local_path, log_checksum=log_checksum, preserve_mtime=preserve_mtime,
            remote_path=remote_path, remove_source=remove_source
        )
        return log

    def get_by_list(self, log_checksum: bool = False, preserve_mtime: bool = True,
                    file_list: List[dict] = None, remove_source: bool = False) -> List[dict]:
        """Download a list of files from the SFTP server to the local host.

        Args:
            log_checksum: Calculate file SHA256 checksum and log resulting value.
            preserve_mtime: Keep modification time of source file.
            file_list: List of dictionaries in the format [{'src': '<source path>', 'dst': '<destination path>'}, ...]
            remove_source: Remove the remote source file.

        Returns:
            A list of file transfer logs.
        """
        log = self.transfer_by_list(
            action='GET', file_list=file_list, log_checksum=log_checksum, preserve_mtime=preserve_mtime,
            remove_source=remove_source
        )
        return log
