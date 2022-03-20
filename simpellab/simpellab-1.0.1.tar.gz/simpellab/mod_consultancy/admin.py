from django.contrib import admin

from simpel.simpel_products.admin import ProductChildAdmin

from .models import ConsultancyService
from .resources import ConsultancyServiceResource


@admin.register(ConsultancyService)
class ConsultancyServiceAdmin(ProductChildAdmin):
    fields = ProductChildAdmin.fields + ["price"]
    resource_class = ConsultancyServiceResource
