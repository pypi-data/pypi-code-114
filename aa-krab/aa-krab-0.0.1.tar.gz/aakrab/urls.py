from django.conf.urls import url

from . import views

app_name: str = "aakrab"

urlpatterns = [
    url(r"^$", views.aakrab_view, name="aakrab_view")
]
