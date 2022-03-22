import bz2
import gzip
import shutil
import tarfile
import zipfile
from pathlib import Path

from . import filesys


class Archive():
    def __init__(self, ar_filename):
        self.archive = ar_open(ar_filename)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.archive.close()

    def open(self, ar_filename):
        return ar_open(ar_filename)

    def open_file(self, filename):
        return ar_open_file(self.archive, filename)

    def contains(self, filename):
        return ar_contains(self.archive, filename)

    def contents(self):
        return ar_contents(self.archive)

    def extract_all(self, dest):
        return ar_extract_all(self.archive, dest)

    def extract_file(self, filename, dest):
        return ar_extract_file(self.archive, filename, dest)


def ar_open(ar_filename: str):
    """
    Function to open the archive
    :param ar_filename:
    :return:
    """
    if ar_filename.endswith('.bz2'):
        ar = tarfile.open(ar_filename, 'r:bz2')
    elif ar_filename.endswith('.gz'):
        ar = tarfile.open(ar_filename, 'r:gz')
    elif ar_filename.endswith('.xz'):
        ar = tarfile.open(ar_filename, 'r:xz')
    elif ar_filename.endswith('.zip'):
        ar = zipfile.ZipFile(ar_filename)
    else:
        ar = open(ar_filename)
    return ar


def ar_open_file(ar, filename):
    """
    Function to open a specific file in an archive

    :param ar:
    :param filename:
    :return:
    """
    if isinstance(ar, (zipfile.ZipFile, bz2.BZ2File, gzip.GzipFile)):
        ar_file = ar.open(filename)
    elif isinstance(ar, tarfile.TarFile):
        ar_file = ar.extractfile(filename)
    else:
        ar_file = False
    return ar_file


def ar_contains(ar, f):
    """
    Function to check if the archive contains a file or not
    :param ar:
    :param f:
    :return:
    """
    if isinstance(ar, zipfile.ZipFile):
        success = f in ar.namelist()
    elif isinstance(ar, (tarfile.TarFile)):
        success = f in ar.getnames()
    else:
        success = False
    return success


def ar_contents(ar):
    """
    Function to list the contents of an archive

    :param ar:
    :return:
    """
    if isinstance(ar, zipfile.ZipFile):
        # namelist = ar.namelist()
        names = {}
        infolist = ar.infolist()
        if not infolist[0].is_dir:
            dirname = '/'
            names[dirname] = []
        for info in infolist:
            if info.is_dir():
                dirname = Path(info.filename).name
                names[dirname] = []
            else:
                filename = Path(info.filename).name
                names[dirname].append(filename)
        namelist = names
    elif isinstance(ar, tarfile.TarFile):
        namelist = ar.getnames()
    else:
        namelist = False

    # print(namelist)
    # if namelist:
    #    names = {}
    #    if not Path(namelist[0]).is_dir():
    #        dirname = 'root'
    #        names[dirname]=[]
    #    for name in namelist:
    #        name = Path(name)
    #        if name.is_dir():
    #            dirname = name.name                
    #            names[dirname]=[]
    #        else:
    #            filename = name.name
    #            names[dirname].append(filename)
    #
    #    namelist = names
    return namelist


def ar_extract_all(ar, dest='.'):
    """
    Function to extract all the files in an archive

    :param ar: open archive handle
    :param dest:
    :return:
    """
    if isinstance(ar, str):
        ar = ar_open(ar)
    try:
        ar.extractall(dest)
    except (tarfile.TarError, RuntimeError, KeyboardInterrupt):
        # remove the destination folder/file
        shutil.rmtree(dest)
        raise


def ar_extract_file(ar, filename, dest='.'):
    """
    Function to extract one file in an archive

    :param ar: open archive handle
    :param dest:
    :return:
    """
    try:
        ar.extract(dest)
    except (tarfile.TarError, RuntimeError, KeyboardInterrupt):
        # remove the destination folder/file
        filesys.rm(dest)
        raise


def archive_extract(ar_filename, dest='.'):
    """Extracts an archive if it matches tar, tar.gz, tar.bz, or zip formats.
    """
    ar = ar_open(ar_filename)
    ar_extract_all(ar, dest)
