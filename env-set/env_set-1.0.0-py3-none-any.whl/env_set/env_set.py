import os
import re
from tkinter.messagebox import NO


class WriteENV(object):

    def __init__(self, filepath: str, *args, **kwargs) -> None:
        self._filepath = filepath
        self.mapper = {}
        self._args = args
        self._kwargs = kwargs
        self.__read_environment_variables__()

    def __read_environment_variables__(self):
        try:
            with open(os.path.dirname(self._filepath)+self._filepath, "w+") as f:
                # mapper = {}
                content = f.read().splitlines()
                # print(content)
                for line, data in enumerate(content):
                    valreg = r"([a-zA-Z_]+[0-9]*=[a-zA-Z0-9]*)"
                    if re.compile(valreg).match(data):
                        dictionary = {}
                        k, v = data.split(r"=")
                        dictionary["line"] = line
                        dictionary[k] = v
                        self.mapper[k] = dictionary
        except FileNotFoundError:
            # print("Not found")
            with open(self._filepath, "w+") as f:
                f.write("\n")

    def get_environment_keys(self):
        keys = []
        for x in self.mapper.keys():
            # for k, _ in x:
            keys.append(x)
        return keys

    def get_environment_values(self):
        values = []
        # print(self.mapper)
        for v in self.mapper.items():
            if v is not None:
                key_item = list(v[1].keys())
                values.append(key_item[1])
        return values

    def set_value(self, key, value):
        if self.search_value(key) is not None:
            self.mapper[key][key] = value
        else:
            key_count = len(self.mapper.items())
            self.mapper[key] = {"line": key_count + 1, key: value}
        try:
            with open(self._filepath, "r+") as f:
                for k, v in self.mapper.items():
                    f.writelines(f"{k}={v[k]}\n")
        except FileNotFoundError:
            with open(self._filepath, "r+") as f:
                for k, v in self.mapper.items():
                    f.writelines(f"{k}={v[k]}\n")

    def search_value(self, key):
        val = self.mapper.get(key)
        if val is not None:
            return val
        return None

    def create_env_example(self, example_name):
        keys = self.get_environment_keys()
        with open(os.path.join(os.path.dirname(self._filepath), example_name), "w+") as f:
            [f.writelines(f"{key}=\n") for key in keys]

