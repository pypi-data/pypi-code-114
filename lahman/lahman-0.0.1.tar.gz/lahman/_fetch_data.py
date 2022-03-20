import os
import re
import shutil
import zipfile
import pandas as pd

from pathlib import Path
from functools import partial

try:
    from importlib.resources import files
except ImportError:
    from importlib_resources import files


BASE_URL = "https://github.com/chadwickbureau/baseballdatabank/archive/refs/tags/"
TAG = "v2021.2"
SOURCE_DIR = files("lahman") / "data"
SOURCE_PATH = SOURCE_DIR / "_source.zip"


def fetch_data(dst_file=None):
    import requests

    r = requests.get(f"{BASE_URL}/{TAG}.zip", stream=True)
    r.raise_for_status()
    with open(SOURCE_PATH, "wb") as f:
        shutil.copyfileobj(r.raw, f)


def unpack_data():
    with zipfile.ZipFile(SOURCE_PATH, "r") as f_zip:
        for info in f_zip.infolist():
            if "/core/" in info.filename and info.filename.endswith(".csv"):
                info.filename = Path(info.filename).name
                f_zip.extract(info, SOURCE_PATH.parent)


def format_name(fname):
    return re.sub("(?!^)([A-Z]+)", r"_\1", fname).lower().replace(".csv", "")


def create_data_accessors(fpaths):
    accessors = {}
    for path in fpaths:
        accessors[format_name(path.name)] = partial(pd.read_csv, path)

    return accessors


def remove_data():
    for csv in SOURCE_DIR.glob("*.csv"):
        os.remove(csv)


if __name__ == "__main__":
    fetch_data()
    unpack_data()
