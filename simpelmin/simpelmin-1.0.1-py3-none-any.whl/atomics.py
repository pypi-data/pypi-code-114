from django.urls import reverse
from django.utils.translation import gettext as _
from django_hookup import core as hookup

from django_atomics import Component, ListItem, UnOrderedList


class AdminMenuItem(ListItem):
    template_string = """
    <li {% if attrs %}{{ attrs }}{% endif %}
         {% if style %}style="{{ style }}"{% endif %}
         {% if classes %}class="{{ classes }}"{% endif %}>
            <a {{ link_attrs }} {% if link_classes %}class="{{ link_classes }}"{% endif %} href="{{ url }}">
                {% if icon %}<i class="mdi mdi-{{ icon }}"></i>{% endif%}
                {{ label }}
            </a>
            {{ childs }}
        </li>
    """


class AdminMenu(UnOrderedList):
    template_string = """
    <ul {% if attrs %}{{ attrs }}{% endif %}
         class="module border bg-light p-5px m-5px {% if classes %}{{ classes }}{% endif %}">{{ childs }}</ul>
    """

    def get_child_objects(self, parent_context):
        request = parent_context["request"]
        childs = [func(request) for func in hookup.get_hooks("REGISTER_ADMIN_MENU")]
        return [
            AdminMenuItem(
                url=reverse("admin:index"),
                icon="home-variant",
                label=_("Home"),
            )
        ] + childs


class AdminAppSection(Component):
    template_name = "admin/app_section.html"
    title = "Admin Section Title"

    def __init__(self, classes=None, attrs=None, style=None, childs=None, **initial_context):
        initial_context.setdefault("title", self.title)
        super().__init__(classes, attrs, style, childs, **initial_context)


class AdminHeaderChips(Component):
    template_name = "admin/atomics/header_chip.html"

    def __init__(self, order=0, classes=None, attrs=None, style=None, childs=None, **initial_context):
        super().__init__(classes, attrs, style, childs, **initial_context)
