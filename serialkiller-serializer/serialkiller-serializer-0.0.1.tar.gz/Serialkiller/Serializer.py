from Serialkiller.exc.SerializationError import SerializationError
from Serialkiller.exc.DeserializationError import DeserializationError

from functools import partial


class Serializer:
    __slots__ = 'serialize', 'deserialize', 'serialize_many', 'deserialize_many'

    def __init__(self, cls, only=None, ignore=None):
        self.serialize = partial(self.serialize_, only=only, ignore=ignore)
        self.deserialize = partial(self.deserialize_, cls=cls)
        self.serialize_many = partial(self.serialize_many_, only=only, ignore=ignore)
        self.deserialize_many = partial(self.deserialize_many_, cls=cls)

    @staticmethod
    def serialize_(obj, only=None, ignore=None):
        try:
            if only is not None:
                fields = set(only)

            else:
                fields = set(obj.__fields__)

            if ignore is not None:
                for item in ignore:
                    fields.discard(item)

            return dict(
                map(lambda field: (field, obj.__dict__[field]), fields)
            )

        except KeyError as err:
            raise SerializationError(f'Field {err} is not an attribute of object')

    @staticmethod
    def serialize_many_(obj_iterable, only=None, ignore=None):
        return map(partial(Serializer.serialize_, only=only, ignore=ignore), obj_iterable)

    @staticmethod
    def deserialize_(obj_dict, cls, init_args=None):
        if init_args is None:
            init_args = []

        try:
            obj = cls(*init_args)

        except Exception as err:
            raise DeserializationError(f'Failed to deserialize: {str(err)}')

        try:
            for key, value in obj_dict.items():
                if key in obj.__dict__:
                    obj.__dict__[key] = value

            return obj

        except KeyError as err:
            raise DeserializationError(f'Field {err} is not an attribute of object')

    @staticmethod
    def deserialize_many_(dict_iterable, cls, init_args=None):
        return map(partial(Serializer.deserialize_, cls=cls, init_args=init_args), dict_iterable)
