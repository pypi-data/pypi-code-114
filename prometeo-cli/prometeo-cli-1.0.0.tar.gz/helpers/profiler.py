import os
import configparser

from pathlib import Path
from exceptions import ProviderNotFound
from .crypto import Crypto

class Profiler():

    def __init__(self):
        home = str(Path.home())
        self._directory = f'{home}/.prometeo'
        self._config_path = f'{self._directory}/configuration.ini'
        self._credentials_path = f'{self._directory}/credentials.ini'

    def initialize(self):
        if not self._exists_directory():
            self._create_directory()

        if not self._exists_configurations():
            self._create_config_file()

        if not self._exists_profile_file():
            self._create_profile_file()

    def _exists_directory(self):
        return os.path.isdir(self._directory)

    def _create_directory(self):
        os.mkdir(self._directory)

    def _exists_configurations(self):
        return os.path.isfile(self._config_path)

    def _create_config_file(self):
        with open(self._config_path, 'a') as fs:
            fs.write('[example]\n')
            fs.write('api_key=12345\n')

    def _exists_profile_file(self):
        return os.path.isfile(self._credentials_path)


    def _create_profile_file(self):
        with open(self._credentials_path, 'a') as fs:
            fs.write('[example]\n')
            fs.write('username=1234\n')
            fs.write('password=12345\n')

    def get_credentials(self, provider, passphrase):
        config = configparser.ConfigParser()
        config.read(self._credentials_path)
        if provider not in config.sections():
            raise ProviderNotFound(f'{provider} not found configuration for this provider')

        crypto = Crypto()
        b_text = crypto.decrypt(config[provider]['password'], passphrase)

        return (config[provider]['username'], b_text.decode())


    def exists_section_credentials(self, provider):
        config = configparser.ConfigParser()
        config.read(self._credentials_path)
        return provider in config.sections()

    def exists_section_envs(self, env):
        config = configparser.ConfigParser()
        config.read(self._config_path)
        return env in config.sections()


    def get_configuration(self, profile):
        config = configparser.ConfigParser()
        config.read(self._config_path)
        if profile not in config.sections():
            raise Exception(profile, 'Does not exists')

        return config[profile]['api_key']


    def add_new_credential(self, provider, username, password):
        if self.exists_section_credentials(provider):
            config = configparser.ConfigParser()
            config.read(self._credentials_path)
            # modify
            config[provider]['username'] = username
            config[provider]['password'] = password

            # override
            with open(self._credentials_path, 'w') as fs:
                config.write(fs)
        else:
            with open(self._credentials_path, 'a') as fs:
                fs.write(f'[{provider}]\n')
                fs.write(f'username={username}\n')
                fs.write(f'password={password}\n')

    def add_new_environment(self, environment, api_key):
        if self.exists_section_envs(environment):
            config = configparser.ConfigParser()
            config.read(self._config_path)
            # modify
            config[environment]['api_key'] = api_key

            # override
            with open(self._config_path, 'w') as fs:
                config.write(fs)
        else:
            with open(self._config_path, 'a') as fs:
                fs.write(f'[{environment}]\n')
                fs.write(f'api_key={api_key}\n')





