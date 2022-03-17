import json
import logging
from os import makedirs, path
from typing import Dict

from appdirs import AppDirs
from PyQt6.QtCore import QTimer

appdirs = AppDirs("Collimator", "latanowicz.com")
logger = logging.getLogger(__name__)


class Config:
    default = {
        "markers": [
            {
                "type": "center",
                "offset": (0, 0),
                "hex_color": "#ffff00",
            },
            {
                "type": "circle",
                "offset": (0, 0),
                "hex_color": "#0000ff",
                "radius": 50,
            },
        ],
    }

    FILENAME = "config.json"
    INTERVAL = 500  # ms

    def __init__(self) -> None:
        self.data_to_save = None

    def get_config_path(self) -> str:
        return path.join(appdirs.user_config_dir, self.FILENAME)

    def load(self) -> Dict:
        try:
            with open(self.get_config_path(), "r") as f:
                return json.loads(f.read())
        except:
            return self.default

    def save(self, data):
        self.data_to_save = data

    def _do_save(self):
        if not self.data_to_save:
            return

        logger.info("Saving new config.")

        data = self.data_to_save
        self.data_to_save = None
        json_str = json.dumps(data, indent=4)
        filename = self.get_config_path()
        makedirs(path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            f.write(json_str)

    def setup_interval(self):
        timer = QTimer()
        timer.timeout.connect(self._do_save)
        timer.setInterval(self.INTERVAL)
        timer.start()
        self.timer = timer
