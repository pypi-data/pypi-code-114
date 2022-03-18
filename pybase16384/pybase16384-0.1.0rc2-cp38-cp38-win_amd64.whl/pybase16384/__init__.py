from io import BytesIO
from ._core import *

__version__ = "0.1.0rc2"


def encode_from_string(data: str, write_head: bool = False) -> bytes:
    inp = BytesIO(data.encode())
    out = BytesIO()
    encode(inp, out, write_head)
    return out.getvalue()


def encode_to_string(data: bytes) -> str:
    inp = BytesIO(data)
    out = BytesIO()
    encode(inp, out)
    return out.getvalue().decode("utf-16-be")


def decode_from_bytes(data: bytes) -> str:
    inp = BytesIO(data)
    out = BytesIO()
    decode(inp, out)
    return out.getvalue().decode()


def decode_from_string(data: str) -> bytes:
    inp = BytesIO(data.encode("utf-16-be"))
    out = BytesIO()
    decode(inp, out)
    return out.getvalue()
