# *_*coding:utf-8 *_*
import os
from pathlib import Path
from typing import Dict

DATA_PATH = os.path.join(str(Path.home()), '.langma')

Path(DATA_PATH).mkdir(exist_ok=True, parents=True)


class Config:
    def __init__(self) -> None:
        self.verbose = False

    def to_dict(self) -> Dict:
        return {'verbose': self.verbose}


config = Config()

if __name__ == "__main__":
    pass
