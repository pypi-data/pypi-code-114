from django.contrib import admin

from simpel.simpel_products.admin import ProductChildAdmin

from .models import CalibrationService
from .resources import CalibrationServiceResource


@admin.register(CalibrationService)
class CalibrationServiceAdmin(ProductChildAdmin):
    fields = ProductChildAdmin.fields + ["analysis_method", "price"]
    resource_class = CalibrationServiceResource
