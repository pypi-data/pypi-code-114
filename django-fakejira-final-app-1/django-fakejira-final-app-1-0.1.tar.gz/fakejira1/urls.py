from django.urls import path
from . import views


urlpatterns = [
    path('fakejira-admin/', views.main, name='fakejira_admin'),
    path('manage-users/', views.manage_users, name='manage_users'),
    path('shippings/', views.shippings, name='shippings'),
    path('view_shipping/<str:pk>/', views.view_shipping, name='view_shipping'),
    path('create-shipping/', views.create_shipping, name='create_shipping'),
    path('add_new_shipping/', views.add_new_shipping, name='add_new_shipping'),
    path('update_shipping/<str:pk>/', views.update_shipping, name='update_shipping'),
    path('delete_shipping/<str:pk>/', views.delete_shipping, name='delete_shipping'),
    path('bulk_delete_shippings/', views.bulk_delete_shippings, name='bulk_delete_shippings'),
    path('fakejira-login/', views.login_view, name='login_view'),
    path('singin/', views.login, name='login'),
    path('logout_view/', views.logout_view, name='logout_view'),
]