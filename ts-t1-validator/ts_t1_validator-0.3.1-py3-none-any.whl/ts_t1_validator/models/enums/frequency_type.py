from ts_t1_validator.models.enums.abstract_enum import AbstractEnum


class FrequencyTypeEnum(AbstractEnum):
    EVEN = "even"
    ASAP = "asap"
    NO_LIMIT = "no-limit"
    UNDEFINED = None
