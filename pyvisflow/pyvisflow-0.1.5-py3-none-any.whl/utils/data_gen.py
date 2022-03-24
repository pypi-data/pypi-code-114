from pathlib import Path
from json import JSONEncoder, dumps
from functools import partial
import pandas as pd

_global_id = 0


def get_global_id():
    global _global_id
    _global_id += 1
    return str(_global_id)


_m_project_root = Path(__file__).absolute().parent.parent


def get_project_root():
    return _m_project_root


def _nan2None(obj):
    if isinstance(obj, dict):
        return {k: _nan2None(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [_nan2None(v) for v in obj]
    elif isinstance(obj, float) and pd.isna(obj):
        return None
    return obj


class _NanConverter(JSONEncoder):
    def default(self, obj):
        # possible other customizations here
        pass

    def encode(self, obj, *args, **kwargs):
        obj = _nan2None(obj)
        return super().encode(obj, *args, **kwargs)

    def iterencode(self, obj, *args, **kwargs):
        obj = _nan2None(obj)
        return super().iterencode(obj, *args, **kwargs)


json_dumps_fn = partial(dumps, cls=_NanConverter)