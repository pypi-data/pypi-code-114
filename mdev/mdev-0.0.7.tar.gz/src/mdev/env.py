# Author: Snow Yang
# Date  : 2022/03/21

import os
import sys
import stat
import errno
import pathlib
import shutil
import requests
import tarfile
import zipfile

from mdev import log

'''
URL example:
https://code.aliyun.com/mxos/toolchain/raw/master/build/cmake-macos.tar.gz
https://code.aliyun.com/mxos/toolchain/raw/master/build/ninja-mac.zip
'''

url_common_header = 'https://code.aliyun.com/mxos/toolchain/raw/master/build/'

user_home = str(pathlib.Path.home())
env_root = os.path.abspath(os.path.join(user_home, '.mdev'))
build_root = os.path.join(env_root, 'build')
cmake_exe = os.path.join(build_root, 'CMake.app', 'Contents', 'bin', 'cmake')
ninja_exe = os.path.join(build_root, 'ninja')

def mkdir_p(path):  # type: (str) -> None
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno != errno.EEXIST or not os.path.isdir(path):
            raise

def add_execute_permission(exe):
    st = os.stat(exe)
    os.chmod(exe, st.st_mode | stat.S_IEXEC)

def check_and_download(exe, zip, name):
    exe_zip = os.path.join(build_root, zip)
    if not os.path.exists(exe):
        log.inf(f'{name} was not found.')
        if not os.path.exists(exe_zip):
            download(f'{url_common_header}{zip}', exe_zip)
        extract(exe_zip)
        os.remove(exe_zip)
        add_execute_permission(exe)

def get_env():  # type: () -> None
    # Create env directory
    if not os.path.exists(env_root):
        log.inf(f'Directory {env_root} was not found.')
        log.inf(f'Creating {env_root} ...')
        mkdir_p(env_root)
        
    # Create build tools directory
    if not os.path.exists(build_root):
        log.inf(f'Directory {build_root} was not found.')
        log.inf(f'Creating {build_root} ...')
        os.makedirs(build_root)
    
    check_and_download(cmake_exe, 'cmake-mac.zip', 'CMake')
    check_and_download(ninja_exe, 'ninja-mac.zip', 'Ninja')

    return env_root

def get_cmake():
    return cmake_exe

def get_ninja():
    return ninja_exe

def download(url, destination): # type: (str, str) -> None
    print(f'Downloading {url} to {os.path.dirname(destination)} ...', flush=True)
    with requests.get(url, stream=True) as r:
        with open(destination, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

def extract(filename, destination=None):  # type: (str, str) -> None
    if destination == None:
        destination = os.path.dirname(filename)
    print(f'Extracting {filename} to {destination} ...', flush=True)
    if filename.endswith(('.tar.gz', '.tgz')):
        archive_obj = tarfile.open(filename, 'r:gz')
    elif filename.endswith(('.tar.xz')):
        archive_obj = tarfile.open(filename, 'r:xz')
    elif filename.endswith(('.tar.bz2')):
        archive_obj = tarfile.open(filename, 'r:bz2')    
    elif filename.endswith('zip'):
        archive_obj = zipfile.ZipFile(filename)
    else:
        raise NotImplementedError('Unsupported archive type')
    if sys.version_info.major == 2:
        # This is a workaround for the issue that unicode destination is not handled:
        # https://bugs.python.org/issue17153
        destination = str(destination)
    archive_obj.extractall(destination)
