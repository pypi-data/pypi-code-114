import re
from decimal import Decimal, Decimal as D, InvalidOperation

from django import template
from django.apps import apps
from django.conf import settings
from django.templatetags.static import static
from django.utils.formats import number_format
from django.utils.html import format_html
from django.utils.translation import get_language, to_locale

from babel.numbers import format_currency

from simpel.utils import number_to_text_id

from ..settings import simpel_core_settings as core_settings

register = template.Library()


@register.filter(name="currency")
def currency(value, currency=None):
    """
    Format decimal value as currency
    """
    if currency is None:
        currency = core_settings.DEFAULT_CURRENCY
    try:
        value = D(value)
    except (TypeError, InvalidOperation):
        return ""
    # Using Babel's currency formatting
    # http://babel.pocoo.org/en/latest/api/numbers.html#babel.numbers.format_currency
    CURRENCY_FORMAT = core_settings.CURRENCY_FORMAT
    kwargs = {"currency": currency, "locale": to_locale(get_language() or settings.LANGUAGE_CODE)}
    if isinstance(CURRENCY_FORMAT, dict):
        kwargs.update(CURRENCY_FORMAT.get(currency, {}))
    else:
        kwargs["format"] = CURRENCY_FORMAT
    return format_currency(value, **kwargs).strip()


@register.simple_tag
def replace_char(value, old_char, new_char):
    return value.replace(old_char, new_char)


@register.simple_tag(takes_context=True)
def concat_text(context, *args):
    return "".join([str(x) for x in args])


@register.filter(is_safe=True)
def money(value, use_l10n=True):
    """
    Convert an integer to a string containing commas every three digits.
    For example, 3000 becomes '3,000' and 45000 becomes '45,000'.
    """
    if value is None:
        return money(0, use_l10n)
    if settings.USE_L10N and use_l10n:
        try:
            if not isinstance(value, (float, Decimal)):
                value = int(value)
        except (TypeError, ValueError):
            return money(value, False)
        else:
            return number_format(value, decimal_pos=2, force_grouping=True)
    orig = str(value)
    new = re.sub(r"^(-?\d+)(\d{3})", r"\g<1>,\g<2>", orig)
    if orig == new:
        return new
    else:
        return money(new, use_l10n)


@register.filter(is_safe=True)
def point(value):
    """
    Convert an integer to a string containing commas every three digits.
    For example, 3000 becomes '3,000' and 45000 becomes '45,000'.
    """
    return "{:20,.2f}".format(value)


@register.simple_tag(name="sum")
def sum(value1, value2):
    value1 = value1 or 0
    value2 = value2 or 0
    return float(value1) + float(value2)


@register.filter(name="percentof")
def percentof(value1, value2):
    """Return Percent Of"""
    v1 = value1 or 0
    v2 = value2 or 1
    return (v1 / v2) * 100


@register.filter(name="proper_paginate")
def proper_paginate(paginator, current_page, neighbors=3):
    if paginator.num_pages > 2 * neighbors:
        start_index = max(1, current_page - neighbors)
        end_index = min(paginator.num_pages, current_page + neighbors)
        if end_index < start_index + 2 * neighbors:
            end_index = start_index + 2 * neighbors
        elif start_index > end_index - 2 * neighbors:
            start_index = end_index - 2 * neighbors
        if start_index < 1:
            end_index -= start_index
            start_index = 1
        elif end_index > paginator.num_pages:
            start_index -= end_index - paginator.num_pages
            end_index = paginator.num_pages
        page_list = [f for f in range(start_index, end_index + 1)]
        return page_list[: (2 * neighbors + 1)]
    return paginator.page_range


@register.simple_tag(takes_context=True)
def replace_param(context, **kwargs):
    """ """
    d = context["request"].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    for k in [k for k, v in d.items() if not v]:
        del d[k]
    return d.urlencode()


@register.filter(name="number_to_text")
def number_to_text(value):
    number = value or 0
    return number_to_text_id(int(number))


@register.simple_tag(takes_context=True)
def get_model_opts(context, slug):
    model = apps.get_model(slug, require_ready=False)
    return model._meta


@register.simple_tag(takes_context=True)
def django_htmx_script():
    # Copied from django htmx
    # Optimization: whilst the script has no behaviour outside of debug mode,
    # don't include it.
    if not settings.DEBUG:
        return format_html("")
    return format_html(
        '<script type="text/javascript" src="{}" data-debug="{}" defer></script>',
        static("js/django-htmx.js"),
        str(bool(settings.DEBUG)),
    )
