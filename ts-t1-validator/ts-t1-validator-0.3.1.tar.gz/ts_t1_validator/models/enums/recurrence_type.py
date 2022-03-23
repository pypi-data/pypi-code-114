from ts_t1_validator.models.enums.abstract_enum import AbstractEnum


class RecurrenceTypeEnum(AbstractEnum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    UNDEFINED = None
