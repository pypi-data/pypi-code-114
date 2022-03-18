from configparser import ConfigParser

class Config:

    def __init__(self, path):
        self.config = ConfigParser()
        # read config.ini file
        self.config.read(path)

    def get(self, section, key, default=None):
        # get config value
        if section in self.config and key in self.config[section]:
            return self.config[section][key]
        elif (section in self.config and key not in self.config[section]) or (section not in self.config):
            if default is not None:
                return default
            else:
                return None
        else:
            raise Exception('Configuration not found!')