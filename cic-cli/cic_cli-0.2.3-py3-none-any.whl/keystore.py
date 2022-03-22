# standard imports
import os
import json
import logging

# external imports
from funga.error import (
        DecryptError,
        KeyfileError,
        )
from funga.keystore import Keystore

logg = logging.getLogger(__name__)


class KeystoreDirectory(Keystore):

    def process_dir(self, path, password_retriever=None, default_password=''):
        for v in os.listdir(path):
            fp = os.path.join(path, v)
            try:
                self.import_keystore_file(fp, password=default_password)
            except IsADirectoryError:
                pass
            except KeyfileError as e:
                logg.warning(f'file {fp} could not be parsed as keyfile: {e}')
            except DecryptError as e:
                if password_retriever is None:
                    raise e
                password = password_retriever()
                self.import_keystore_file(fp, password=password)
