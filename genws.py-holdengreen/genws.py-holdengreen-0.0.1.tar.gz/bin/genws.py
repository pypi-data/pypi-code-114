#!/usr/bin/python

#
#
#

import os
from pathlib import Path
import importlib
from shutil import copyfile

def sum(ls):
    ret = 0
    for e in ls:
        ret += e
    return ret

def mkdir(path):
	if not os.path.exists(path):
		print("mkdir(): '{path}' creating".format(path=path))
		os.mkdir(path)
	else:
		print("mkdir(): '{path}' exists, skipping".format(path=path))

def mkdirs(path):
	if not os.path.exists(path):
		print("mkdirs(): '{path}' creating".format(path=path))
		os.makedirs(path)
	else:
		print("mkdirs(): '{path}' exists, skipping".format(path=path))

def readfl(fl):
	handle = open(fl, 'r')
	ret = handle.read()
	handle.close()
	return ret

def writefl(fl, data):
	handle = open(fl, 'w')
	handle.write(data)
	handle.close()


ROOT         = "./"
PROJECT_DIR  = "genws"
PROJECT_PATH = ROOT + PROJECT_DIR
MACROS_PATH  = ROOT + PROJECT_DIR + '/' + "macros/"
LOG_PATH     = ROOT + PROJECT_DIR + '/' + "log/"
CONF_FILE    = "ws.py"
CONF_PATH    = ROOT + PROJECT_DIR + '/' + CONF_FILE
COPY_NO_PROCESS_PATH = PROJECT_PATH + '/' + "copy_no_process"

SRC_PATH = ROOT + "src"
OUT_PATH = ROOT + "out"


if not os.path.exists(PROJECT_PATH):
    print("creating {0} since it doesn't exist".format(PROJECT_PATH))

    os.mkdir(PROJECT_PATH)
    os.mkdir(MACROS_PATH)
    os.mkdir(LOG_PATH)

    Path(COPY_NO_PROCESS_PATH).touch()

if not os.path.exists(CONF_PATH):
    conf_fp = open(CONF_PATH, 'w')
    conf_fp.write("""
title        = "Example Website"
url          = "example.com"

example_text = "hello world"

process_extensions = [
    ".html",
    ".txt"
]
    """)
    conf_fp.close()

#importlib.import_module(PROJECT_PATH + '.' + CONF_FILE)

copy_no_process = readfl(COPY_NO_PROCESS_PATH).split('\n')

exec(readfl(CONF_PATH))


def render(raw, varz=vars()):
    ret = raw.format(**varz)
    return ret

dirs = [x[0] for x in os.walk(SRC_PATH)]

for path in dirs:
    cutoff = "./src/"
    rel_path = os.path.relpath(path, cutoff)
    new_path = "./out/" + rel_path

    mkdirs(new_path)

paths = list(Path(SRC_PATH).rglob('*'))
paths = [str(fl) for fl in paths if fl.is_file()]

if not 'process_extensions' in globals():
    process_extensions = [".html"]

_copy = []
_paths = []
for path in paths:
    found = False
    for ext in process_extensions:
        if path.lower().endswith(ext):
            _paths.append(path)
            found = True

    if not found:
        _copy.append(path)

paths = _paths

def should_copy(rel_path):
    if rel_path in copy_no_process:
        print("ignoring {}".format(rel_path))
        return False
    else:
        return True

for path in paths:
    cutoof = "./src/"
    rel_path = os.path.relpath(path, cutoff)
    dest = "./out/" + rel_path

    if not should_copy(rel_path):
        continue

    raw = readfl(path)
    writefl(dest, render(raw))

for path in _copy:
    cutoff = "./src/"
    rel_path = os.path.relpath(path, cutoff)
    dest = "./out/" + rel_path

    if not should_copy(rel_path):
        continue

    print("copying {0}".format(rel_path))
    copyfile(path, dest)
