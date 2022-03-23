from rest_framework import serializers

from .enums import UIType, HttpMethod
from .generator import FORM_GENERATABLE_URLS


class FieldsRetrieveSerializer(serializers.Serializer):
    url = serializers.ChoiceField(choices=FORM_GENERATABLE_URLS)
    method = serializers.ChoiceField(choices=HttpMethod.choices)
    field = serializers.ChoiceField(choices=UIType.choices, default='pk')

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    #기본적으로는 choices의 내용을 기반으로하고, overide해서 대상 endpoint 를 바꿀 수 있도록 제공
    @classmethod
    def get_declared_field_choices(cls, field_name):
        field = cls._declared_fields.get(field_name)
        choices = getattr(field, 'choices')
        return choices


