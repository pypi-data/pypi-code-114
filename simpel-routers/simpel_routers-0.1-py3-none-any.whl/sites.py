from django.utils.translation import gettext_lazy as _

import simpel_hookup.core as hookup

from .routers import DefaultIndexView, Site
from .settings import routers_settings


class IndexView(DefaultIndexView):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_template_names(self):
        return super().get_template_names()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"title": _("Simpellab")})
        return context


class DashboardRouter(Site):
    namespace = "dashboard"
    index_view_class = IndexView
    site_title = routers_settings.DASHBOARD_TITLE
    site_header = routers_settings.DASHBOARD_HEADER
    index_template_name = "dashboard/index.html"
    site_view_hook_name = "REGISTER_DASHBOARD_VIEW"
    site_path_hook_name = "REGISTER_DASHBOARD_PATH"


class WebsiteRouter(Site):
    namespace = "website"
    index_template_name = "website/index.html"
    index_enabled = routers_settings.WEBSITE_INDEX_ENABLED
    site_title = routers_settings.WEBSITE_TITLE
    site_header = routers_settings.WEBSITE_HEADER
    site_view_hook_name = "REGISTER_WEBSITE_VIEW"
    site_path_hook_name = "REGISTER_WEBSITE_PATH"


def get_router(router_class, hook_name):
    router = router_class()
    viewsets = [func() for func in hookup.get_hooks(hook_name)]
    for viewset in viewsets:
        router.register(viewset)
    return router


website = get_router(WebsiteRouter, "REGISTER_WEBSITE_VIEWSET")
dashboard = get_router(DashboardRouter, "REGISTER_DASHBOARD_VIEWSET")
