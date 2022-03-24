from django.urls import path
from .views import HotKeyListView, call_python

urlpatterns = [
    path('', HotKeyListView.as_view()),
    path('callpython', call_python)
]