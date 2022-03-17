# cheesefactory-sftp/exceptions.py

from typing import Union


class CfSftpError(Exception):
    def __init__(self, message: str = None):
        """Generic CfSFTP exception.

        Args:
            message: Error message.
        """
        super().__init__(message)


class CfSftpBadListValueError(CfSftpError):
    def __init__(self, message: str):
        """Exception raised when a bad value is given in a list.

        Args:
            message: Error message.
        """
        super().__init__(message)


class CfSftpEmptyListError(CfSftpError):
    def __init__(self, function_name: str, variable_name: str):
        """Exception raised when a list of paths is empty.

        Args:
            function_name: Path of local file.
            variable_name: Size of local file.
        """
        message = f'Path list is empty. Function: {function_name}, Variable: {variable_name}'
        super().__init__(message)


class CfSftpFileSizeMismatchError(CfSftpError):
    def __init__(self, local_path: str, local_size: str, remote_path: str, remote_size: Union[int, str]):
        """Exception raised when source and destination files do not match.

        Args:
            local_path: Path of local file.
            local_size: Size of local file.
            remote_path: Path of remote file.
            remote_size: Size of remote file.
        """
        message = f'Size mismatch -- Local: {local_path} ({local_size}) != Remote: {remote_path} ({str(remote_size)})'
        super().__init__(message)


class CfSftpInternalValueError(CfSftpError):
    def __init__(self, message: str):
        """A bad value is given in a list.

        Args:
            message: Error message.
        """
        super().__init__(message)
