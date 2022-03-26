# -*- coding: utf-8 -*-

from pip_services3_commons.convert import TypeCode
from pip_services3_commons.validate import ObjectSchema


class FireMapUpdateV1Schema(ObjectSchema):

    def __init__(self):
        super().__init__()

        self.with_optional_property('type', TypeCode.String)
        self.with_required_property('time', TypeCode.String)
        self.with_required_property('drone_id', TypeCode.String)
        self.with_required_property('long', TypeCode.Float)
        self.with_required_property('lat', TypeCode.Float)
        self.with_optional_property('people', TypeCode.Integer)
