from django.urls import path

from simpel_pages import views

urlpatterns = [
    path("", views.simpelpage, name="simpelpage"),
    path("<path:url>", views.simpelpage, name="simpelpage"),
]
