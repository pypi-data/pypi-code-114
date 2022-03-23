import base64


def trans_b64_to_file(b64, file_path):
    data = base64.b64decode(b64)
    with open(file_path, 'wb') as fp:
        fp.write(data)


if __name__ == '__main__':
    pass