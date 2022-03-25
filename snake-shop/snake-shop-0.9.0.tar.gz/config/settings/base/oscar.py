from decimal import Decimal as D
from django.utils.translation import gettext_lazy as _
from oscar.defaults import *


__all__ = ('OSCAR_SHOP_NAME', 'OSCAR_HOMEPAGE', 'OSCAR_DEFAULT_CURRENCY',
           'OSCAR_ALLOW_ANON_CHECKOUT', 'OSCAR_SEND_REGISTRATION_EMAIL',
           'OSCAR_FROM_EMAIL', 'CHANGELOG_FROM_EMAIL', 'OSCAR_URL_SCHEMA',
           'OSCAR_PRODUCT_SEARCH_HANDLER', 'OSCAR_OFFERS_INCL_TAX',
           'OSCAR_HIDDEN_FEATURES', 'OSCAR_REQUIRED_ADDRESS_FIELDS',
           'OSCAR_PRODUCTS_PER_PAGE', 'OSCAR_PRODUCTS_PER_PAGE_AJAX',
           'OSCAR_OFFERS_PER_PAGE', 'OSCAR_ORDER_STATUS_PIPELINE',
           'OSCAR_MISSING_IMAGE_URL', 'OSCAR_OFFER_ROUNDING_FUNCTION',
           'oscar_round', 'OSCAR_PRODUCT_SEARCH_HANDLER', 'DEFAULT_TAX_RATE',
           'HAYSTACK_CONNECTIONS', 'OSCAR_ATTACHED_PRODUCT_FIELDS',
           'OSCAR_DETAILS_DISABLED_FIELDS', 'OSCAR_SEARCH_DISABLED_FIELDS')


OSCAR_SHOP_NAME = 'Shop'
OSCAR_HOMEPAGE = reverse_lazy('home')
OSCAR_DEFAULT_CURRENCY = 'EUR'
OSCAR_ALLOW_ANON_CHECKOUT = False
OSCAR_SEND_REGISTRATION_EMAIL = True
CHANGELOG_FROM_EMAIL = OSCAR_FROM_EMAIL
OSCAR_URL_SCHEMA = 'http'
OSCAR_PRODUCT_SEARCH_HANDLER = None
OSCAR_OFFERS_INCL_TAX = True
OSCAR_HIDDEN_FEATURES = ['reviews']
OSCAR_REQUIRED_ADDRESS_FIELDS = [*OSCAR_REQUIRED_ADDRESS_FIELDS] + ['phone_number']
OSCAR_REQUIRED_ADDRESS_FIELDS.remove('country')
DEFAULT_TAX_RATE = D('0.19')


# Lazy Loading
# BUG: When using different for page and ajax
OSCAR_PRODUCTS_PER_PAGE = 0
OSCAR_PRODUCTS_PER_PAGE_AJAX = 12

OSCAR_OFFERS_PER_PAGE = OSCAR_PRODUCTS_PER_PAGE
OSCAR_ORDER_STATUS_PIPELINE = {
    'Frei': ('Versand', 'Abholung'),
    'Abholung': ('Erledigt', 'Storno'),
    'Versand': ('Erledigt', 'Storno'),
    'Erledigt': (),
    'Storno': (),
}

def oscar_round(price, currency=None):
    return price.quantize(D('0.00'))

OSCAR_OFFER_ROUNDING_FUNCTION = 'config.settings.base.oscar.oscar_round'
OSCAR_PRODUCT_SEARCH_HANDLER = 'oscar_pg_search.postgres_search_handler.PostgresSearchHandler'
HAYSTACK_CONNECTIONS = {"default": {}}

OSCAR_ATTACHED_PRODUCT_FIELDS = [
    'volume', 'weight', 'manufacturer', 'reusability', 'deposit', 'tax', 'container_count',
]
OSCAR_DETAILS_DISABLED_FIELDS = ['deposit', 'reusability']
OSCAR_SEARCH_DISABLED_FIELDS = ['deposit', 'tax']
