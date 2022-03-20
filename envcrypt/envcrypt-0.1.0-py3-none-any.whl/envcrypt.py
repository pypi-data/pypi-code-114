from dotenv import dotenv_values
from pathlib import Path
from typing import Union, Dict
import hashlib
from base64 import b64encode, b64decode
import os
import re

from Crypto.Cipher import AES


def decrypt_string(ciphertext: str, key: bytes) -> str:
    """Decrypt ciphertext.

    Args:
        ciphertext (str): The encrypted text.
        key (bytes): The key to use to decrypt the ciphertext.

    Returns:
        str: The decrypted text.
    """
    ciphertext = b64decode(ciphertext)
    iv = ciphertext[:AES.block_size]
    aes = AES.new(key, AES.MODE_CFB, iv)
    return aes.decrypt(ciphertext[AES.block_size:])


def encrypt_text(text: str, key: bytes) -> bytes:
    """Encrypt text.

    Args:
        text (str): The text to encrypt.
        key (bytes): THe key used to encrypt the text.

    Returns:
        bytes: The encrypted text.
    """
    iv = os.urandom(AES.block_size)
    aes = AES.new(key, AES.MODE_CFB, iv)
    return b64encode(iv + aes.encrypt(text))

def get_encryption_key(password: str, salt: str) -> bytes:
    """Create a key for encryption/decryption.

    Args:
        password (str): A strong password.
        salt (str): Some random salt.

    Returns:
        bytes: The generated encryption key.
    """
    return hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100_000)


def decrypt_env_file(env_file: Union[str, Path], password: str) -> Dict[str, str]:
    """Load a file with environment variables and decrypt each value.

    Args:
        env_file (Union[str, Path]): The file to load.
        password (str): The password to use for decryption.

    Raises:
        ValueError: If an invalid file path is provided.

    Returns:
        Dict[str, str]: Map of environment variable name to decrypted value.
    """
    if not Path(env_file).is_file():
        raise ValueError(f'Not a valid env file: {env_file}')
    env_vars = dotenv_values(env_file)
    salt = b64decode(env_vars.pop('__'))
    enc_key = get_encryption_key(password, salt)
    for k, v  in env_vars.items():
        env_vars[k] = decrypt_string(v, enc_key).decode()
    return env_vars
    
        
        
def encrypt_env_file(env_file: Union[str, Path], password: str) -> None:
    """Encrypt all values in the given environment variable file.

    Args:
        env_file (Union[str, Path]): The file to encrypt.
        password (str): The password to use for encryption.

    Raises:
        ValueError: If an invalid file path is provided.
    """
    if not (env_file := Path(env_file)).is_file():
        raise ValueError(f'Not a valid env file: {env_file}')
    salt = os.urandom(16)
    enc_key = get_encryption_key(password, salt)
    env_vars = dotenv_values(env_file)
    enc_lines = []
    for k,v in env_vars.items():
        env_vars[k] = encrypt_text(v, enc_key).decode()
    env_vars['__'] = b64encode(salt).decode()
    for k,v in env_vars.items():
        # quote all strings.
        if not re.match(r'\d+(\.\d+)?$', v):
            if not "'" in v:
                v = "'" + v.strip('"') + "'"
            else:
                v = '"' + v.strip('"') + '"'

        enc_lines.append(f"""export {k}={v}""")
    text = '\n'.join(enc_lines)
    print(f"Writing encrypted env file to {env_file}:\n{text}")
    env_file.write_text(text)
