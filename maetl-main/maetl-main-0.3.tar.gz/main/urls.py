from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',  views.dashboard, name='dashboard'),
    path('login/', views.CustomLoginView.as_view(redirect_authenticated_user = True,template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),

   path('exportdata',views.ExportData, name='exportdata'),
   path('exportdadussuku',views.ExportDadusSuku, name='exportdadussuku'),
]