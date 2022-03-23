from ts_t1_validator.models.enums.abstract_enum import AbstractEnum


class DimensionActionEnum(AbstractEnum):
    ADD = "add"
    REMOVE = "remove"
    OVERWRITE = "overwrite"
    UNDEFINED = None
