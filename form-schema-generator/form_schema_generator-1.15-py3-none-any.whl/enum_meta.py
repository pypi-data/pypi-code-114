import copy
from collections import OrderedDict
from enum import EnumMeta, Enum


class ChoiceEnumMeta(EnumMeta):

    @property
    def choices(cls):
        return OrderedDict([(instance.name, instance.value[0]) for instance in cls])

    def to_dict(cls):
        result: dict = {}
        for instance in cls:
            instance_info: dict = copy.deepcopy(instance.__dict__)
            del instance_info['__objclass__']
            result[instance.name] = instance_info
        return result


class ChoiceEnum(Enum, metaclass=ChoiceEnumMeta):
    pass