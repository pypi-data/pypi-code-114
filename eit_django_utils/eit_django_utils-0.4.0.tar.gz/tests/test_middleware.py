from django.test import override_settings, TestCase, RequestFactory
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.urls import reverse
from re import compile


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


@override_settings(LOCALDEV_SHIB_UID="unknown_user")
class TestUserThatDoesntExist(EitDjangoUtilsBaseTest):
    def test_home_view_403(self):
        response = self.client.get(reverse("eit_django_utils:base"))
        self.assertEqual(response.status_code, 403)

    def test_create_unknown_user(self):
        response = self.client.get(reverse("eit_django_utils:base"))
        user_model = get_user_model()
        self.assertEqual(user_model.objects.count(), 1)

        username_field = user_model.USERNAME_FIELD
        employee = user_model.objects.get(id=1)
        self.assertEquals(getattr(employee, username_field), "jdoe1")
        self.assertNotEquals(getattr(employee, username_field), "unknown_user")


class TestSetLocalDevShibUID(EitDjangoUtilsBaseTest):
    def test_unity_id_content(self):
        user_model = get_user_model()
        username_field = user_model.USERNAME_FIELD
        employee = user_model.objects.get(id=1)
        self.assertEquals(getattr(employee, username_field), "jdoe1")

    def test_unity_id_content2(self):
        user_model = get_user_model()
        username_field = user_model.USERNAME_FIELD
        employee = user_model.objects.get(id=1)
        self.assertNotEquals(getattr(employee, username_field), "jdoe")


@override_settings(
    MIDDLEWARE=[
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        # SetLocalDevShibUID is only for local development!
        "eit_django_utils.backends.custom_auth.SetLocalDevShibUID",
        "eit_django_utils.backends.custom_auth.CustomHijackMiddleware",
        "eit_django_utils.backends.custom_auth.CustomHeaderMiddleware",
        "eit_django_utils.backends.custom_auth.LoginRequiredMiddleware",
        "eit_django_utils.backends.custom_auth.SpecialGroupRequiredMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]
)
class TestSpecialGroupRequired(EitDjangoUtilsBaseTest):
    def test_non_member(self):
        response = self.client.get(reverse("eit_django_utils:base"))
        self.assertEqual(response.status_code, 403)

    def test_testers_member(self):
        testers = Group.objects.create(name="testers")
        user_model = get_user_model()
        username_field = user_model.USERNAME_FIELD
        employee = user_model.objects.get(**{username_field: "jdoe1"})
        employee.groups.add(testers)
        response = self.client.get(reverse("eit_django_utils:base"))
        self.assertEqual(response.status_code, 200)

    def test_eit_admin_member(self):
        eit_admin = Group.objects.create(name="eit_admin")
        user_model = get_user_model()
        username_field = user_model.USERNAME_FIELD
        employee = user_model.objects.get(**{username_field: "jdoe1"})
        employee.groups.add(eit_admin)
        response = self.client.get(reverse("eit_django_utils:base"))
        self.assertEqual(response.status_code, 200)

    @override_settings(ALLOWED_GROUPS=[])
    def test_empty_allowed_groups(self):
        some_custom_group = Group.objects.create(name="some_custom_group")
        user_model = get_user_model()
        username_field = user_model.USERNAME_FIELD
        employee = user_model.objects.get(**{username_field: "jdoe1"})
        employee.groups.add(some_custom_group)
        response = self.client.get(reverse("eit_django_utils:base"))
        self.assertEqual(response.status_code, 403)

    @override_settings(ALLOWED_GROUPS=["some_custom_group"])
    def test_custom_allowed_group(self):
        some_custom_group = Group.objects.create(name="some_custom_group")
        user_model = get_user_model()
        username_field = user_model.USERNAME_FIELD
        employee = user_model.objects.get(**{username_field: "jdoe1"})
        employee.groups.add(some_custom_group)
        response = self.client.get(reverse("eit_django_utils:base"))
        self.assertEqual(response.status_code, 200)


@override_settings(
    MIDDLEWARE=[
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        # SetLocalDevShibUID is only for local development!
        # "eit_django_utils.backends.custom_auth.SetLocalDevShibUID",
        "eit_django_utils.backends.custom_auth.CustomHijackMiddleware",
        "eit_django_utils.backends.custom_auth.CustomHeaderMiddleware",
        "eit_django_utils.backends.custom_auth.LoginRequiredMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]
)
class TestExemptUrls(EitDjangoUtilsBaseTest):
    def test_login_redirect(self):
        response = self.client.get(reverse("eit_django_utils:base"))
        self.assertEquals(response.status_code, 302)

    @override_settings(LOGIN_EXEMPT_URLS=[r"^$"])
    def test_exempt_url(self):
        response = self.client.get(reverse("eit_django_utils:base"))
        self.assertEqual(response.status_code, 200)
