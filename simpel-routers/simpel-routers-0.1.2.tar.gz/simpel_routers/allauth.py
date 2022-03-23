from django.urls import include
from django.urls.conf import path

from .routers import SimpleRouter


class AuthenticationRouter(SimpleRouter):
    namespace = "accounts"
    index_enabled = False

    def get_urls(self):
        urls = []
        try:
            from allauth.account import views as allviews

            urls += [
                path("signup/", allviews.signup, name="account_signup"),
                path("login/", allviews.login, name="account_login"),
                path("logout/", allviews.logout, name="account_logout"),
                path(
                    "%s/" % self.namespace,
                    include("simpel.simpel_auth.urls.account"),
                ),
            ]
        except ImportError as err:
            print(err)
        return urls
