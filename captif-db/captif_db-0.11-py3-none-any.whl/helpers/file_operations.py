from pathlib import Path
from os import listdir, walk


def abs_directory(path):
    if isinstance(path, str):
        path = Path(path)

    path = path.absolute()
    if path.is_dir():
        return path
    return path.parent


def find_file(path, pattern, recursive=True, depth=0, max_depth=5):
    path = abs_directory(path)
    for ff in listdir(path):
        if pattern in ff:
            return path.joinpath(ff)
    if recursive:
        if depth > max_depth:
            return None
        depth += 1
        return find_file(path.parent, pattern, recursive, depth, max_depth)
    return None


def find_files_in(path, pattern):
    matching = []
    for root, dirs, files in walk(path, topdown=True):
        matching += [
            Path(root).joinpath(ff).absolute() for ff in files if pattern in ff
        ]
    return matching
