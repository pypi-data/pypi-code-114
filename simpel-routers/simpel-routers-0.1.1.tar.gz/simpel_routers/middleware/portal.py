from ..settings import routers_settings


class MaintenanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        from ..views import MaintenanceView

        if routers_settings.MAINTENANCE_MODE_FORCE:
            return MaintenanceView.as_view()(request).render()
        return self.get_response(request)
