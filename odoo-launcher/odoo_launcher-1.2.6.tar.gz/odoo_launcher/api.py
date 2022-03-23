import abc
import sys
from collections import OrderedDict
from typing import Any, Dict, Union

if sys.version_info[0] == 2:  # Python 2

    class ABC(object):
        __meta_class__ = abc.ABCMeta
        __slots__ = ()

else:
    ABC = abc.ABC


class Dictable(ABC):
    def to_dict(self):
        # type: () -> Dict[str, Any]
        raise NotImplementedError()

    @staticmethod
    def clean_config_dict(values):
        # type: (Union[Dict[str, Any], Dictable]) -> Dict[str, str]
        new_values = OrderedDict()
        if isinstance(values, Dictable):
            values = values.to_dict()

        for key, value in values.items():
            if isinstance(value, dict):
                value = Dictable.clean_config_dict(value)
            elif isinstance(value, (list, tuple, set)):
                value = ",".join([str(x) for x in value]) or ""
            if value and value is not None and not isinstance(value, dict):
                new_values[key] = str(value)
        return new_values

    @staticmethod
    def clean_none_env_vars(dict_value):
        # type: (Union[Dict[str, Any], Dictable]) -> Dict[str, Any]
        result = OrderedDict()
        if isinstance(dict_value, Dictable):
            dict_value = dict_value.to_dict()

        for key, value in dict_value.items():
            if value is not None:
                result[key] = value
        return result


class ConfigConvert(ABC):
    def is_true(self, any):
        # type: (Union[str, bool, int, None]) -> bool
        if not any or not isinstance(any, (str, bool, int)):
            return False
        return bool(any) and (str(any).isdigit() and bool(int(any))) or (str(any).capitalize() == str(True)) or False

    def to_int(self, any):
        # type: (Union[str, bool, int, None]) -> int
        if not any or not isinstance(any, (str, bool, int)):
            return 0
        if isinstance(any, str):
            return any.isdigit() and int(any) or "." in any and int(float(any)) or 0
        return int(any)


class EnvMapper(ConfigConvert):
    def map_vars(self, env_vars):
        # type: (Dict[str, str]) -> Dict[str, str]
        raise NotImplementedError()


class OdooConfigABC(ConfigConvert, ABC):
    def __init__(self, main_instance=True):
        super(OdooConfigABC, self).__init__()
        self.main_instance = main_instance

    @property
    def odoo_version(self):
        raise NotImplementedError


class OdooConfigSection(ConfigConvert, Dictable, ABC):
    def __init__(self, odoo_config_maker, env_vars):
        # type: (OdooConfigABC, Dict[str, Union[str, bool, int, None]]) -> None
        self.config_maker = odoo_config_maker
        self.enable = True

    def to_dict(self):
        # type: () -> Dict[str, Any]
        if not self.enable:
            return {}
        return self.get_info()
