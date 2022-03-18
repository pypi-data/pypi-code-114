from datetime import datetime
import logging
import nacl
from aries_cloudagent.wallet.util import b58_to_bytes, b64_to_bytes, bytes_to_b58
from urllib.request import parse_http_list
import multidict
from typing import Mapping

log = logging.getLogger(__name__)


class VerifierException(Exception):
    pass


class SignerException(VerifierException):
    pass


def decode_string(key, enc_format: str) -> bytes:
    if enc_format == 'base58':
        return b58_to_bytes(key)
    elif enc_format == 'base64':
        return b64_to_bytes(key)
    elif enc_format == 'hex':
        return bytes.fromhex(key)
    else:
        raise VerifierException('Key format not supported: {}'.format(enc_format))


class VerifierBase:
    def __init__(self, _key_type, _pubkey=None):
        self._pubkey = None

    @property
    def public_key(self) -> bytes:
        pass

    def _verify(self, _message: bytes, _signature: bytes, android: bool = False) -> bool:
        raise SystemError('Not implemented')

    def verify(self, message, signature, signature_format=None, android=False) -> bool:
        if signature_format:
            signature = decode_string(signature, signature_format)
        return self._verify(message, signature, android)


class Verifier(VerifierBase):
    algorithm = 'ed25519'

    def __init__(self, key_type, pubkey):
        super(Verifier, self).__init__(key_type)
        self._pubkey = pubkey

    def _verify(self, message: bytes, signature: bytes, android: bool = False) -> bool:
        try:
            vk = bytes_to_b58(self._pubkey)
            if android:
                # Make sure the message we generated is in the signature payload,
                # then just verify the payload.
                log.debug(f"Android signature verification of {message} and {signature} for {vk}.")
                assert signature[-len(message):] == message
                nacl.bindings.crypto_sign_open(signature, self._pubkey)
            else:
                log.debug(f"Standard signature verification of {message} and {signature} for {vk}.")
                nacl.bindings.crypto_sign_open(signature + message, self._pubkey)
            return True
        except:
            log.debug("Error validating signature", exc_info=True)
            return False


class SignatureHandlers:
    def __init__(self):
        self._classes = {}

    def add_key_type(self, key_type: str, signer, verifier):
        self._classes[key_type] = (signer, verifier)

    def supports(self, key_type: str):
        return key_type in self._classes

    def get_supported(self):
        return self._classes.keys()

    def create_signer(self, key_type, secret, secret_format=None):
        if secret and secret_format:
            secret = decode_string(secret, secret_format)
        return self._classes[key_type][0](key_type, secret)

    def create_verifier(self, key_type, pubkey, pubkey_format=None):
        if pubkey and pubkey_format:
            pubkey = decode_string(pubkey, pubkey_format)
        return self._classes[key_type][1](key_type, pubkey)


def parse_authorization_header(header):
    if isinstance(header, bytes):
        header = header.decode('ascii')  # HTTP headers cannot be Unicode.

    auth = header.split(' ', 1)
    if len(auth) > 2:
        raise VerifierException('Invalid authorization header. (eg. Method ' +
                                'key1=value1,key2="value, \"2\"")')

    # Split up any args into a dictionary.
    values = multidict.CIMultiDict()
    if len(auth) == 2:
        auth_value = auth[1]
        if auth_value:
            # This is tricky string magic.  Let urllib do it.
            fields = parse_http_list(auth_value)

            for item in fields:
                # Only include keypairs.
                if '=' in item:
                    # Split on the first '=' only.
                    key, value = item.split('=', 1)
                    if not key or not value:
                        continue

                    # Unquote values, if quoted.
                    if value[0] == '"':
                        value = value[1:-1]

                    values[key] = value

    # ("Signature", {"headers": "date", "algorithm": "hmac-sha256", ... })
    return (auth[0], values)



def signing_header(name, values):
    if isinstance(values, str):
        value = values
    else:
        value = ', '.join(v.strip() for v in values)
    return '{}: {}'.format(name, value)


def generate_message(required_headers, headers, method=None, path=None) -> bytes:
    headers = multidict.CIMultiDict(headers)

    if not required_headers:
        required_headers = ['date']

    signable_list = []
    for h in required_headers:
        h = h.lower()
        if h == '(request-target)':
            if not method or not path:
                raise SignerException('Method and path arguments required when ' +
                                      'using "(request-target)"')
            signable_list.append(signing_header(h, '{} {}'.format(method.lower(), path)))
        else:
            if h not in headers:
                raise SignerException('Missing required header "{}"'.format(h))
            signable_list.append(signing_header(h, headers.getall(h)))

    signable = '\n'.join(signable_list).encode('ascii')
    return signable


class Ed25519HeaderVerifier:
    """
    Verifies an HTTP signature from given headers.
    """
    def __init__(self, pubkey: bytes, required_headers=None):
        self.pubkey = pubkey
        self._handlers = ALL
        log.debug(f"Required headers set as {required_headers}.")
        if required_headers is None:
            required_headers = ["date"] # implementors should require (request-target) and date
        self._required_headers = [h.lower() for h in required_headers]


    def verify(self, headers: Mapping, method=None, path=None, android=False):
        """
        Parse Signature Authorization header and verify signature

        `headers` is a dict or multidict of headers
        `host` is a override for the 'host' header (defaults to value in
            headers).
        `method` is the HTTP method (required when using '(request-target)').
        `path` is the HTTP path (required when using '(request-target)').

        Args:
            android (bool): when True, treat the signature as coming from an android 
                app running lazy-sodium.
        """
        if not 'authorization' in headers:
            return False

        auth_type, auth_params = parse_authorization_header(headers['authorization'])
        if auth_type.lower() != 'signature':
            return False

        for param in ('algorithm', 'keyId', 'signature'):
            if param not in auth_params:
                raise VerifierException("Unsupported HTTP signature, missing '{}'".format(param))

        auth_headers = (auth_params.get('headers') or 'date').lower().strip().split()

        missing_reqd = set(self._required_headers) - set(auth_headers)
        if missing_reqd:
            error_headers = ', '.join(missing_reqd)
            raise VerifierException(
                'One or more required headers not provided: {}'.format(error_headers))

        key_id, algo = auth_params['keyId'], auth_params['algorithm']

        if not self._handlers.supports(algo):
            raise VerifierException("Unsupported HTTP signature algorithm '{}'".format(algo))

        if not self.pubkey:
            raise VerifierException("Cannot locate public key for '{}'".format(key_id))
        log.debug("Got %s public key for '%s': %s", algo, key_id, bytes_to_b58(self.pubkey))

        handler = self._handlers.create_verifier(algo, self.pubkey)
        message = generate_message(auth_headers, headers, method, path)

        signature = auth_params['signature']
        raw_signature = decode_string(signature, 'base64')

        if handler.verify(message, raw_signature, android=android):
            return {
                'verified': True,
                'algorithm': algo,
                'headers': auth_headers,
                'keyId': key_id,
                'key': self.pubkey,
                'signature': signature
            }
        raise VerifierException("Signature could not be verified for keyId '{}'".format(key_id))


ALL = SignatureHandlers()
ALL.add_key_type('ed25519', None, Verifier)


def auth_did_signature(did, pubkey, headers, method, url_path):
    """Checks the DID signature in the headers to make sure that it is valid.

    Args:
        headers (dict): headers from the request object.
        method (str): one of the HTTP methods used in the request.
        url_path (str): full request path (excluding the host name and query
            string parameter).
    """
    log.debug(f"Creating header verifier for DID {did} with PK {pubkey}.")
    if pubkey is None:
        return False, None

    verifier = Ed25519HeaderVerifier(b58_to_bytes(pubkey))
    log.debug(f"Verifying headers: {headers} with {method} at {url_path}.")
    is_android = "okhttp" in headers.get("User-Agent", "") or "okhttp" in headers.get("user-agent", "")
    try:
        verified = verifier.verify(headers, method, url_path, android=is_android)
    except VerifierException:
        log.exception(f"Verifying DID-based signature for {headers} and {method}>{url_path}.")
        return False, None

    if isinstance(verified, bool) or "keyId" not in verified:
        return False, None

    their_did = verified["keyId"]
    did_ok = False
    if verified['verified'] and their_did == did:
        # Check that the datetime is within a 15 seconds
        did_ok = didauth_time_okay(headers["date"], 15)

    return did_ok, their_did


def didauth_time_okay(their_date, max_seconds):
    """Checks whether the time encoded in a `didauth` message is close enough to the timestamp on the server.

    Args:
        their_date (str): date/time from the request.
        max_seconds (int): maximum number of seconds allowed for the time difference to be okay.

    Returns:
        bool: `True` if the time is within `max_seconds` of the server time.
    """
    server_now = datetime.utcnow()
    request_now = datetime.strptime(their_date, "%Y-%m-%d %H:%M:%S.%f")

    if server_now > request_now:
        delta = server_now - request_now
    else:
        delta = request_now - server_now

    result = delta.seconds < max_seconds
    if not result:
        log.debug(f"DID auth failed; too long: {delta.seconds} > {max_seconds}\n"
                    f"\t{server_now}\n"
                    f"\t{request_now}")
        
    return result
