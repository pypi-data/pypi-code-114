import hashlib
import base64
def get_md5(file_path):
    h = hashlib.md5()
    h.update(open(file_path, 'rb').read())

    return h.hexdigest()


def get_base64(file_path):
    return base64.b64encode(open(file_path, 'rb').read()).decode("utf-8")
