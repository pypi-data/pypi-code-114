from django.conf import settings

is_maintenance = getattr(settings, "MAINTENANCE", False)


class MaintenanceMiddleware:
    """Simply copied form Django"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        from simpel.simpel_core.views import MaintenanceView

        if is_maintenance and not request.user.is_superuser:
            return MaintenanceView.as_view()(request).render()
        return self.get_response(request)
