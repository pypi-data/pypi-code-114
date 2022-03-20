from django.contrib import admin

from mptt.admin import DraggableMPTTAdmin

from .models import Chair, Department, Employee, Employment, Position
from .settings import simpel_employs_settings as employs_settings


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
    raw_id_fields = ["employment"]
    inlines = [ChairInline]


admin.site.register(Employment, employs_settings.EMPLOYMENT_ADMIN)
admin.site.register(Department, employs_settings.DEPARTMENT_ADMIN)
admin.site.register(Position, employs_settings.POSITION_ADMIN)
admin.site.register(Employee, employs_settings.EMPLOYEE_ADMIN)
