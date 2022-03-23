from sys import stderr

ENC_HEADER = b"AES256"


def write_to_file(output_file, nonce, tag, ciphertext):
    output_file.write(ENC_HEADER)
    output_file.write(nonce)
    output_file.write(tag)
    output_file.write(ciphertext)


def read_from_file(input_file):
    header, nonce, tag, ciphertext = [
        input_file.read(x) for x in (len(ENC_HEADER), 16, 16, -1)
    ]
    return header, nonce, tag, ciphertext
    if header != ENC_HEADER:
        print(f"Got unexpected header {ENC_HEADER}", file=stderr)
        exit(3)
