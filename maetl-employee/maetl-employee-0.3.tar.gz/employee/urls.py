from django.urls import path

from employee import views
app_name = 'employee'
urlpatterns = [
    path('', views.AdminEmployeeDashboard, name='admin-employee-dashboard'),
    path('add/', views.AdminEmployeeAdd, name='admin-employee-add'),
    path('lists/xefe/', views.AdminListXefe, name='admin-employee-list-xefe'),
    path('lists/sec/', views.AdminListSec, name='admin-employee-list-sec'),
    #USER MANAGEMENT
    path('account/', views.AccountUpdate, name='user-account'),
    path('change/password/', views.UserPasswordChangeView.as_view(), name='user-change-password'),
    path('change/password/done/', views.UserPasswordChangeDoneView.as_view(), name='user-change-password-done'),
    #EMPLOYEE
    path('detail/<str:hashid>/', views.EmployeeDetail, name="employee-detail"),
    path('update/<str:hashid>/', views.EmployeeUpdate, name="employee-update"),
    path('terminate/<str:hashid>/', views.EmployeeTerminate, name="employee-terminate"),
    # CHART
    path('xefe-charts/', views.xefe_charts, name="xefe-charts"),
    path('sec-charts/', views.sec_charts, name="sec-charts"),
    # path('activity-charts/', views.activity_charts, name="activity-charts"),
]
