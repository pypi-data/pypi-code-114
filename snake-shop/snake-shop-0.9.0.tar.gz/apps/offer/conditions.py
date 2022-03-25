from django.utils.translation import ngettext

delta = int()

ngettext(
    'Buy %(delta)d more product from %(range)s',
    'Buy %(delta)d more products from %(range)s',
    delta
) % {'delta': delta, 'range': None}