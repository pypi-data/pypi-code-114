from rest_framework import serializers

from huscy.project_design.models import DataAcquisitionMethod, Experiment, Session
from huscy.project_design.services import (
    add_data_acquisition_method,
    create_experiment,
    create_session,
)


class DataAcquisitionMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataAcquisitionMethod
        fields = (
            'id',
            'location',
            'order',
            'session',
            'type',
        )

    def create(self, validated_data):
        return add_data_acquisition_method(**validated_data)


class SessionSerializer(serializers.ModelSerializer):
    order = serializers.IntegerField(required=False)
    title = serializers.CharField(required=False)

    class Meta:
        model = Session
        fields = (
            'duration',
            'experiment',
            'id',
            'operator',
            'order',
            'title',
        )

    def create(self, validated_data):
        return create_session(**validated_data)

    def to_representation(self, session):
        response = super().to_representation(session)
        response['data_acquisition_methods'] = \
            DataAcquisitionMethodSerializer(session.dataacquisitionmethod_set.all(), many=True).data
        return response


class ExperimentSerializer(serializers.ModelSerializer):
    order = serializers.IntegerField(required=False)
    title = serializers.CharField(required=False)

    class Meta:
        model = Experiment
        fields = (
            'description',
            'id',
            'order',
            'project',
            'title',
        )
        read_only_fields = 'project',

    def create(self, validated_data):
        return create_experiment(**validated_data)

    def to_representation(self, experiment):
        response = super().to_representation(experiment)
        response['sessions'] = SessionSerializer(experiment.sessions.all(), many=True).data
        return response
