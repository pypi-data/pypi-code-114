from django.conf import settings
from django.contrib import admin

from mptt.admin import DraggableMPTTAdmin

from simpel_employs import get_profile_model

from .models import Chair, Department, Employee, Employment, Position
from .settings import employs_settings


class DepartmentAdmin(DraggableMPTTAdmin):
    search_fields = ["name"]


class EmploymentAdmin(admin.ModelAdmin):
    search_fields = ["name"]


class PositionAdmin(DraggableMPTTAdmin):
    search_fields = ["name"]
    list_filter = ["is_manager", "is_co_manager", "is_active"]


class ChairInline(admin.TabularInline):
    extra = 0
    model = Chair
    autocomplete_fields = ["employee", "position"]


class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ["eid"]
    raw_id_fields = ["employment", "profile"]
    list_display = ["eid", "profile", "employment", "date_registered", "is_active"]
    inlines = [ChairInline]


admin.site.register(Employment, employs_settings.EMPLOYMENT_ADMIN)
admin.site.register(Department, employs_settings.DEPARTMENT_ADMIN)
admin.site.register(Position, employs_settings.POSITION_ADMIN)
admin.site.register(Employee, employs_settings.EMPLOYEE_ADMIN)

if settings.PROFILE_MODEL == "simpel_employs.Profile":

    class ProfileAdmin(admin.ModelAdmin):
        list_display = ["full_name", "employee"]
        search_fields = ["full_name", "employee_id"]

    admin.site.register(get_profile_model(), ProfileAdmin)
