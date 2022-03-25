from decimal import Decimal as D
from datetime import date


def clean(element, data_type=str):
    if data_type is str:
        result = data_type(element.strip())

    elif data_type is date:
        result = date(data_type) if element else None

    elif data_type is int:
        element = ''.join(
            [char for char in element if char in '0123456789']
        )
        result = int(element) if element is 0 or element else None

    elif data_type is bool:
        result = bool(element)

    elif data_type is D:
        result = D(element.replace(',', '.')) if element else D('0.00')

    return result

