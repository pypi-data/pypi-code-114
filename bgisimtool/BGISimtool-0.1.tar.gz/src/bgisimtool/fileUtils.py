import os
import collections


def check_if_list_like(obj):
    return isinstance(obj, collections.abc.Iterable) and not isinstance(obj, str)


def findFileWithExtention(path, ext):
    if not ext[0] == ".":
        ext = "." + ext
    if not path[-1] == "/":
        path += '/'
    list_of_file = []
    for file in os.listdir(path):
        if file.endswith(ext):
            list_of_file.append(path+file)
    return list_of_file


def find_file_with_multiple_extension(path, ext_s):
    if check_if_list_like(ext_s):
        for ext in ext_s:
            if not ext[0] == ".":
                ext = "." + ext
    else:
        if not ext_s[0] == ".":
            ext_s = "." + ext_s
    list_of_file = []
    for file in os.listdir(path):
        for ext in ext_s:
            if file.endswith(ext):
                list_of_file.append(os.path.join(path, file))
    list_of_file.sort()
    return list_of_file


def get_path_minus_n_branch(path, n):
    if path[-1] == "/":
        path = path[:-1]
    return '/'.join(path.split('/')[0:-n])