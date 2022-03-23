from django.contrib import admin
from employee.models import *
from django.contrib.auth.models import User

from import_export import resources

from import_export.admin import ImportExportModelAdmin


class EmployeeResource(resources.ModelResource):
    class Meta:
        model = Employee
class EmployeeAdmin(ImportExportModelAdmin):
    resource_class = EmployeeResource
admin.site.register(Employee, EmployeeAdmin)

class EmployeeUserResource(resources.ModelResource):
    class Meta:
        model = EmployeeUser
class EmployeeUserAdmin(ImportExportModelAdmin):
    resource_class = EmployeeUserResource
admin.site.register(EmployeeUser, EmployeeUserAdmin)

class UserResource(resources.ModelResource):
    class Meta:
        model = User
class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
