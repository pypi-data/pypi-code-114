from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, mixins, permissions, viewsets

from huscy.attributes import models, serializer, services
from huscy.attributes.permissions import AttributeSetPermission
from huscy.subjects.models import Subject


class AttributeSchemaView(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                          generics.GenericAPIView):
    permission_classes = (permissions.DjangoModelPermissions, )
    queryset = models.AttributeSchema.objects.all()
    serializer_class = serializer.AttributeSchemaSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_object(self):
        return services.get_attribute_schema()


class AttributeSetViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                          viewsets.GenericViewSet):
    permission_classes = (permissions.IsAuthenticated, AttributeSetPermission)
    queryset = Subject.objects.all()
    serializer_class = serializer.AttributeSetSerializer

    def get_object(self):
        subject = super().get_object()
        attribute_set = services.get_or_create_attribute_set(subject)
        services.filter_attributes_by_category_permissions(attribute_set, self.request.user)
        return attribute_set

    def perform_update(self, serializer):
        attribute_schema = serializer.validated_data['attribute_schema']
        for node, node_description in attribute_schema.schema['properties'].items():
            if (node in serializer.validated_data['attributes'] and
                    node_description['type'] == 'object' and
                    len(serializer.validated_data['attributes'][node]) and
                    not self.request.user.has_perm(f'attributes.change_attribute_category_{node}')):
                raise PermissionDenied('You don\'t have the permission to update attribute '
                                       f'category {node}')
        super().perform_update(serializer)
