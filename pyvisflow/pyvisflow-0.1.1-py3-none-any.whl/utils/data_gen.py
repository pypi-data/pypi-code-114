

from pathlib import Path
_global_id = 0


def get_global_id():
    global _global_id
    _global_id += 1
    return str(_global_id)


_m_project_root = Path(__file__).absolute().parent.parent


def get_project_root():
    return _m_project_root
