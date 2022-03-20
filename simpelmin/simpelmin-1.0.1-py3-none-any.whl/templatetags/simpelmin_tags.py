from django import template
from django.contrib.admin import site
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from django_atomics import Div
from django_hookup import core as hookup

from simpel.utils import reverse_lazy
from simpelmin import __version__
from simpelmin.components import MenuItem, SidenavMenuGroup, SubMenuItem

from ..components import AccountMenu

register = template.Library()


@register.inclusion_tag(takes_context=True, filename="admin/admin_menu.html")
def render_admin_menu(context, classnames=None):
    request = context["request"]
    menus = [func(request) for func in hookup.get_hooks("REGISTER_ADMIN_MENU")]
    # lambda x: x["order"]
    return {"classnames": classnames, "menus": sorted(menus)}


@register.simple_tag(takes_context=True)
def render_app_sections(context, app_label, classnames=None):
    request = context["request"]
    hookname = "REGISTER_ADMIN_APP_SECTION"
    sections = ""
    for func in hookup.get_hooks(hookname):
        app, component = func(request)
        if app == app_label:
            sections += component

    return mark_safe(sections)


@register.simple_tag(takes_context=True)
def get_app_list(context, app_label=None):
    request = context["request"]
    app_dict = site.get_app_list(request)
    return app_dict


@register.simple_tag(name="simpelmin_sidenav_menu", takes_context=True)
def simpelmin_sidenav_menu(context):
    request = context["request"]
    menu_items = [
        MenuItem(
            label=_("Home"),
            icon="home-variant-outline",
            url=reverse_lazy("admin:index"),
        ),
    ]
    funcs = hookup.get_hooks("REGISTER_ADMIN_SIDENAV_MENU")
    menu_items += [func(request) for func in funcs]
    # Add App List
    app_dict = site.get_app_list(request)
    for app in app_dict:
        model_menus = []
        for model in app["models"]:
            model_menus.append(
                SubMenuItem(
                    label=model["name"].title(),
                    icon=model["icon"],
                    url=model["admin_url"] or "#",
                )
            )
        menu_items.append(
            SidenavMenuGroup(
                name=app["app_label"],
                label=app["name"],
                icon=app["icon"],
                childs=model_menus,
            )
        )
    account_menu = Div(childs=menu_items)
    return mark_safe(account_menu.render(context={"request": request}))


@register.simple_tag(name="simpelmin_version")
def simpelmin_version():
    return "Simpelmin v.%s" % __version__


@register.simple_tag(name="simpelmin_account_menu", takes_context=True)
def simpelmin_account_menu(context):
    request = context["request"]
    funcs = hookup.get_hooks("REGISTER_ADMIN_ACCOUNT_MENU")
    menu_items = []
    if request.user.is_superuser or request.user.has_setting_perm:
        menu_items.append(
            SubMenuItem(
                label=_("Update Settings"),
                icon="cog-outline",
                url=reverse_lazy("admin:settings"),
            )
        )
    menu_items += [
        SubMenuItem(
            label=_("Change Password"),
            icon="lock-outline",
            url=reverse_lazy("admin:password_change"),
        ),
        SubMenuItem(
            label=_("Logout"),
            icon="logout-variant",
            url=reverse_lazy("admin:logout"),
        ),
    ]
    menu_items += [func(request) for func in funcs]

    account_menu = AccountMenu(
        name="account_menu",
        label=_("My Account"),
        icon="account-circle-outline",
        childs=menu_items,
    )
    return mark_safe(account_menu.render(context={"request": request}))
