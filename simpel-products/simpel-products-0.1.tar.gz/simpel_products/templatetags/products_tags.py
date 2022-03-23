from django.template import Library

from simpel_utils.currency import currency as crc

register = Library()


@register.filter
def currency(val, currency=None):
    return crc(val, currency=None)
