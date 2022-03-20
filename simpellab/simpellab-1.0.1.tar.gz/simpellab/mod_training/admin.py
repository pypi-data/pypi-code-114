from django.contrib import admin

from simpel.simpel_products.admin import ProductChildAdmin

from .models import TrainingService, TrainingTopic
from .resources import TrainingServiceResource


class TrainingTopicInline(admin.StackedInline):
    extra = 0
    model = TrainingTopic


@admin.register(TrainingService)
class TrainingServiceAdmin(ProductChildAdmin):
    fields = ProductChildAdmin.fields + ["audience_criterias", "price"]
    inlines = ProductChildAdmin.inlines + [TrainingTopicInline]
    resource_class = TrainingServiceResource
