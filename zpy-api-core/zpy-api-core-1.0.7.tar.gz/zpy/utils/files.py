# Created by Noé Cruz | Zurckz 22 at 20/03/2022
# See https://www.linkedin.com/in/zurckz

import os
import sys
import json
from pathlib import Path


def read_event(name: str = None, event_file_path: str = None):
    event_path = f"{os.getcwd()}\\events\\{name}" if name else event_file_path
    if not event_path:
        raise ValueError("Path file or name is required...")
    with open(event_path, 'r') as sm:
        return json.loads(sm.read())


def add_source_to_path(src_dir: str = None, replacement: str = None):
    current_dir = src_dir
    if not current_dir:
        current_dir = os.getcwd()
        current_dir = current_dir.replace('\\tests' if not replacement else replacement, '\\src')
    sys.path.append(current_dir)
    path = Path(current_dir)
    sys.path.append(str(path.parent.absolute()))
