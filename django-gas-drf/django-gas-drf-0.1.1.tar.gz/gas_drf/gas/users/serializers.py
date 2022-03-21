from django.contrib.auth.models import User

from rest_framework import serializers

from gas.sites import site


class UserRoleField(serializers.MultipleChoiceField):
    def to_representation(self, value):
        return {
            self.choice_strings_to_values.get(str(item), item) for item in value.all()
        }


class UserSerializer(serializers.ModelSerializer):
    user_roles = UserRoleField(
        allow_empty=True,
        choices=site.role_choices,
    )
    password = serializers.CharField(required=False, write_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'username', 'email', 'is_active',
            'password', 'is_staff', 'date_joined', 'user_roles',
        )
        read_only_fields = (
            'is_staff', 'date_joined',
        )
        hidden_fields = ('password',)

    def create(self, validated_data):
        user = User()
        return self.update(user, validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        roles = validated_data.pop('user_roles')

        for field, value in validated_data.items():
            setattr(instance, field, value)
        if password:
            instance.set_password(password)
        instance.save()

        for role in roles:
            instance.user_roles.update_or_create(role=role)
        instance.user_roles.exclude(role__in=roles).delete()
        return instance
