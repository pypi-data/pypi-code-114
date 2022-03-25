from django import template
from django.db.models import Q
from apps.catalogue.models import Category

register = template.Library()


@register.simple_tag
def category_pov_menu(pov_category):
    """
    get self and descendants
    """
    qs = Category.objects.browsable()
    if not pov_category:
        return qs.filter(depth=1)

    path = pov_category.path
    parents_and_self = [pov_category.path]

    while len(path) > 4:
        path = path[:-4]
        parents_and_self.append(path)
    parents_and_self = sorted(parents_and_self, key=lambda x: len(x))

    filter_parent_siblings = Q(path__startswith=pov_category.path, depth=pov_category.depth+1)
    for element in parents_and_self:
        filter_parent_siblings |= Q(path__startswith=element[:-4], depth=len(element) / 4)

    qs = qs.filter(filter_parent_siblings)
    return qs.order_by('path', 'depth')
