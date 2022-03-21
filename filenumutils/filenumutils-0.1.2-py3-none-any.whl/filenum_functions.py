import os
from filenumutils.helper_functions import _get_pattern, _get_str_number_list, _get_number_list


def get_last_file_number(path: str = os.getcwd(), prefix: str = '', suffix: str = '', folder: bool = False) -> int:
    root, folders, files = next(os.walk(path))
    pattern = _get_pattern(prefix, suffix)
    number_list = _get_number_list(pattern, folders if folder else files)
    return max(number_list) if len(number_list) > 0 else -1


def get_last_folder_number(path: str = os.getcwd(), prefix: str = '', suffix: str = '') -> int:
    return get_last_file_number(path=path, prefix=prefix, suffix=suffix, folder=True)


def get_next_file(path: str = None, prefix: str = '', suffix: str = '',
                  create: bool = False, default_number_width: int = 2,
                  folder: bool = False, full_path: bool = False) -> str:

    # Store original parameter to see if path parameter was passed later
    original_path_passed = path
    if path is None:
        path = os.getcwd()
    else:
        if not os.path.exists(path):
            raise ValueError(f'Given path "{path}" does not exist!')

    root, folders, files = next(os.walk(path))
    pattern = _get_pattern(prefix, suffix)

    # find last file number but also get str number list
    # hence get_last_file_number is not used
    str_number_list = _get_str_number_list(pattern, folders if folder else files)
    number_list = [int(number) for number in str_number_list]
    max_number = max(number_list) if len(number_list) > 0 else -1

    # find last file number length for padding zeros
    strings_of_max_number = [len(str_number) for str_number in str_number_list if int(str_number) == max_number]
    number_length = max(strings_of_max_number) if len(strings_of_max_number) > 0 else default_number_width

    # Create file or folder if required
    filename = ('{}{:0' + str(number_length) + 'd}{}').format(prefix, max_number + 1, suffix)
    full_path_filename = os.path.join(path, filename)
    if create:
        if folder:
            os.makedirs(full_path_filename, exist_ok=True)
        else:
            with open(full_path_filename, 'w'):
                pass

    if full_path and original_path_passed is not None:
        return full_path_filename

    # if full_path is false
    # or if original_path_passed is None
    else:
        return filename


def get_next_folder(path: str = os.getcwd(), prefix: str = '', suffix: str = '',
                    create: bool = False, full_path: bool = False) -> str:
    return get_next_file(path, prefix, suffix, create=create, folder=True, full_path=full_path)
