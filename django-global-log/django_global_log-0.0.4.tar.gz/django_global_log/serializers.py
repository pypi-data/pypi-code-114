from rest_framework import serializers

from django_global_log.models import DjangoGlobalLog


class LogSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoGlobalLog
        fields = "__all__"
