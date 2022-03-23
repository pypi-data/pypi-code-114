from django.contrib.auth.decorators import login_required
from django.urls import include, re_path

from .sites import dashboard, website
from .utils import decorator_include

urlpatterns = [
    re_path(r"^", include(website.urls)),
    re_path(
        r"^dashboard/",
        decorator_include([login_required], dashboard.urls),
    ),
]
