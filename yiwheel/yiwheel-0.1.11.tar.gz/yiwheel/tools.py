import os
import hashlib


def get_file_md5(filename: str) -> str:
    """获取一个文件的 md5 值"""
    if not os.path.isfile(filename):
        return ''
    my_hash = hashlib.md5()
    f = open(filename, 'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        my_hash.update(b)
    f.close()
    return my_hash.hexdigest()
