from tornado.web import RequestHandler
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from urllib.parse import urlencode
from base.django_handler_mixin import DjangoHandlerMixin
from django.conf import settings

from .models import Customer


class Proxy(DjangoHandlerMixin, RequestHandler):
    async def post(self, relative_url):
        self.user = self.get_current_user()
        if not self.user.is_authenticated:
            self.set_status(401)
            self.finish()
            return
        if relative_url == "update_subscription":
            customer = Customer.objects.filter(user=self.user).first()
            if not customer:
                self.set_status(404)
                self.finish()
                return
            post_data = {
                "plan_id": self.get_argument("plan_id"),
                "vendor_id": settings.PADDLE_VENDOR_ID,
                "vendor_auth_code": settings.PADDLE_API_KEY,
                "subscription_id": customer.subscription_id,
            }
            body = urlencode(post_data)
            http = AsyncHTTPClient()
            response = await http.fetch(
                HTTPRequest(
                    (
                        "https://vendors.paddle.com/api/2.0/"
                        "subscription/users/update"
                    ),
                    "POST",
                    None,
                    body,
                    request_timeout=40.0,
                )
            )
            self.write(response.body)
            self.finish()
