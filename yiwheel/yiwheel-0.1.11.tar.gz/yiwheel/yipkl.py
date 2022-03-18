import zipfile
try:
    import _pickle
except:
    import pickle as _pickle

import os


def dict_to_zip(dir_path: str, file_name: str, data_dict: dict) -> None:
    """
    压缩一个 dict 到 zip
    :param dir_path: <str>
    :param file_name: <str> 不带 .zip 后缀的文件名
    :param data_dict: dict
    """
    file_path = os.path.join(dir_path, file_name) + '.zip'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)
    with zipfile.ZipFile(file_path, 'w', zipfile.ZIP_DEFLATED) as f:
        f.writestr(file_name + '.pkl', _pickle.dumps(data_dict))


def zip_to_dict(dir_path: str, file_name: str) -> dict or None:
    """
    解压缩一个 zip 到 dict
    :param dir_path: <str> 目录名
    :param file_name: <str> 不带 .zip 后缀的文件名
    """
    file_path = os.path.join(dir_path, file_name)
    try:
        with zipfile.ZipFile(file_path + '.zip', 'r') as f:
            return _pickle.loads(f.open(file_name + '.pkl').read())
    except Exception as e:
        return None