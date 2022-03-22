#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import requests
import hashlib
import os
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
def down_proj_mat(destination=None):
    if destination == None:
        libLocal = os.path.dirname(os.path.realpath(__file__))
        mat_file_local = os.path.join(libLocal,'sweep-default-projection-matrix-600.mat')
        destination = mat_file_local
    try:
        if md5(destination) == 'f18587ac79c452e419f0bcb2059d6619':
            print('The default projection matrix is already available at <%s>' % (destination), flush=True)
            return
    except FileNotFoundError:
        pass
    link = "https://github.com/diogomachado-bioinfo/sweep-default-projection-matrix/releases/download/sweep-default-projection-matrix/sweep-default-projection-matrix-600.mat"
    with open(destination, "wb") as f:
        print('The download destination is <%s>' % (destination), flush=True)
        print("Downloading %s" % os.path.basename(destination), flush=True)
        response = requests.get(link, stream=True)
        total_file_size = response.headers.get('content-length')
        c = 0
        total_file_size = int(total_file_size)
        for data in response.iter_content(chunk_size=4096):
            c += len(data)
            f.write(data)
            s = int(50*c/total_file_size)
            sys.stdout.write("\r[%s%s]" % ('='*s, ' '*(50-s)) )    
            sys.stdout.flush()
    if md5(destination) != 'f18587ac79c452e419f0bcb2059d6619':
        raise("Download failed")
def return_proj_mat_not_found_error():
    error_str = 'Default projection matrix not found, to download it use:\nfrom sweep import down_proj_mat\ndown_proj_mat()'
    raise Exception(error_str)
def check_default_proj_mat(file):
    try:
        if md5(file) != 'f18587ac79c452e419f0bcb2059d6619':
            return_proj_mat_not_found_error()
    except FileNotFoundError:
        return_proj_mat_not_found_error()