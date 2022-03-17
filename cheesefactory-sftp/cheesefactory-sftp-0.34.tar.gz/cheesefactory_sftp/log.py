# log.py

import logging
from typing import List, Optional

logger = logging.getLogger(__name__)


class CfSftpLog:
    def __init__(self):
        """Log structure"""
        self.connection_ok: Optional[bool] = None
        self.host: Optional[str] = None
        self.note: Optional[str] = None
        self.password: Optional[str] = None
        self.port: Optional[str] = None
        self.transfers: List[CfSftpLogTransfer] = []
        self.user: Optional[str] = None
        
    def as_dict(self) -> dict:
        """Get log contents.
        
        Returns:
             Log contents.
        """
        return {
            'connection_ok': self.connection_ok,
            'host': self.host,
            'note': self.note,
            'password': self.password,
            'port': self.port,
            'transfers': [transfer.as_dict() for transfer in self.transfers],
            'user': self.user
        }

    def as_string(self) -> str:
        return str(self.as_dict())
        
    def __repr__(self):
        return self.as_string()


class CfSftpLogTransfer:
    def __init__(self):
        """Transfer log structure"""
        self.action: Optional[str] = None
        self.action_ok: Optional[bool] = None
        self.client: Optional[str] = None
        self.local_path: Optional[str] = None
        self.note: Optional[str] = None
        self.preserve_mtime: Optional[bool] = None
        self.preserve_mtime_ok: Optional[bool] = None
        self.remote_path: Optional[str] = None
        self.remove_source: Optional[str] = None
        self.remove_source_ok: Optional[bool] = None
        self.sha256_checksum: Optional[str] = None
        self.size: Optional[int] = None
        self.size_match: Optional[bool] = None
        self.size_match_ok: Optional[bool] = None
        self.status: Optional[str] = None
        
    def as_dict(self):
        """Get log contents.
        
        Returns:
             Log contents.
        """
        return {
            'action': self.action,
            'action_ok': self.action_ok,
            'client': self.client,
            'local_path': self.local_path,
            'note': self.note,
            'preserve_mtime': self.preserve_mtime,
            'preserve_mtime_ok': self.preserve_mtime_ok,
            'remote_path': self.remote_path,
            'remove_source': self.remove_source,
            'remove_source_ok': self.remove_source_ok,
            'sha256_checksum': self.sha256_checksum,
            'size': self.size,
            'size_match': self.size_match,
            'size_match_ok': self.size_match_ok,
            'status': self.status,
        }

    def as_string(self) -> str:
        return str(self.as_dict())

    def __repr__(self):
        return self.as_string()
        