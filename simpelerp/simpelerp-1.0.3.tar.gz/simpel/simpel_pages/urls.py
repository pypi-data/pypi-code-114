from django.urls import path

from simpel.simpel_pages import views

urlpatterns = [
    path("", views.simpelpage, name="simpel_simpelpage"),
    path("<path:url>", views.simpelpage, name="simpel_simpelpage"),
]
