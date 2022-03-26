import os
import shutil
import subprocess
import sys
from typing import Literal, List
import glob
from tooly.types import Encoding

defaultShellEncoding: Encoding = 'utf8'
if sys.platform.find('win'):
    defaultShellEncoding = 'gbk'


def ls(path: str = '.') -> List[str]:
    """
    ls文件或者文件夹(支持通配符，例如 ls("*.py"))
    :return: 文件或文件夹列表
    """

    # 如果是文件夹，则直接返回
    if isDir(path):
        return os.listdir(path)

    # 是文件或者glob格式
    ret = glob.glob(path, recursive=False)
    return [os.path.normpath(i) for i in ret]


def writeText(fname: str, *contents: str, encoding: Encoding = "utf8"):
    mode = 'w'
    with open(fname, mode, encoding=encoding) as fd:
        for content in contents:
            fd.write(content)


def appendText(fname: str, *content: str, encoding: Encoding = 'utf8'):
    with open(fname, 'a+', encoding=encoding) as fd:
        for c in content:
            fd.write(c)


def readAsBytes(fname: str) -> bytes:
    with open(fname, 'rb') as fd:
        return fd.read()


def fileStatus(fname: str) -> Literal["file", "dir", "notExists", "other"]:
    if not os.path.exists(fname):
        return "notExists"
    if os.path.isfile(fname):
        return "file"
    if os.path.isdir(fname):
        return "dir"
    return "other"


def cat(fname: str, encoding: Encoding = "utf8") -> str:
    with open(fname, 'r', encoding=encoding) as fd:
        return fd.read()


def exec(cmd: str, encoding: Encoding = defaultShellEncoding):
    """
    执行命令，并将命令结果返回
    :param cmd:
    :param encoding:
    :return:
    """
    return subprocess.check_output(cmd, shell=True, encoding=encoding)


def mkdir(dirName: str, exist_ok=True):
    """
    创建文件夹，如果中间文件夹不存在则自动创建
    """
    os.makedirs(dirName, exist_ok=exist_ok)


def isDir(dirName: str) -> bool:
    return os.path.isdir(dirName)


def rm(fname: str):
    """
    删除文件或文件夹（支持shell文件名的通配符）
    """
    files = glob.glob(fname)
    for f in files:
        status = fileStatus(f)
        if status == "file":
            os.remove(f)
        else:
            shutil.rmtree(f, True)


def touch(fname: str):
    """
    创建一个空文件，如果文件夹的路径不存在则创建之
    :param fname:
    :return:
    """
    mkdir(os.path.dirname(fname))
    writeText(fname, "")


def move(src: str, dst: str):
    """
    移动文件或文件夹.
    函数行为跟linux下的mv命令类似
    如果dst是一个已经存在的文件夹，则将src移动到dst目录下，否则将src移动到dst的位置
    """
    for f in glob.glob(src):
        shutil.move(f, dst)


def pwd() -> str:
    """
    打印当前路径
    :return:
    """
    return os.getcwd()


def cd(path: str):
    os.chdir(path)


if __name__ == '__main__':
    # print(ls("*.py"))
    # touch("a/b/c.txt")
    # move("a/*.txt","a/b")
    # rm("a/b/*.txt")
    # print(ls("a/b/"))
    # rm("a")
    print(ls("a/b/"))
