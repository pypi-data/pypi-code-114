from rest_framework import serializers

SESSION_CART_ID = "cart"


class JSONPolymorphicChildBase(serializers.Serializer):
    uid = serializers.CharField(required=False)
    type = serializers.CharField()


class JSONPolymorphicSerializer(serializers.Serializer):
    type_field_name = "type"
    object_serializers_map = None

    def to_internal_value(self, data):
        resource_type = self._get_resource_type_from_mapping(data)
        serializer = self._get_serializer_from_type(resource_type)
        ret = serializer.to_internal_value(data)
        ret[self.type_field_name] = resource_type
        return ret

    def to_representation(self, instance):
        resource_type = self._get_resource_type_from_mapping(instance)
        serializer = self._get_serializer_from_type(resource_type)
        ret = serializer.to_representation(instance)
        ret[self.type_field_name] = resource_type
        return ret

    def _get_resource_type_from_mapping(self, mapping):
        try:
            return mapping[self.type_field_name]
        except KeyError:
            raise serializers.ValidationError(
                {
                    self.type_field_name: "This field is required",
                }
            )

    def _get_serializer_from_type(self, resource_type):
        serializer = self.object_serializers_map[resource_type]
        return serializer
