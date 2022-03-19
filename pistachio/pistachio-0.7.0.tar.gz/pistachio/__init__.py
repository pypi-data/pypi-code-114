"""
Pistachio aims to simplify reoccurring tasks when working with the file system.
"""

__version__ = "0.7.0"


from dataclasses import dataclass
from pathlib import Path


import errno
import hashlib
import os
import shutil


# Classes ---------------------------------------------------------------------
@dataclass
class Pistachio:
    path: str
    exists: bool
    is_directory: bool
    is_file: bool
    is_symlink: bool
    name: str
    stem: str
    suffix: str


@dataclass
class Tree:
    path: str
    results: list


# Public ----------------------------------------------------------------------
def cp(source_path_str, target_path_str):
    """
    Method to copy and paste a resource from one location to another.
    """
    if is_directory(source_path_str):
        shutil.copytree(
            source_path_str,
            target_path_str,
            symlinks=True,
            copy_function=shutil.copy
        )

    if is_file(source_path_str):
        shutil.copy(
            source_path_str,
            target_path_str
        )

    if is_symlink(source_path_str):
        Path(target_path_str).symlink_to(os.readlink(source_path_str))

    return exists(target_path_str)


def describe(path_str):
    """
    Method to describe the type of resources.
    """
    return Pistachio(
        path=path_str,
        exists=exists(path_str),
        is_directory=is_directory(path_str),
        is_file=is_file(path_str),
        is_symlink=is_symlink(path_str),
        name=name(path_str),
        stem=stem(path_str),
        suffix=suffix(path_str)
    )


def exists(path_str):
    """
    Method to return True or False whether a resource exists.
    """
    if is_symlink(path_str):
        return True
    else:
        return Path(path_str).exists()


def get_md5_hash(path_str):
    """
    Method to return the MD5 hash of a file.
    """
    if exists(path_str) is True and is_file(path_str) is True:
        md5_hash = hashlib.md5()
        with open(path_str, "rb") as fh:
            for block in iter(lambda: fh.read(4096), b""):
                md5_hash.update(block)
            fh.close()
        return md5_hash.hexdigest()
    else:
        return None


def is_directory(path_str):
    """
    Method to return True or False whether a resource is a directory.
    """
    return Path(path_str).is_dir()


def is_file(path_str):
    """
    Method to return True or False whether a resource is a file.
    """
    return Path(path_str).is_file()


def is_symlink(path_str):
    """
    Method to return True or False whether a resource is a symbolic link.
    """
    return Path(path_str).is_symlink()


def ln(link_path_str, source_path_str):
    """
    Method to make a Symbolic Link.
    """
    Path(link_path_str).symlink_to(source_path_str)

    return exists(link_path_str)


def mkdir(path_str):
    """
    Method to create a new directory or directories recursively.
    """
    return Path(path_str).mkdir(parents=True, exist_ok=True)


def mv(source_path_str, target_path_str):
    """
    Method to move a resource from one location to another.
    """
    shutil.move(source_path_str, target_path_str)

    return exists(target_path_str)


def name(path_str):
    """
    Method to return the name of a resource.
    """
    return os.path.basename(path_str)


def path_builder(type, root, *args):
    """
    Method to build a clear relative or absolute path to a resource.
    """
    if type in ["abs", "rel"]:
        if type == "rel":
            return os.path.normpath("/".join(args))
        else:
            return os.path.join(
                root,
                os.path.normpath("/".join(args))
            )
    else:
        raise ValueError(
            """{type} but be 'abs' or 'rel'."""
        )


def stem(path_str):
    """
    Return the stem of the last item in the path.
    """
    return Path(path_str).stem


def suffix(path_str):
    """
    Return the file extension suffix of the last item in the path.
    """
    suffix = Path(path_str).suffix

    clean = [
        (".", "")
    ]

    for old, new in clean:
        suffix = suffix.replace(old, new)

    return suffix if suffix != '' else None


def touch(path_str):
    """
    Method to generated an empty file.
    """
    if exists(path_str) is False:
        try:
            open(path_str, "a").close()
            return True
        except FileNotFoundError:
            raise FileNotFoundError(
                errno.ENOENT, os.strerror(errno.ENOENT), path_str
            )
    else:
        return False


def tree(path_str):
    """
    Method to walk through a directory tree and discover all files
    and directories on the file system.
    """
    results_lst = []

    if exists(path_str) and is_directory(path_str):
        initial_path_str = os.getcwd()

        os.chdir(path_str)

        for base_str, directories_lst, filenames_lst in os.walk("."):
            for directory_str in directories_lst:
                results_lst.append(
                    describe(
                        path_builder(
                            "abs",
                            os.getcwd(),
                            *[
                                base_str,
                                directory_str
                            ]
                        )
                    )
                )
            for filename_str in filenames_lst:
                results_lst.append(
                    describe(
                        path_builder(
                            "abs",
                            os.getcwd(),
                            *[
                                base_str,
                                filename_str
                            ]
                        )
                    )
                )

        os.chdir(initial_path_str)

        return Tree(
            path=os.path.realpath(path_str),
            results=results_lst
        )
    else:
        raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), path_str
        )
