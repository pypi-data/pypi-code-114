"""This module was created to encode and decode data in a a web-friendly format.

It's only uses building libraries, therefore, it has no external dependency.
It is also lightweight and thread-safe, which makes it ideal for use in services and microservices.

By default WebEncoder will try to compress the data.
If it manages to compress the data, the encoded data started with '.'.

Typical usage example:

---------------------------------------

# Encode session

web_encoder = WebEncoder()

session_id = "b801692b-135f-40ff-8f7e-016dc7748c45"
session = {"user_uuid": "67fa3e17-4672-4036-8184-7fbe4c097439"}
encoded_session = web_encoder.encode(json.dumps(session))

redis.set(session_id, encoded_session)

---------------------------------------

# Decode session

web_encoder = WebEncoder()

session_id = "b801692b-135f-40ff-8f7e-016dc7748c45"
encoded_session = redis.get(session_id)
session = json.loads(web_encoder.decode(encoded_session))

---------------------------------------

"""

import base64
import sys
import zlib

from .exceptions import (
    CannotBeCompressed,
    CannotBeDecompressed,
    DataDecodeError,
    InvalidBytesType,
    InvalidDataType,
    InvalidEncodedDataType,
    InvalidStringType,
)


class WebEncoder:
    """Use to encode and decode data in a web-friendly format.


    By default WebEncoder will try to compress the data.
    If it manages to compress the data, the encoded data started with '.'.

    Steps to compress and encode the data:
        1. Turn the data into bytes
        2. Try to compress the data
    If the data has been compressed and the compressed size is smaller than the originals:
        3.1 Encode the compressed data with base64 url safe method
        3.2 A '.' is added at the beginning of the encoded data.
        3.3 The encoded data is turn to str
    Else:
        3.1 Encode the original data with base64 url safe method
        3.2 The encoded data is turn to str


    Args:
        encoding (str) = The encoding that will be used to encode string to bytes. Defaults is 'utf-8'.
        encoding_errors (str) = The encoding error type. Defaults is 'strict'.


    Raises:
        InvalidStringType: Invelid input type. It should be a str type.
        InvalidBytesType:  Invelid input type. It should be a bytes type.
        DataDecodeError: Error when trying to convert string to bytes.
        CannotBeCompressed: Error thrown when compressed file is larger than original.
        InvalidDataType: Invelid input type. It should be a str type.
        InvalidEncodedDataType: Invelid input type. It should be a str type.

    Returns:
        web_encoder: WebEncoder instance.
    """

    __slots__ = ("_compression_signal", "encoding", "encoding_errors")

    def __init__(self, encoding="utf-8", encoding_errors="strict") -> "WebEncoder":
        self._compression_signal = b"."
        self.encoding = encoding
        self.encoding_errors = encoding_errors

    def _string_to_bytes(self, _string: str) -> bytes:
        if not isinstance(_string, str):
            raise InvalidStringType

        return _string.encode(self.encoding, self.encoding_errors)

    def _bytes_to_string(self, _bytes: bytes) -> str:
        if not isinstance(_bytes, bytes):
            raise InvalidBytesType

        try:
            return _bytes.decode(self.encoding, self.encoding_errors)

        except UnicodeDecodeError:
            raise DataDecodeError

    def _base64_urlsafe_encode(self, _bytes: bytes) -> bytes:
        if not isinstance(_bytes, bytes):
            raise InvalidBytesType

        return base64.urlsafe_b64encode(_bytes).strip(b"=")

    def _base64_urlsafe_decode(self, _bytes: bytes) -> bytes:
        if not isinstance(_bytes, bytes):
            raise InvalidBytesType

        pad = b"=" * (-len(_bytes) % 4)
        return base64.urlsafe_b64decode(_bytes + pad)

    def _compress_data(self, _bytes: bytes) -> bytes:
        if not isinstance(_bytes, bytes):
            raise InvalidBytesType

        compressed_bytes = zlib.compress(_bytes)
        compressed_bytes_size = sys.getsizeof(compressed_bytes)
        _bytes_size = sys.getsizeof(_bytes)

        if compressed_bytes_size < _bytes_size:
            return compressed_bytes
        else:
            raise CannotBeCompressed

    def _decompress_data(self, compressed_bytes: bytes) -> bytes:
        if not isinstance(compressed_bytes, bytes):
            raise InvalidBytesType

        try:
            return zlib.decompress(compressed_bytes)
        except zlib.error:
            raise CannotBeDecompressed

    def encode(self, data: str, compress=True) -> str:
        """Use to encode data in a web-friendly format.

        Args:
            data (str): data to be encoded.
            compress (bool, optional): Try to compress the data befor encode. Defaults to True.

        Raises:
            InvalidDataType: The input data should be str type.

        Returns:
            str: encoded_data
        """

        if not isinstance(data, str):
            raise InvalidDataType

        data = self._string_to_bytes(data)

        if compress:
            try:
                compressed_data = self._compress_data(data)
                encoded_data = self._base64_urlsafe_encode(compressed_data)
                encoded_data = self._compression_signal + encoded_data
            except CannotBeCompressed:
                encoded_data = self._base64_urlsafe_encode(data)
        else:
            encoded_data = self._base64_urlsafe_encode(data)

        return self._bytes_to_string(encoded_data)

    def decode(self, encoded_data: str) -> str:
        """Use to decode data.

        Args:
            encoded_data (str): data that was encoded with the encode method of the class.

        Raises:
            InvalidEncodedDataType: The input encoded_data should be str type.

        Returns:
            str: decoded_data
        """

        if not isinstance(encoded_data, str):
            raise InvalidEncodedDataType

        encoded_data = self._string_to_bytes(encoded_data)

        if encoded_data[:1] == self._compression_signal:
            decoded_data = self._base64_urlsafe_decode(encoded_data[1::])
            decoded_data = zlib.decompress(decoded_data)
        else:
            decoded_data = self._base64_urlsafe_decode(encoded_data)

        return self._bytes_to_string(decoded_data)
