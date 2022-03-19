from typing import get_type_hints, get_origin, get_args, Union, List
from enum import Enum


class InitAttrsWKwArgs:
    @staticmethod
    def _convert_option_name_to_attr_name(name: str) -> str:
        if name.startswith('--'):
            ns = name[2:]
        elif name.startswith('-'):
            ns = name[1:]
        elif name.startswith('<') and name.endswith('>'):
            ns = name[1:-1]
        else:
            ns = name
        ns = ns.replace('-', '_')
        
        if not(len(ns) > 0 and ('a' <= ns[0] <= 'z' or 'A' <= ns[0] <= 'Z') and \
                all('a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9' or c == '_' for c in ns)):
            raise NameError("Invalid name for option or positional argument: %s" % repr(name))

        return ns

    @staticmethod
    def _convert_str_value(value: str, target_type):
        if issubclass(target_type, bool):
            return not not value
        elif issubclass(target_type, int):
            return int(value)
        elif issubclass(target_type, float):
            return float(value)
        elif issubclass(target_type, Enum):
            try:
                return target_type[value]  # conversion from str to Enum (it might not look so)
            except KeyError as e:
                raise ValueError('Invalid Enum name: %s' % repr(value)) from e
        else:
            return value  # not converted

    def __init__(self, _cast_str_values=False, **kwargs):
        attr_to_type = get_type_hints(self.__class__)
        for name in kwargs:
            attr = InitAttrsWKwArgs._convert_option_name_to_attr_name(name)
            t = attr_to_type.get(attr)
            if t is None:
                raise KeyError("attribute `%s` not found in class `%s`" % (repr(attr), repr(self.__class__)))
            v = kwargs[name]
            if _cast_str_values:
                ot = get_origin(t)
                if isinstance(v, list) and ot is list:
                    it = get_args(t)[0]
                    v = [(InitAttrsWKwArgs._convert_str_value(vi, it) if isinstance(vi, str) else vi) for vi in v]
                elif isinstance(v, str):
                    if ot is Union:  # handle such as Optional[str], Optional[int], etc.
                        ts = get_args(t)
                        if len(ts) == 2:
                            if ts[0] is type(None):
                                v = InitAttrsWKwArgs._convert_str_value(v, ts[1])
                            elif ts[1] is type(None):
                                v = InitAttrsWKwArgs._convert_str_value(v, ts[0])
                    else:
                        v = InitAttrsWKwArgs._convert_str_value(v, t)
            setattr(self, attr, v)
    
    def __repr__(self) -> str:
        return "%s(%s)" % (
            self.__class__.__name__, 
            ', '.join("%s=%s" % (a, repr(getattr(self, a))) for a in get_type_hints(self.__class__).keys()))

