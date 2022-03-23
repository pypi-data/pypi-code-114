from base64 import b64decode, b64encode
from os import environ
from sys import stderr
from Cryptodome.Random import get_random_bytes


def get_encryption_key(key_env):
    if not key_env:
        print(
            "ERROR: Encryption key environment variable name must be provided using -k",
            file=stderr,
        )
        exit(2)
    try:
        key_value = environ[key_env]
    except KeyError:
        print(f"ERROR: Environment var {key_env} is not defined", file=stderr)
        exit(2)
    bin_key_value = b64decode(key_value)
    if len(bin_key_value) != 32:
        print(
            f"ERROR: Value provided at {key_env} is not at 32 bytes value", file=stderr
        )
        exit(2)
    return bin_key_value


def generate_random_key(b64_encoded=False):
    key = get_random_bytes(32)  # AES256
    if b64_encoded:
        return b64encode(key).decode()
    return key
