from django.conf.urls import url

from . import views

urlpatterns = [
    url("^get_paddle_info/$", views.get_paddle_info, name="get_paddle_info"),
    url(
        "^get_subscription_details/$",
        views.get_subscription_details,
        name="get_subscription_details",
    ),
    url("webhook/$", views.webhook, name="webhook"),
]
