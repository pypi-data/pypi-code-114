# cheesefactory-sftp/put.py

import logging
from typing import List
from .transfer import CfSftpTransfer

logger = logging.getLogger(__name__)


class CfSftpPut(CfSftpTransfer):
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

    def put(self, local_path: str = None, log_checksum: bool = False, preserve_mtime: bool = True,
            remote_path: str = None, remove_source: bool = False) -> dict:
        """Upload a single file from the local host to the SFTP server.

        Args:
            local_path: Local/source path and filename.
            log_checksum: Calculate file SHA256 checksum and log resulting value.
            preserve_mtime: Keep modification time of source file.
            remote_path: Remote/destination path and filename.
            remove_source: Remove the local source file.

        Returns:
            A log of the transfer.
        """
        log = self.transfer(
            action='PUT', local_path=local_path, log_checksum=log_checksum, preserve_mtime=preserve_mtime,
            remote_path=remote_path, remove_source=remove_source
        )
        return log

    def put_by_list(self, log_checksum: bool = False, preserve_mtime: bool = True,
                    file_list: List[dict] = None, remove_source: bool = False) -> List[dict]:
        """Upload a list of files from the local host to the SFTP server.

        Args:
            log_checksum: Calculate file SHA256 checksum and log resulting value.
            file_list: Local/source path and filename.
            preserve_mtime: Keep modification time of source file.
            remove_source: Remove the local source file.

        Returns:
            A list of file transfer logs.
        """
        log = self.transfer_by_list(
            action='PUT', file_list=file_list, log_checksum=log_checksum, preserve_mtime=preserve_mtime,
            remove_source=remove_source
        )
        return log
