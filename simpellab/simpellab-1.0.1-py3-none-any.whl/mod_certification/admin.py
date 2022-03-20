from django.contrib import admin

from simpel.simpel_products.admin import ProductChildAdmin

from .models import CertificationService
from .resources import CertificationServiceResource


@admin.register(CertificationService)
class CertificationServiceAdmin(ProductChildAdmin):
    fields = ProductChildAdmin.fields + ["price"]
    resource_class = CertificationServiceResource
