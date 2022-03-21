# Author: Snow Yang
# Date  : 2022/03/21

import os
import errno
import pathlib

from mdev import log

def mkdir_p(path):  # type: (str) -> None
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno != errno.EEXIST or not os.path.isdir(path):
            raise

def get_env():  # type: () -> None
    home = str(pathlib.Path.home())
    env_path = os.path.abspath(os.path.join(home, '.mdev'))
    if not os.path.exists(env_path):
        log.inf(f'Directory {env_path} was not found.')
        log.inf(f'Creating {env_path} ...')
        mkdir_p(env_path)
    return env_path