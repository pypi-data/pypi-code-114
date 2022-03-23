from ts_t1_validator.models.enums.abstract_enum import AbstractEnum


class FrequencyIntervalEnum(AbstractEnum):
    HOUR = "hour"
    DAILY = "day"
    WEEKLY = "week"
    MONTH = "month"
    NOTAPPLICABLE = "not-applicable"
    UNDEFINED = None
