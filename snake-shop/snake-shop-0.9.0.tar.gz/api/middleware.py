from django.conf import settings
from oscarapi import middleware


class ApiGatewayMiddleWare(middleware.ApiGatewayMiddleWare):
    def __call__(self, request):
        if request.user.is_superuser:
            return self.get_response(request)

        return super().__call__(request)
