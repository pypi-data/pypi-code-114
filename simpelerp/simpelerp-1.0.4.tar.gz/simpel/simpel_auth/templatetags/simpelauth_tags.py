from django import template
from django.utils.safestring import mark_safe

from ..utils import render_notice

register = template.Library()


@register.simple_tag(takes_context=True)
def notice(context, notice):
    request = context["request"]
    return mark_safe(render_notice(request, notice))
