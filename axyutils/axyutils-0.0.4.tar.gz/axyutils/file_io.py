'''
File I/O utility functions.

XXX deep alpha

:copyright: Copyright 2022 AXY axy@declassed.art
:license: BSD, see LICENSE for details.
'''

import errno
import fcntl
import gzip
import os
import stat
import sys
from tempfile import NamedTemporaryFile

def atomic_write(content, filename, encoding=None):
    '''
    Write content to a temporary file and then rename so it appears atomically in the file system.
    '''
    mode = 'w'
    if not encoding:
        mode += 'b'
    dest_dir = os.path.dirname(filename)
    os.makedirs(dest_dir, exist_ok=True)
    with NamedTemporaryFile(mode=mode, encoding=encoding, dir=dest_dir, delete=False) as f:
        f.write(content)
        temp_filename = f.name
    _set_file_permissions(temp_filename)
    os.rename(temp_filename, filename)

def atomic_copy(src_filename, dest_filename):
    '''
    Copy file to a temporary file and then rename so it appears atomically in the file system.
    '''
    with open(src_filename, 'rb') as src_fileobj:
        dest_dir = os.path.dirname(filename)
        os.makedirs(dest_dir, exist_ok=True)
        with NamedTemporaryFile(mode='wb', dir=dest_dir, delete=False) as dest_fileobj:
            temp_filename = dest_fileobj.name
            while True:
                content = src_fileobj.read(8192)
                dest_fileobj.write(content)
                if len(content) < 8192:
                    break
    _set_file_permissions(temp_filename)
    os.rename(temp_filename, dest_filename)

def _set_file_permissions(filename):
    '''
    Helper function to set file permissions to 664.
    '''
    os.chmod(filename, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH)

def atomic_write_with_gz(content, filename, encoding=None):
    '''
    Write content to file and compressed content to .gz file.
    This is a helper to generate statically served content.
    '''
    atomic_write(content, filename, encoding=encoding)
    filename += '.gz'
    if encoding:
        content = content.encode(encoding)
    content = gzip.compress(content)
    atomic_write(content, filename)

def lock_file(fileobj, timeout=None):
    '''
    Lock file.
    If the file is opened for reading, use shared lock.
    If the file is opened for writing, use exclusive lock.
    '''

    class LockContext:

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, exc_tb):
            unlock_file(fileobj)

    lock_type = fcntl.LOCK_EX if fileobj.writable() else fcntl.LOCK_SH
    delay = 0.01
    attempt = 1
    while True:
        try:
            fcntl.lockf(fileobj.fileno(), lock_type | fcntl.LOCK_NB)
            break
        except IOError as e:
            if e.errno == errno.EWOULDBLOCK:
                # already locked
                pass
            raise

        if timeout is not None and attempt > timeout / delay:
            raise TimeoutError()

        if attempt < sys.maxsize:
            attempt += 1

        time.sleep(delay)

    return LockContext()

def unlock_file(fileobj):
    '''
    Unlock file.
    '''
    fcntl.lockf(fileobj.fileno(), fcntl.LOCK_UN)
