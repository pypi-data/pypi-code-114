# ezai

from . import util

from pathlib import Path

version_file = Path(__file__).parent.joinpath('version.txt')
with open(version_file, 'r') as vf:
    __version__ = vf.read().strip()

__all__ = ['image', 'env', 'dict', 'json', 'res','util']
