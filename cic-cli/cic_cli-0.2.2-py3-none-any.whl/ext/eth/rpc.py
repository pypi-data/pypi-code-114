# standard imports
from getpass import getpass
import logging
import os
import stat

# external imports
from funga.eth.keystore.dict import DictKeystore
from funga.eth.signer import EIP155Signer
from chainlib.cli import Wallet
from chainlib.eth.cli import Rpc

# local imports
from cic.keystore import KeystoreDirectory


logg = logging.getLogger(__name__)


class EthKeystoreDirectory(DictKeystore, KeystoreDirectory):
    """Combination of DictKeystore and KeystoreDirectory

    TODO: Move to funga
    """


def get_passphrase():
    return getpass('Enter passphrase: ')

def parse_adapter(config, signer_hint):
    """Determine and instantiate signer and rpc from configuration.

    If either could not be determined, None is returned.

    :param config: Configuration object implementing the get() method
    :type config: dict, object with get()
    :param signer_hint: Signer resource description (e.g. keystore directory)
    :type signer_hint: str
    :rtype: tuple; chainlib.connection.RPCConnection, funga.signer.Signer
    :return: RPC interface, signer interface
    """
    keystore = None
    if signer_hint is None:
        logg.info("signer hint missing")
        return None
    st = os.stat(signer_hint)
    if stat.S_ISDIR(st.st_mode):
        logg.debug("signer hint is directory")
        keystore = EthKeystoreDirectory()
        keystore.process_dir(signer_hint, password_retriever=get_passphrase)

    w = Wallet(EIP155Signer, keystore=keystore)
    signer = EIP155Signer(keystore)
    rpc = Rpc(wallet=w)
    rpc.connect_by_config(config)

    return (rpc.conn, signer)

# TODO Find a better place for this
def list_keys(config, signer_hint):
    keystore = None
    if signer_hint is None:
        logg.info("signer hint missing")
        return None
    st = os.stat(signer_hint)
    if stat.S_ISDIR(st.st_mode):
        logg.debug("signer hint is directory")
        keystore = EthKeystoreDirectory()
        keystore.process_dir(signer_hint, default_password=config.get('WALLET_PASSPHRASE', ''), password_retriever=get_passphrase)
        
    return keystore.list()
