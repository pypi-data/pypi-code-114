from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from huscy.project_design import serializer, services
from huscy.projects.models import Project


class DataAcquisitionMethodViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin,
                                   mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = services.get_data_acquisition_methods()
    serializer_class = serializer.DataAcquisitionMethodSerializer
    permission_classes = (IsAuthenticated, )


class ExperimentViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin,
                        mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = serializer.ExperimentSerializer
    permission_classes = (IsAuthenticated, )

    def initial(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, pk=self.kwargs['project_pk'])
        super().initial(request, *args, **kwargs)

    def get_queryset(self):
        return services.get_experiments(self.project)

    def perform_create(self, serializer):
        serializer.save(project=self.project)


class SessionViewSet(viewsets.ModelViewSet):
    queryset = services.get_sessions()
    serializer_class = serializer.SessionSerializer
    permission_classes = (IsAuthenticated, )
