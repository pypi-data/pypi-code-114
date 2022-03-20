from django.utils.safestring import mark_safe
from django_atomics import Component
from django_hookup import core as hookup


class Section(Component):
    template_string = "<section class='section-{{ name }}'>{{ childs }}</section>"


class SidenavMenu(Component):
    template_string = "{{ childs }}"

    def get_childs(self, parent_context):
        request = parent_context.get("request")
        funcs = hookup.get_hooks("REGISTER_SIDEMENU_ITEM")
        menu_items = [func(request) for func in funcs]
        childs = self.childs + [item for item in menu_items if item.is_shown(parent_context)]
        rendered_childs = ""
        for child in childs:
            rendered_childs += child.render(context=parent_context)
        return mark_safe(rendered_childs)


class SidenavMenuGroup(Component):
    template_name = "admin/components/sidenav_menu_group.html"


class AccountMenu(SidenavMenuGroup):
    template_name = "admin/components/sidenav_menu_account.html"

    def get_childs(self, parent_context):
        request = parent_context.get("request")
        funcs = hookup.get_hooks("REGISTER_ACCOUNTMENU_ITEM")
        menu_items = [func(request) for func in funcs]
        childs = self.childs + [item for item in menu_items if item.is_shown(parent_context)]
        rendered_childs = ""
        for child in childs:
            rendered_childs += child.render(context=parent_context)
        return mark_safe(rendered_childs)


class MenuItem(Component):
    template_name = "admin/components/sidenav_menu_item.html"


class SubMenuItem(Component):
    template_name = "admin/components/sidenav_submenu_item.html"
