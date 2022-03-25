from django.urls import path
from django.urls import include
from oscarapi import urls
from rest_framework.routers import DefaultRouter
from .views.sync import sync_router


urlpatterns = urls.urlpatterns + [
    path('sync/', include((sync_router.urls, 'sync-api'), namespace='sync-api')),
]
