from os import name, path
import cloudsync as cs
import tempfile as tf
from .cc_debug import cc_print
from .config import make_auth
import pandas as pd
import json
from . import vars

def connect():
    oauth_config = cs.command.utils.generic_oauth_config('onedrive')
    if vars.token is None:
        if vars.creds_path == "":
            make_auth()
        f = open(vars.creds_path, 'r')
        creds = json.load(f)
    else:
        print("[DEBUG] Loading token from file")
        creds = vars.token # The ouath token is read from file on the local machine and "imported" on the remote one
    vars.provider = cs.create_provider('onedrive', oauth_config=oauth_config)
    vars.provider.connect(creds)

def change_namespace(path_in_ns, namespace=None):
    # Change namespace to shared folder
    ns = vars.provider.list_ns()
    if namespace is None:
        shared_folder_name = path_in_ns
        for x in ns:
            if shared_folder_name in x.name:
                break
        print("Changing namespace to: {}".format(x.id))
        vars.provider.namespace = x
    else:
        for x in ns:
            if namespace in x.name:
                break
        print("Changing namespace to: {}".format(x.id))
        vars.provider.namespace = x

def download_file(filename, namespace=None, output=None, cached=True, force_dl=False):
    if vars.provider is None:
        connect()
    if not namespace is None:
        change_namespace(namespace)
    # Check temp dir for a cached version of the file (unless force_dl=True)
    if force_dl == True:
        cc_print("Forcing re-download...", 2)
    else:
        # Check if file was previously downloaded
        fname = vars.tempdir + filename.split("/")[-1] # Split filename
        if path.exists(fname):
            cc_print("Reading file from cache...", 1)
        tmp = open(fname, 'r')
        return tmp
    if output is None:
        '''
        WARNING: caching (cached=False) will not delete the temporary file (stored in /tmp by default).
        This may be useful instead of re-downloading many times the same file, for speed of execution.
        The temp dir may be periodically emptied by your system daemons (systemd).
        '''
        if cached and (not force_dl):
            print("[DEBUG] caching file...")
            fname = vars.tempdir + filename.split("/")[-1] # Split filename
            tmp = open(fname, 'wb+')    # Open the file in binary mode ('b') > tmp must be _io.BufferedRandom
        else:
            ext = "." + filename.split(".")[-1]
            tmp = tf.NamedTemporaryFile(suffix=ext, dir=vars.tempdir, delete=(not cached))
            fname = tmp.name
        cc_print("Downloading to {} ...".format(fname), 1)
    else:
        tmp = open(output, 'wb+')
    vars.provider.download_path(filename, tmp)
    tmp.seek(0) # Go back to first line
    return tmp

def read_remote_csv_pandas(fname, header=None, namespace=None):
    f = download_file(f, namespace=namespace, cached=False, force_dl=True)
    df = pd.read_csv(f.name, header=header)
    return df

def upload_file():
    print("> upload_file()")
    print("Still to be implemented...")