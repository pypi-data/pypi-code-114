from lisp_utils import Configuration
from unittest import mock
import unittest
import io


class ConfigFiles(unittest.TestCase):


    def test_user_provided_config(self):

        config_file = '/tmp/user_config.json'
        return_value = io.StringIO('{"content":{"test_name":"user_provided_conf"}}')

        with mock.patch('builtins.open', return_value=return_value) as m:
            conf = Configuration(config_file_path=config_file)
            m.assert_called_with(config_file, 'r')
            self.assertEqual(conf.config_file_path, config_file)
            self.assertEqual(conf.get('content.test_name'), 'user_provided_conf')



    def test_env_provided_config(self):

        config_file = '/tmp/env_config.json'
        return_value = io.StringIO('{"content":{"test_name":"env_provided_conf"}}')

        with mock.patch('builtins.open', return_value=return_value) as m:
            with mock.patch('os.getenv', return_value=config_file):
                conf = Configuration()
                m.assert_called_with(config_file, 'r')
                self.assertEqual(conf.config_file_path, config_file)
                self.assertEqual(conf.get('content.test_name'), 'env_provided_conf')



    def test_default_config_lisp(self):

        config_file = '/lisp/global_configs/common.json'
        return_value = io.StringIO('{"content":{"test_name":"default_lisp_conf"}}')

        with mock.patch('builtins.open', return_value=return_value) as m:
            conf = Configuration()
            m.assert_called_with(config_file, 'r')
            self.assertEqual(conf.config_file_path, config_file)
            self.assertEqual(conf.get('content.test_name'), 'default_lisp_conf')



    def test_default_config_opt(self):

        config_file = '/opt/siem/global_configs/common.json'
        return_value = io.StringIO('{"content":{"test_name":"default_opt_conf"}}')

        with mock.patch('builtins.open', side_effect=[FileNotFoundError, return_value]) as m:
            conf = Configuration()
            m.assert_called_with(config_file, 'r')
            self.assertEqual(conf.config_file_path, config_file)
            self.assertEqual(conf.get('content.test_name'), 'default_opt_conf')



    def test_config_priority(self):

        user_config_file = '/tmp/user_config.json'
        env_config_file = '/tmp/env_config.json'
        lisp_config_file = '/lisp/global_configs/common.json'
        opt_config_file = '/opt/siem/global_configs/common.json'

        def mocked_open(path, mode):

            user_return_value = io.StringIO('{"content":{"test_name":"user_provided_conf"}}')
            lisp_return_value = io.StringIO('{"content":{"test_name":"default_lisp_conf"}}')
            opt_return_value = io.StringIO('{"content":{"test_name":"default_opt_conf"}}')

            return { user_config_file : user_return_value,
                     lisp_config_file : lisp_return_value,
                     opt_config_file : opt_return_value
                     }.get(path)


        with mock.patch('builtins.open', mocked_open):

            # Testing lettura config passati nel costruttore
            conf = Configuration(config_file_path=user_config_file)
            self.assertEqual(conf.config_file_path, user_config_file)
            self.assertEqual(conf.get('content.test_name'), 'user_provided_conf')

            # Testing lettura config di default
            conf = Configuration()
            self.assertEqual(conf.config_file_path, lisp_config_file)
            self.assertEqual(conf.get('content.test_name'), 'default_lisp_conf')

            # Testing priorità tra config passati nel costruttore e
            # config impostati con la variabile d'ambiente 'LISP_UTILS_CONFIG_PATH'
            with mock.patch('os.getenv', return_value=env_config_file):
                conf = Configuration(config_file_path=user_config_file)
                self.assertEqual(conf.config_file_path, user_config_file)
                self.assertEqual(conf.get('content.test_name'), 'user_provided_conf')

            ## TODO: Verificare ordine di apertura dei config file di default '/lisp/global_configs/common.json' e '/opt/siem/global_configs/common.json'