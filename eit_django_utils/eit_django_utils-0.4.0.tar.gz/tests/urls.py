# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from eit_django_utils.urls import urlpatterns as eit_django_utils_urls

urlpatterns = [url(r"^", include(eit_django_utils_urls, namespace="eit_django_utils"))]
