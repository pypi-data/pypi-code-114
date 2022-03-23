from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ImproperlyConfigured

from simpel_hookup import core as hookup

from .models import Product
from .settings import products_settings


def get_product_models():
    # Get default products child models from settings
    child_models = products_settings.PRODUCT_TYPES

    # Get products child models from hooks
    funcs = hookup.get_hooks("REGISTER_PRODUCT_CHILD_MODELS")
    registered_child_models = [func() for func in funcs]

    for child_model in registered_child_models:
        if issubclass(child_model, Product):
            if child_model not in child_models:
                child_models.append(child_model)
            else:
                pass
        else:
            raise ImproperlyConfigured("Hook REGISTER_PRODUCT_MODEL should return Product subclass")

    return child_models


def get_product_states():
    models = get_product_models()
    states = dict()
    for model in models:
        model_type = ContentType.objects.get_for_model(model)
        queryset = Product.objects.filter(polymorphic_ctype=model_type.id)
        count = queryset.count()
        model_key = "%s.%s" % (model_type.app_label, model_type.model)
        states.update(
            {
                model_key: {
                    "count": count,
                },
            }
        )
    return states
