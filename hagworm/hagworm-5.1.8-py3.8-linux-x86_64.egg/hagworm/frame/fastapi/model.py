# -*- coding: utf-8 -*-

__author__ = r'wsb310@gmail.com'

from inspect import Signature, Parameter

from pydantic.main import BaseModel as _BaseModel
from pydantic.main import ModelMetaclass as _ModelMetaclass

from fastapi.params import Param


class ModelMetaclass(_ModelMetaclass):

    def __init__(cls, _what, _bases=None, _dict=None):

        super().__init__(_what, _bases, _dict)

        if cls.__fields__:

            # 原始参数类型清单
            annotations = _dict.get(r'__annotations__', {})

            func_params = []

            for field in cls.__fields__.values():

                # 如果不是Param参数类型的子类，则不写入签名
                if not isinstance(field.field_info, Param):
                    continue

                func_params.append(
                    Parameter(
                        field.name, Parameter.POSITIONAL_OR_KEYWORD,
                        default=field.field_info,
                        annotation=annotations.get(field.name, Parameter.empty)
                    )
                )

            # 更新类方法签名
            cls.dependency = lambda **kwargs: kwargs
            cls.dependency.__signature__ = Signature(func_params)


class BaseModel(_BaseModel, metaclass=ModelMetaclass):

    @staticmethod
    def dependency(**kwargs):
        return kwargs
