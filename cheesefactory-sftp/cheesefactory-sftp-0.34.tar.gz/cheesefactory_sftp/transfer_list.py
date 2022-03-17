# cheesefactory_sftp/helpers.py

# Non-SFTP functions that can help around the app

from pathlib import Path
from typing import List


class CfSftpTransferList:

    def __init__(self):
        # List of dictionaries in the format [{'src': '<source path>', 'dst': '<destination path>'}, ...]
        self.list: List = []

    #
    # PROPERTIES
    #

    @property
    def dst_list(self) -> List[str]:
        """Return a list of destination files.

        Returns:
            List of dst files.
        """
        dst_list = []
        for file in self.list:
            dst_list.append(file['dst'])

        return dst_list

    @property
    def src_list(self) -> List[str]:
        """Return a list of source files.

        Returns:
            List of src files.
        """
        src_list = []
        for file in self.list:
            src_list.append(file['src'])

        return src_list

    #
    # CLASS METHODS
    #

    @classmethod
    def build_list(cls, base_dst_dir: str = None, base_src_dir: str = None, file_list: List = None,
                   flatten_dst: bool = False, flatten_src: bool = False):
        """Start with a list and return a properly formatted CfSftpTransferList object.

        Used by transfer_by_list(), get_by_list(), put_by_list(). Order of operations: 1) Flatten, 2) Pre-pend base dir.

        Args:
            base_dst_dir: The base directory to use when building the destination path.
            base_src_dir: The base directory to use when building the destination path.
            file_list: A list of files to transfer.
            flatten_dst: Removes parent directories from destination paths
            flatten_src: Removes parent directories from destination paths
        Returns:

        """
        transfers = cls()

        for file in file_list:
            file = str(Path(file))
            transfers.list.append({'dst': file, 'src': file})  # First, make dst and src the same.

        if flatten_dst is True:  # Next, remove parent directorys from the destination, if needed.
            transfers.flatten_dst()
        if flatten_src is True:
            transfers.flatten_src()

        if base_dst_dir is not None:  # Finally, prepend the destination's base directory.
            transfers.add_base_dst_dir(base_dst_dir)
        if base_src_dir is not None:
            transfers.add_base_src_dir(base_src_dir)

        return transfers

    @classmethod
    def import_list(cls, file_list: List[dict] = None):
        """Start with a properly formatted list of dictionaries and return as a CfSftpTransferList object.

        Used by transfer_by_list(), get_by_list(), put_by_list(). Order of operations: 1) Flatten, 2) Pre-pend base dir.

        Args:
            file_list: A list of dictionaries in the format
                       [{'src': '<source path>', 'dst': '<destination path>'}, ...]
        Returns:

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

        transfers = cls()
        transfers.list = file_list

        return transfers

    #
    # PUBLIC METHODS
    #

    def add_base_dst_dir(self, base_dir: str = ''):
        for index, transfer in enumerate(self.list):
            path = f"{Path(base_dir)}{Path('/')}{Path(transfer['dst'])}"
            self.list[index]['dst'] = path

    def add_base_src_dir(self, base_dir: str = ''):
        for index, transfer in enumerate(self.list):
            path = f"{Path(base_dir)}{Path('/')}{Path(transfer['src'])}"
            self.list[index]['src'] = path

    def flatten_dst(self):
        for transfer in self.list:
            transfer['dst'] = str(Path(transfer['dst']).name)

    def flatten_src(self):
        for transfer in self.list:
            transfer['src'] = str(Path(transfer['src']).name)
