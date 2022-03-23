from django.urls import path

from .viewset import FormSchemaGeneratorAPI, ModelChoicesAPI

app_name = 'form_schema'


urlpatterns = [
    path('form-schema-generate/', FormSchemaGeneratorAPI.as_view(), name='generate'),
    path('model-list/', ModelChoicesAPI.as_view(), name='model_choices'),
    path('model-list2/', ModelChoicesAPI.as_view(), name='model_choices2')
]

