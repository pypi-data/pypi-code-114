from datetime import datetime, timedelta
from django.test import override_settings, TestCase, RequestFactory
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.urls import reverse
from django.utils import timezone
from re import compile

import json

from eit_django_utils.urls import *
from eit_django_utils.views import *

from eit_django_utils.backends.custom_auth import (
    SetLocalDevShibUID,
    CustomRemoteUserBackend,
    CustomHijackMiddleware,
    CustomHeaderMiddleware,
    LoginRequiredMiddleware,
    SpecialGroupRequiredMiddleware,
)

from .test_shared import EitDjangoUtilsBaseTest


class TestAuthcheck(EitDjangoUtilsBaseTest):
    def test_authcheck(self):
        response = self.client.get(reverse("eit_django_utils:authcheck"))
        self.assertEqual(response.status_code, 200)

    def test_authcheck_time(self):
        request = RequestFactory().get(reverse("eit_django_utils:authcheck"))
        request.META["SHIB_UID"] = "jdoe1"
        request.META["Shib-Authentication-Instant"] = datetime.strftime(
            timezone.now(), "%Y-%m-%dT%H:%M:%S.%fZ"
        )
        view = authcheck
        response = view(request)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        # print("json: {}".format(data))
        self.assertEquals(data.get("shib_uid"), "jdoe1")
        self.assertGreaterEqual(data.get("shib_authentication_minutes_remaining", 0), 599)

    def test_authcheck_time_past(self):
        request = RequestFactory().get(reverse("eit_django_utils:authcheck"))
        request.META["SHIB_UID"] = "jdoe1"
        request.META["Shib-Authentication-Instant"] = datetime.strftime(
            timezone.now() - timedelta(minutes=599), "%Y-%m-%dT%H:%M:%S.%fZ"
        )
        view = authcheck
        response = view(request)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        # print("json: {}".format(data))
        self.assertEquals(data.get("shib_uid"), "jdoe1")
        self.assertLessEqual(data.get("shib_authentication_minutes_remaining", 600), 1)


class TestReauthenticated(EitDjangoUtilsBaseTest):
    def test_authcheck_with_shib_uid(self):
        request = RequestFactory().get(reverse("eit_django_utils:reauthenticated"))
        request.META["SHIB_UID"] = "jdoe1"
        view = Reauthenticated.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response.render(),
            '<h2>Reauthenticated <span class="glyphicon glyphicon-check btn-success"</span></h2>',
        )

    def test_authcheck_without_shib_uid(self):
        request = RequestFactory().get(reverse("eit_django_utils:reauthenticated"))
        view = Reauthenticated.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response.render(), "<h1>Reauthenticating...</h1>")
