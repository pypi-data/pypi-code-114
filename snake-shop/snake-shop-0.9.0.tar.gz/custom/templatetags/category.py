from django import template

from oscar.core.loading import get_model
from django.db.models import Case, BooleanField, Value, When

register = template.Library()
Category = get_model("catalogue", "category")


@register.simple_tag(name="menu_objects", takes_context=True)   # noqa: C901 too complex
def menu_objects(context):
    # return Category.objects.filter(depth='1', is_public=True)
    # annotate active and parent_active
    qs = Category.objects.filter(depth=1, is_public=True)
    if 'category' in context and context['category'].path:
        qs = qs.annotate(
            active=Case(
                When(path=context['category'].path, then=Value(True)),
                default=Value(False),
                output_field=BooleanField(),
            )
        )
        qs = qs.annotate(
            active_ancestor=Case(
                When(path=context['category'].path[:4], then=Value(True)),
                default=Value(False),
                output_field=BooleanField(),
            )
        )
    return qs
