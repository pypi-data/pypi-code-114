from secrets import token_urlsafe


def gen_urlsafe_token(length):
    return token_urlsafe(length)


def create_folder(folder_path, folder_name: str):
    try:
        from os import path
        from os import mkdir
        mkdir(path.join(folder_path, folder_name))
    except FileExistsError:
        pass


def create_file(file_path, file_name: str, file_mode: str = "x", file_content: str = ''):
    try:
        from os import path
        with open(path.join(file_path, file_name), file_mode) as f:
            f.write(file_content)
    except FileExistsError:
        pass
