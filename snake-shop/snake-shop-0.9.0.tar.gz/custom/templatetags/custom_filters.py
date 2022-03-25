from decimal import Decimal as D
from decimal import InvalidOperation

from babel.numbers import format_currency
from django import template
from django.conf import settings
from django.utils.translation import get_language, to_locale

register = template.Library()


@register.filter(name='pc')
def float_to_pc(value, decimal_places=None):
    """
    This converts a factor to its percentage value
    decimal_places is None : no changes of decimal place number
    decimal_places is str('x') : quantize String
    decimal_places > 0 : Number of decimal places
    """
    if value is None:
        return value

    value = D(value) * 100
    if decimal_places is None:
        return value
    
    elif isinstance(decimal_places, str):
        quantize_str = decimal_places

    elif decimal_places == 0:
        quantize_str = '1'

    elif decimal_places > 0:
        quantize_str = '.{}1'.format((decimal_places-1)*'0')

    return value.quantize(D(quantize_str))
