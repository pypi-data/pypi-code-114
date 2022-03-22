from ts_t1_validator.models.enums.abstract_enum import AbstractEnum


class ImpressionPacingTypeEnum(AbstractEnum):
    EVEN = "even"
    ASAP = "asap"
    NO_LIMIT = "no-limit"
    UNDEFINED = None
