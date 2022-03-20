from django.contrib import admin

from simpel.simpel_products.admin import ProductChildAdmin

from .models import ResearchService
from .resources import ResearchServiceResource


@admin.register(ResearchService)
class ResearchServiceAdmin(ProductChildAdmin):
    fields = ProductChildAdmin.fields + ["price"]
    resource_class = ResearchServiceResource
