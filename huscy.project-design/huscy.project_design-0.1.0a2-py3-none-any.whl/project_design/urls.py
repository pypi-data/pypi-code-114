from rest_framework_nested.routers import DefaultRouter

from huscy.project_design import views
from huscy.projects.urls import project_router


router = DefaultRouter()
router.register('dataacquisitionmethods', views.DataAcquisitionMethodViewSet)
router.register('sessions', views.SessionViewSet)

project_router.register('experiments', views.ExperimentViewSet, basename='experiment')

urlpatterns = []
urlpatterns += router.urls
urlpatterns += project_router.urls
