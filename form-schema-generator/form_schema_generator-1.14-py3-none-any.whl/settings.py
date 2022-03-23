from django.conf import settings

form_schema_generator_settings = {
    'MODEL_CHOICES_API': 'api:form_schema:model_choices'
    # TODO: 초이스 기본값 셀렉트, 라디오 변경가능하도록 옵션제공하기
}

form_schema_generator_settings.update(getattr(settings, 'FORM_SCHEMA_GENERATOR_SETTINGS'))
