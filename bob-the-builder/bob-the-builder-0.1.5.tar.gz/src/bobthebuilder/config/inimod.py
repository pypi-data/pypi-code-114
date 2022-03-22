import configparser
import pathlib


class IniModifier:
    def __init__(self, filename: str):
        self.filename = str(pathlib.Path(filename).resolve())
        self.parser = configparser.ConfigParser()
        self._load()

    def set(self, section, key, value):
        self.parser.set(section, key, value)

    def _load(self):
        with open(self.filename, 'rt') as fp:
            self.parser.read_file(fp)

    def save(self):
        with open(self.filename, 'wt') as fp:
            self.parser.write(fp)
