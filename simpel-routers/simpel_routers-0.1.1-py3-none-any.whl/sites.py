from django.contrib.auth import views
from django.urls import path
from django.utils.translation import gettext_lazy as _

import simpel_hookup.core as hookup

from .routers import DefaultIndexView, DefaultRouter, SimpleRouter
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


class AuthenticationRouter(SimpleRouter):
    namespace = "account"

    def get_urls(self):

        urls = super().get_urls()
        urls += [
            path("login/", views.LoginView.as_view(redirect_authenticated_user=True), name="login"),
            path("logout/", views.LogoutView.as_view(), name="logout"),
            path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
            path("password_reset/done/", views.PasswordResetDoneView.as_view(), name="password_reset_done"),
            path("reset/<uidb64>/<token>/", views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
            path("reset/done/", views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
            path("password_change/", views.PasswordChangeView.as_view(), name="password_change"),
            path("password_change/done/", views.PasswordChangeDoneView.as_view(), name="password_change_done"),
        ]
        return urls


class DashboardRouter(DefaultRouter):
    namespace = "dashboard"
    index_view_class = IndexView
    site_title = routers_settings.DASHBOARD_TITLE
    site_header = routers_settings.DASHBOARD_HEADER
    index_template_name = "dashboard/index.html"
    site_view_hook_name = "REGISTER_DASHBOARD_VIEW"
    site_path_hook_name = "REGISTER_DASHBOARD_PATH"


class WebsiteRouter(DefaultRouter):
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
