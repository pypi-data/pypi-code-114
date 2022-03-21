from django.urls import path, include
from django.utils.module_loading import autodiscover_modules

from rest_framework import routers


class GASDRFSite:
    def __init__(self):
        self._registry = {}
        self.autodiscover_done = False
        self.router = routers.DefaultRouter()

    def register(self, *args, **kwargs):
        """
            Register urls to the site router. Compared to normal urls,
            these are not exposed when gas is not active.

            It takes the same arguments as DefaultRouter.register.
        """
        self.router.register(*args, **kwargs)

    @property
    def urls(self):
        return self.router.urls

    def autodiscover(self):
        if not self.autodiscover_done:
            autodiscover_modules('gas.drf_config', register_to=drfsite)
            self.autodiscover_done = True


drfsite = GASDRFSite()
