from django.utils.translation import ugettext_lazy as _

from . import urls

from allianceauth import hooks
from allianceauth.services.hooks import MenuItemHook, UrlHook


class AAKrabMenuItem(MenuItemHook):  # pylint: disable=too-few-public-methods
    """ This class ensures only authorized users will see the menu entry """

    def __init__(self):
        # setup menu entry for sidebar
        MenuItemHook.__init__(
            self,
            _("Krab Fleet Tracking"),
            "fas fa-crosshairs fa-fw",
            "aakrab:aakrab_view",
            navactive=["aakrab:"],
        )

    def render(self, request):
        """
        only if the user has access to this app
        :param request:
        :return:
        """

        if request.user.has_perm("imicusfat.basic_access"):
            return MenuItemHook.render(self, request)

        return ""


@hooks.register("menu_item_hook")
def register_menu():
    """
    register our menu
    :return:
    """

    return AAKrabMenuItem()


@hooks.register("url_hook")
def register_url():
    """
    register our menu link
    :return:
    """

    return UrlHook(urls, "imicusfat", r"^imicusfat/")
