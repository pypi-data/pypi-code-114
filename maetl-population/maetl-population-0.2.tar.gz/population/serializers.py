from rest_framework import serializers
from django.contrib.auth import password_validation
from django.contrib.auth.models import User



class User(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password')
        extra_kwargs = {'password' : { 'write_only': True }}


# class PerfilSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Family
#         fields = ('id_family')





