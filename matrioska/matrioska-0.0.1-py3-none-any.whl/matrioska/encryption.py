from pathlib import Path
from sys import stderr, stdin, stdout
from Cryptodome.Cipher import AES
from .file import read_from_file, write_to_file


def encrypt(
    input_filename: str, output_filename: str, force: bool, encryption_key=None
):

    cipher = AES.new(encryption_key, AES.MODE_EAX)
    if input_filename:
        with open(input_filename, "rb") as input_file:
            data = input_file.read()
    else:
        data = stdin.buffer.read()
    ciphertext, tag = cipher.encrypt_and_digest(data)

    if output_filename:
        if Path(output_filename).exists() and not force:
            print(f"{output_filename} already exists!", file=stderr)
            exit(1)

        with open(output_filename, "wb") as output_file:
            write_to_file(output_file, cipher.nonce, tag, ciphertext)
    else:
        write_to_file(stdout.buffer, cipher.nonce, tag, ciphertext)


def decrypt(
    input_filename: str, output_filename: str, force: bool, encryption_key=None
):

    if input_filename:
        with open(input_filename, "rb") as input_file:
            header, nonce, tag, ciphertext = read_from_file(input_file)
    else:
        header, nonce, tag, ciphertext = read_from_file(stdin.buffer)

    cipher = AES.new(encryption_key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    if output_filename:
        if Path(output_filename).exists() and not force:
            print(f"{output_filename} already exists!", file=stderr)
            exit(1)
        with open(output_filename, "wb") as output_file:
            output_file.write(data)
    else:
        output_file = stdout.buffer
        output_file.write(data)
