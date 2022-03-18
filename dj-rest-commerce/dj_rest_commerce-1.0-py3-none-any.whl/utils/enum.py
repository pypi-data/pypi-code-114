from enum import IntEnum


class TYPES(IntEnum):
    KG = 0
    PCS = 1
    BOX = 2

    @classmethod
    def select_types(cls):
        return [(key.value, key.name) for key in cls]


class STATUS(IntEnum):
    PENDING = 0
    CANCEL = 1
    FAILED = 2
    PROCESSING = 3
    DELIVERY = 4
    DONE = 5

    @classmethod
    def order_status(cls):
        return [(key.value, key.name) for key in cls]


class PAYMENT(IntEnum):
    CASH_ON_DELIVERY = 0
    BKASH = 1
    NOGOD = 2
    BANK = 3

    @classmethod
    def payment_choices(cls):
        return [(key.value, key.name) for key in cls]
