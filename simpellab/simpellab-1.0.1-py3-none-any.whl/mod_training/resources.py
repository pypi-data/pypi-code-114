from import_export.resources import ModelResource

from simpel.simpel_products.resources import ProductResourceBase, product_fields

from .models import TrainingService, TrainingTopic


class TrainingServiceResource(ProductResourceBase):
    class Meta:
        model = TrainingService
        fields = product_fields + ["audience_criterias", "price"]
        export_order = product_fields + ["audience_criterias", "price"]
        import_id_fields = ("inner_id",)


class TrainingTopicResource(ModelResource):
    class Meta:
        model = TrainingTopic
