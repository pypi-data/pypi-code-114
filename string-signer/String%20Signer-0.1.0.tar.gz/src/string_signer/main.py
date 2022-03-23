"""This module was created to sign strings.

It's only uses building libraries, therefore, it has no external dependency.
It is also lightweight and thread-safe, which makes it ideal for use in services and microservices.

Typical usage example:

---------------------------------------

# Sing session

string_signer = StringSigner("My Secret")

session_id = "b801692b-135f-40ff-8f7e-016dc7748c45"
session = {"user_uuid": "67fa3e17-4672-4036-8184-7fbe4c097439"}
encoded_session = base64.urlsafe_b64encode(json.dumps(session).encode()).decode()

signed_session = string_signer.sign(encoded_session)

redis.set(session_id, signed_session)

---------------------------------------

# Unsing session

string_signer = StringSigner("My Secret")

session_id = "b801692b-135f-40ff-8f7e-016dc7748c45"

signed_session = redis.get(session_id)

encoded_session = string_signer.unsign(signed_session)
session = json.loads(base64.urlsafe_b64decode(encoded_session).decode())


---------------------------------------


"""

import base64
import hashlib
import hmac
import re
import secrets
import string
from random import SystemRandom

import _hashlib

from .exceptions import (
    InvalidAlgorithm,
    InvalidSaltLength,
    InvalidSecretKey,
    InvalidSeparator,
    InvalidSignature,
    InvalidSignatureStructure,
    InvalidSignatureType,
    InvalidSignedString,
    InvalidString,
)


class StringSigner:
    """Sign and unsign strings.

    The signed string respects the following format:
        '{_string}{separator}{hash_algorithm}{separator}{salt}{separator}{encoded_signature}'

    Steps to sign a string:
    1. generate a random salt
    2. generate key using salt and secret
    3. generate string signature with key
    4. encode signature
    5. join the string, the hash algorithm used, the generated salt and the encoded signature

    Steps to unsign a signed string:
    1. check if the string is signed
    2. split the signed string to get the hash algorithm, salt and encoded signature
    3. generate key using the secret and extracted salt
    4. generate a new string signature with key
    5. encode the new signature
    6. compare signatures


    Args:
        secret_key (str): The secret that will be used to generate the key to sign the string.
        hash_algorithm (str): The hash algorithm that will be used to generate the signature. Defaults is 'sha256'.
        salt_length (int) = The salt length. Defaults is '8'.
        separator (str) = The separator that will be used in the signed string structure. Defaults is ':'.
        encoding (str) = The encoding that will be used to encode string to bytes. Defaults is 'utf-8'.
        encoding_errors (str) = The encoding error type. Defaults is 'strict'.


    Raises:
        InvalidSecretKey: Invalid secret_key input value.
        InvalidAlgorithm: Invalid hash_algorithm input value.
        InvalidSeparator: Invalid separator input value.
        InvalidSaltLength: Invalid salt length input value.
        InvalidSignatureType: Invalid signature input value.
        InvalidString: Invalid _string input value.
        InvalidSignatureStructure: Invalid signature structure input value.
        InvalidSignedString: Invalid signed_string input value.
        InvalidSignature: Invalid signature.

    Returns:
        string_signer: use to sign or unsing strings.
    """

    __slots__ = (
        "_secret_key",
        "_hash_algorithm",
        "_separator",
        "_salt_length",
        "encoding",
        "encoding_errors",
    )

    SALT_CHARS = string.ascii_letters + string.digits
    NOT_ALLOWED_SEPARATOR_REGEX = re.compile(r"^[A-z0-9-_=]*$")
    SIGNATURE_STRUCTURE = "{_string}{separator}{hash_algorithm}{separator}{salt}{separator}{encoded_signature}"

    def __init__(
        self,
        secret_key: str,
        hash_algorithm: str = "sha256",
        salt_length: int = 8,
        separator: str = ":",
        encoding="utf-8",
        encoding_errors="strict",
    ) -> "StringSigner":
        self._secret_key = None
        self.secret_key = secret_key
        self._hash_algorithm = None
        self.hash_algorithm = hash_algorithm
        self._separator = None
        self.separator = separator
        self._salt_length = None
        self.salt_length = salt_length
        self.encoding = encoding
        self.encoding_errors = encoding_errors

    @property
    def secret_key(self) -> None:
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key: str) -> None:
        if not secret_key:
            raise InvalidSecretKey
        if not isinstance(secret_key, str):
            raise InvalidSecretKey
        self._secret_key = secret_key

    @property
    def hash_algorithm(self) -> str:
        return self._hash_algorithm

    @hash_algorithm.setter
    def hash_algorithm(self, hash_algorithm: str) -> None:
        if hash_algorithm not in hashlib.algorithms_available:
            raise InvalidAlgorithm
        self._hash_algorithm = hash_algorithm

    @property
    def hasher(self) -> _hashlib.HASH:
        return getattr(hashlib, self.hash_algorithm)

    @property
    def separator(self) -> str:
        return self._separator

    @separator.setter
    def separator(self, separator: str) -> None:
        if self.NOT_ALLOWED_SEPARATOR_REGEX.match(separator):
            raise InvalidSeparator
        self._separator = separator

    @property
    def salt_length(self) -> int:
        return self._salt_length

    @salt_length.setter
    def salt_length(self, salt_length: int) -> None:
        if not isinstance(salt_length, int):
            raise InvalidSaltLength

        if salt_length <= 0:
            raise InvalidSaltLength

        self._salt_length = salt_length

    def _string_to_bytes(self, _string: str) -> bytes:
        return _string.encode(self.encoding, self.encoding_errors)

    def _generate_salt(self) -> str:
        salt = ""
        for _ in range(self.salt_length):
            salt += SystemRandom().choice(self.SALT_CHARS)
        return salt

    def _generate_key(self, salt: str) -> bytes:
        secret_key_encoded = self._string_to_bytes(self.secret_key)
        salt_encoded = self._string_to_bytes(salt)
        return hashlib.sha256(secret_key_encoded + salt_encoded).digest()

    def _generate_signature(self, _string: str, key: bytes) -> bytes:
        signature = hmac.new(
            key, self._string_to_bytes(_string), digestmod=self.hasher
        ).digest()
        return signature

    def _encode_signature(self, signature: bytes) -> str:
        if not isinstance(signature, bytes):
            raise InvalidSignatureType
        return base64.urlsafe_b64encode(signature).strip(b"=").decode()

    def _structure_signed_string(
        self, _string: str, salt: str, encoded_signature: str
    ) -> str:
        sig_msg = self.SIGNATURE_STRUCTURE.format(
            _string=_string,
            separator=self.separator,
            hash_algorithm=self.hash_algorithm,
            salt=salt,
            encoded_signature=encoded_signature,
        )
        return sig_msg

    def sign(self, _string: str) -> str:
        f"""This method is used to sign strings.

        The signed string respect the following format:
           {self.SIGNATURE_STRUCTURE}

        Args:
            _string (str): string to be signed.

        Raises:
            InvalidString: Invalid _string input value. It's must be str.

        Returns:
            str: The signed string.
        """
        if not isinstance(_string, str):
            raise InvalidString

        salt = self._generate_salt()
        key = self._generate_key(salt)
        signature = self._generate_signature(_string, key)
        encoded_signature = self._encode_signature(signature)

        signed_string = self._structure_signed_string(_string, salt, encoded_signature)

        return signed_string

    def _check_signature_structure(self, signed_string: str) -> None:

        if self.separator not in signed_string:
            raise InvalidSignatureStructure

        if len(signed_string.split(self.separator)) != 4:
            raise InvalidSignatureStructure

        _, hash_algorithm, *_ = signed_string.split(self.separator)

        if hash_algorithm not in hashlib.algorithms_available:
            raise InvalidAlgorithm

    def is_signed(self, _string: str) -> bool:
        """check if the string is signed.

        Args:
            _string (str): the string to check if it is signed.

        Returns:
            bool:
        """
        try:
            self._check_signature_structure(_string)
            return True
        except InvalidSignatureStructure or InvalidAlgorithm:
            return False

    def unsign(self, signed_string: str) -> str:
        """_summary_

        Args:
            signed_string (str): the string that was signed.

        Raises:
            InvalidSignedString: Invalid signed_string input value. It's must be str.
            InvalidSignatureStructure: Invalid structure of the signed_string.
            InvalidAlgorithm: Invalid hash algorithm in the signed_string.
            InvalidSignature: Invalid signature. The signature does not match.

        Returns:
            str: The string
        """

        if not isinstance(signed_string, str):
            raise InvalidSignedString

        self._check_signature_structure(signed_string)

        _string, hash_algorithm, salt, encoded_signature = signed_string.split(
            self.separator
        )

        self.hash_algorithm = hash_algorithm

        key = self._generate_key(salt)
        new_signature = self._generate_signature(_string, key)
        new_encoded_signature = self._encode_signature(new_signature)

        if not secrets.compare_digest(
            self._string_to_bytes(encoded_signature),
            self._string_to_bytes(new_encoded_signature),
        ):
            raise InvalidSignature

        return _string
