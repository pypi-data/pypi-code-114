from django.conf import settings
from django_grpc_swagger.serializers import SerializerHandler

__all__ = ['serializer_handler']

PACKAGE = settings.GRPC_SWAGGER_SETTINGS["package"]
ADD_GRPC_PREFIX = settings.GRPC_SWAGGER_SETTINGS.get("add_grpc_prefix", False)
BASE_DIR = settings.BASE_DIR

serializer_handler = SerializerHandler(PACKAGE, ADD_GRPC_PREFIX)
