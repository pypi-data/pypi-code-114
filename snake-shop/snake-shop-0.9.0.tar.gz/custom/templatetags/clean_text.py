from string import ascii_lowercase, ascii_uppercase
from django import template

register = template.Library()


DIGITS = '0123456789'
PUNCTUATION = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
WHITESPACE = ' \t\n\r\v\f'


@register.filter
def base_chars(value):
    """
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyzöäüß'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÖÄÜ'
    """
    usable_chars = ''.join([
        ascii_lowercase + 'öäüß',
        ascii_uppercase + 'ÖÄÜ',
        DIGITS,
        PUNCTUATION,
        WHITESPACE,
    ])
    return ''.join([char for char in value if char in usable_chars])
