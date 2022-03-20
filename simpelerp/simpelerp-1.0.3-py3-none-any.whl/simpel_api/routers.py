from django.core.exceptions import ImproperlyConfigured
from django.urls import path
from django_hookup import core as hookup
from rest_framework.routers import DefaultRouter
from rest_framework.views import APIView

viewset_hooks = hookup.get_hooks("REGISTER_API_VIEWSET")
apiview_hooks = hookup.get_hooks("REGISTER_API_VIEW")


def get_router():
    router = DefaultRouter()
    for func in viewset_hooks:
        hook = func()
        router.register("%s" % hook["prefix"], hook["viewset"], hook["basename"])
        # remove username reset
        if hook["prefix"] == "users":
            bads = [
                "reset-username",
                "reset-username-confirm",
                "reset-email",
                "reset-email-confirm",
                "set-username",
            ]
            router._urls = [r for r in router.urls if not any(r.name.endswith(bad) for bad in bads)]
    return router


def get_apiview():
    urlpatterns = []
    for hook in apiview_hooks:
        url_path, apiview, name = hook()
        if not issubclass(apiview, APIView):
            raise ImproperlyConfigured("%s must subclass of DRF APIView")
        if name:
            url = path(url_path, apiview.as_view(), name=name)
        else:
            url = path(url_path, apiview.as_view(), name=apiview.__class__.__name__.lower())
        urlpatterns.append(url)
    return urlpatterns


app_name = "v1"

urlpatterns = get_apiview() + get_router().urls
