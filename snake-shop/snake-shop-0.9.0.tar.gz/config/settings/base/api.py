

__all__ = ('OSCARAPI_OVERRIDE_MODULES', 'REST_FRAMEWORK')


OSCARAPI_OVERRIDE_MODULES = ["api"]
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}
