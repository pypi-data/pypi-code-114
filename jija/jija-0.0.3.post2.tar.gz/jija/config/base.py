import inspect


class Base:
    INITED = False

    def __init__(self):
        if self.__class__.INITED:
            raise Exception(f'{self.__class__.__name__} already inited')

        self.__class__.INITED = True

    @classmethod
    def clean(cls):
        for key in cls.__dict__:
            if not key.startswith(f'__') and not isinstance(cls.__dict__[key], (staticmethod, classmethod)):
                setattr(cls, key, None)

        cls.INITED = False
