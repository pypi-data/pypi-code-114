"""Basic functions to create cryptographic keys, and to encrypt string data.

Basic cryptographic functions to aid in key management for the user.
"""

import nacl.bindings
import logging
from datetime import datetime
from urllib.parse import urlparse

from didauth.headers import HeaderSigner
from didauth.base import SignerBase

from aries_cloudagent.wallet.crypto import (create_keypair, bytes_to_b58, validate_seed,
                                            verify_signed_message, b58_to_bytes, sign_message)

log = logging.getLogger(__name__)


def create_did(seed: bytes):
    """Creates a DID and verkey from the given seed.

    Args:
        seed (bytes): the secret seed to use in generating the verkey.

    Returns:
        tuple: `(did, verkey)`.
    """
    seed = validate_seed(seed)
    verkey, _ = create_keypair(seed)
    did = bytes_to_b58(verkey[:16])
    return did, bytes_to_b58(verkey)


def verify_signature(signature, verkey, message=None):
    """Verifies a signature cryptographically.

    Args:
        agent (str): name of the agent whose master key should be used.
        signature (str): hex-encoded signature that should be verified.
        verkey (str): public key to use in verifying the signature.
    """
    s, v = bytes.fromhex(signature), b58_to_bytes(verkey)
    if message is not None:
        if isinstance(message, bytes):
            return verify_signed_message(s + message, v)
        else:
            return verify_signed_message(s + message.encode("UTF-8"), v)
    else:
        return verify_signed_message(s, v)


def anon_crypt_message(message: bytes, pk: bytes) -> bytes:
    """Apply anon_crypt to a binary message.

    Args:
        message: The message to encrypt
        pk: The verkey to encrypt the message for

    Returns:
        The anon encrypted message
    """
    _pk = nacl.bindings.crypto_sign_ed25519_pk_to_curve25519(pk)
    enc_message = nacl.bindings.crypto_box_seal(message, _pk)
    return enc_message


def anon_decrypt_message(enc_message: bytes, pk: bytes, sk: bytes) -> bytes:
    """Apply anon_decrypt to a binary message.

    Args:
        enc_message: The encrypted message
        pk: public key that the message was encrypted for.
        sk: private key that the message was encrypted for.

    Returns:
        The decrypted message
    """
    _pk = nacl.bindings.crypto_sign_ed25519_pk_to_curve25519(pk)
    _sk = nacl.bindings.crypto_sign_ed25519_sk_to_curve25519(sk)

    message = nacl.bindings.crypto_box_seal_open(enc_message, _pk, _sk)
    return message


def generate_keys(seed):
    """Generates keys from a given seed.

    Args:
        seed (str): of `32` characters or less. 32 characters encodes a 128-bit seed. If fewer
            than `32` are specified, it will be front-padded with zeros.
    """
    if isinstance(seed, bytes):
        byte_seed = seed
    else:
        byte_seed = f"{seed:0<32}".encode()
    pk, sk = create_keypair(byte_seed)
    did, verkey = create_did(byte_seed)
    return {    
        "seed": bytes_to_b58(seed) if isinstance(seed, bytes) else seed,
        "did": did, 
        "public": verkey, 
        "secret": sk.hex()
    }


class ExplicitSigner(SignerBase):
    """Message signer that uses an explicit set of keys to sign messages.
    """
    algorithm = "ed25519"
    def __init__(self, keys):
        super(ExplicitSigner, self).__init__(self, "ed25519")
        self._pubkey = b58_to_bytes(keys["public"])
        self._secret = keys["secret"]
        self.vk = keys["public"]
        self.did = keys["did"]

    def _sign(self, data: bytes) -> bytes:
        log.debug(f"Signing message of length {len(data)} for DID {self.did} using {self.vk}.")
        result = sign_message(data, bytes.fromhex(self._secret))
        log.debug(f"Signing result is {result} from {data}")
        return result


def get_signed_headers(keys, url, method, headers=None):
    """Gets the didauth headers to sign for an HTTP request.
    """
    log.debug(f"Signing headers {headers} with DID {keys['did']} and PK {keys['public']}.")
    o = urlparse(url)
    _headers = headers or {}
    _headers.update({
        'Date': str(datetime.utcnow()),
        'Host': o.netloc,
        'User-Agent': f'ClearOSMobile/1.0',
    })
    header_list = ['(request-target)']
    header_list.extend(_headers.keys())
    url_path = o.path
    log.debug(f"Using {header_list} as target headers for signing at {url_path}.")
    log.debug(f"Using public keypair {keys['public']} to sign headers.")

    try:
        hdr_signer = HeaderSigner(keys["did"], ExplicitSigner(keys), header_list)
        signed_headers = hdr_signer.sign(_headers, method, url_path)
        assert 'authorization' in signed_headers
    except:
        log.exception("Signing headers for `didauth`.")
        return None
        
    return signed_headers


def get_header_signature_dict(headers):
    """Returns a dictionary of key-value pairs from the `Signature` header.
    """
    raw = headers.get("Authorization")
    if raw is None:
        # falcon has lowercase header keys.
        raw = headers.get("authorization")

    if raw is None:
        return {}

    log.debug(f"Using {raw} as Authorization header contents.")
    if "Signature " in raw:
        kvps = raw.split("Signature ")[1]
        result = {}
        for kp in kvps.split(','):
            parts = kp.split('=')
            if len(parts) == 2:
                k, v = parts
            else:
                k = parts[0]
                v = '='.join(parts[1:])
            result[k] = v.replace('"', '')

        return result

    else:
        return {}