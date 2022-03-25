from django.urls import path
from . import views

app_name = 'fsmedhro_diva'

urlpatterns = [
    path('', views.SendDiva.as_view(), name='send'),
]
