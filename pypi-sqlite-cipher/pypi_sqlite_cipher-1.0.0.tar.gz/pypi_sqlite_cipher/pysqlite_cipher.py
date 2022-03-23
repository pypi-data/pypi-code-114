"""
#### 加密
sqlcipher-shell64.exe client.db
ATTACH DATABASE 'encrypted.db' AS encrypted KEY 'thisiskey';
SELECT sqlcipher_export('encrypted');
.quit

#### 解密
PRAGMA key = 'thisiskey';
ATTACH DATABASE 'plaintext.db' AS plaintext;
SELECT sqlcipher_export('plaintext');
DETACH DATABASE plaintext;
"""
import os
import sys
from subprocess import Popen, PIPE

exe_file = os.path.dirname(sys.executable) + "\\Lib\\site-packages\\pypi_sqlite_cipher\\sqlcipher-shell64.exe"


def encryption_sqlite_file(db_file="", secret_key=""):
    """
    :param db_file: 将要加密的原始文件
    :param secret_key: 连接数据库文件的密钥
    :return:
    """
    if not db_file:
        raise ValueError("db_File is not defined！")
    if not secret_key:
        secret_key = "encrypted"
    exe_cmd = "%s %s" % (exe_file, db_file)
    p1 = Popen(exe_cmd, stdout=PIPE, stdin=PIPE, stderr=PIPE, shell=True)
    cmd_sql = "ATTACH DATABASE 'encrypted.db' AS encrypted KEY '%s'; SELECT sqlcipher_export('encrypted');" % secret_key
    code, message = p1.communicate(bytes(cmd_sql, encoding='utf-8'))
    message = message.decode("gbk")
    if int(p1.poll()) == 0:
        return "success", p1.poll(), code, message
    else:
        return "fail", p1.poll(), code, message


def decrypt_sqlite_file(db_file="", secret_key=""):
    """
    :param db_file:  将要解密的数据库文件
    :param secret_key: 连接数据库的密钥 (要与加密的密钥一致)
    :return:
    """
    if not db_file:
        raise ValueError("db_File is not defined！")

    if not secret_key:
        raise ValueError("secret_key is not defined！")
    exe_cmd = "%s %s" % (exe_file, db_file)
    p2 = Popen(exe_cmd, stdout=PIPE, stdin=PIPE, stderr=PIPE, shell=True)
    cmd_sql = "PRAGMA key = '%s'; ATTACH DATABASE 'plaintext.db' AS plaintext; SELECT sqlcipher_export('plaintext'); DETACH DATABASE plaintext;" % secret_key
    code, message = p2.communicate(bytes(cmd_sql, encoding='utf-8'))
    message = message.decode("gbk")
    if int(p2.poll()) == 0:
        return "success", p2.poll(), code, message
    else:
        return "fail", p2.poll(), code, message
