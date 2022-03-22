from enum import Enum

from .convertors.base import SchemaConvertor
from .convertors.vue_formulator import VueFormulateConvertor
from .enum_meta import ChoiceEnum


class SchemaFieldType(str, Enum):
    OBJECT = 'object'
    ARRAY = 'array'
    FIElD = 'field'


class Widget(ChoiceEnum):
    TEXT_INPUT = ('텍스트',)
    NUMBER = ('실수',)
    INTEGER = ('정수',)
    DATE = ('날짜',)
    CHECKBOX = ('체크박스',)
    SELECT = ('콤보박스',)
    TEXTAREA = ('롱 텍스트',)
    JSON = ('JSON',)
    HIDDEN = ('숨김',)
    TOGGLE = ('토글',)
    PASSWORD = ('패스워드',)

    def __init__(self, view_name: str):
        self.view_name = view_name


class UIType(ChoiceEnum):
    VueFormulate = ('VueFormulate', VueFormulateConvertor())

    def __init__(self, display: str, convertor: SchemaConvertor):

        self.display = display
        self.convertor = convertor


class HttpMethod(ChoiceEnum):
    GET = ('get',)
    POST = ('post',)
    PUT = ('put',)
    PATCH = ('patch',)
    DELETE = ('delete',)

    def __init__(self, display: str):
        self.display = display
